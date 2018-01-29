#!encoding:utf-8
import json

from django.http import HttpResponse
from django.db.models import *
from django.shortcuts import render
from django.views.generic import View

from applications.custom_user.models import *
from applications.record.models import WatchRecord
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int


@class_view_decorator(user_login_required)
class PersonalCenter(View):
    """个人中心-页面"""

    def get(self, request, *args, **kwargs):
        template_name = "personal_center/page/index.html"
        return render(request, template_name, {})


@class_view_decorator(user_login_required)
class PersonalCenterBasicInfo(View):
    """个人中心--基础信息"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": dict(),
        }
        try:
            custom_user_id = str_to_int(request.GET.get('custom_user_id', 0))  # 用户ID
            customusers = CustomUser.objects.filter(id=custom_user_id)
            data_dict = dict()
            if customusers.exists():
                customuser = customusers.first()
                data_dict["nickname"] = customuser.nickname
                data_dict["avatar"] = customuser.avatar.url
                data_dict["signature"] = customuser.signature if customuser.signature else ""
                video_process = WatchRecord.objects.filter(user__id=custom_user_id).aggregate(Sum('video_process')).get(
                    "video_process__sum")
                duration = WatchRecord.objects.filter(user__id=custom_user_id, status=1).aggregate(Sum('duration')).get(
                    "duration__sum")
                learn_time = video_process + duration
                m, s = divmod(learn_time, 60)
                h, m = divmod(m, 60)
                data_dict["learn_time"] = "%02d:%02d:%02d" % (h, m, s)
                data_dict["integral"] = customuser.integral
                data_dict["sex"] = customuser.get_sex_display()
            result_dict["data"] = data_dict
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
