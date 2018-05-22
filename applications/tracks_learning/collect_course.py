#!encoding:utf-8
import json

from django.http import HttpResponse
from django.views.generic import View

from applications.custom_user.models import *
from applications.tracks_learning.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int


@class_view_decorator(user_login_required)
class CollectCourse(View):
    """收藏/取消收藏这个课程"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "成功收藏这个课程"}
        try:
            param_dict = json.loads(request.body)
            course_id = str_to_int(param_dict.get('course_id', 0))  # 必填，课程ID
            custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
            is_collect = str_to_int(param_dict.get('is_collect', 0))  # 必填，1：收藏；0：取消收藏

            if custom_user_id and course_id:
                courses = Course.objects.filter(id=course_id)
                customusers = CustomUser.objects.filter(id=custom_user_id)
                if courses.exists() and customusers.exists():
                    filter_param = {
                        "custom_user": customusers.first(),
                        "course": courses.first()
                    }
                    customusercourses = CustomUserCourse.objects.filter(**filter_param)
                    if is_collect:  # 收藏
                        if not customusercourses.exists():
                            collect_obj = CustomUserCourse.objects.create(**filter_param)
                            if not collect_obj:
                                result_dict["msg"] = "收藏失败"
                    else:  # 取消收藏
                        if customusercourses.exists():
                            customusercourses.delete()
                        result_dict["msg"] = "成功取消收藏"
                else:
                    result_dict["err"] = 1
                    result_dict["msg"] = "课程或用户不存在"

            else:
                result_dict["err"] = 1
                result_dict["msg"] = "缺少参数"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
