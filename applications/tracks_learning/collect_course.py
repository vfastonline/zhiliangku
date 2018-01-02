#!encoding:utf-8
import json

from django.http import HttpResponse
from django.views.generic import View

from applications.custom_user.models import *
from applications.tracks_learning.models import *
from lib.permissionMixin import class_view_decorator, user_login_required


# @class_view_decorator(user_login_required)
class CollectCourse(View):
    """收藏/取消收藏这个课程"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "成功收藏这个课程"}
        try:
            param_dict = json.loads(request.body)
            course_id = int(param_dict.get('course_id', 0))  # 必填，课程ID
            custom_user_id = int(param_dict.get('custom_user_id', 0))  # 必填，用户ID
            is_collect = int(param_dict.get('is_collect', 0))  # 必填，1：收藏；0：取消收藏

            if custom_user_id and course_id:
                courses = Course.objects.filter(id=course_id)
                customusers = CustomUser.objects.filter(id=custom_user_id)
                if courses.exists() and customusers.exists():
                    customusercourses = CustomUserCourse.objects.filter(custom_user=customusers.first())
                    if is_collect:
                        if not customusercourses.exists():
                            collect_obj = CustomUserCourse.objects.create(custom_user=customusers.first())
                            collect_obj.course.add(courses.first())
                            collect_obj.save()

                            if not collect_obj:
                                result_dict["msg"] = "收藏失败"
                        else:
                            add_obj = customusercourses.first()
                            add_obj.course.add(courses.first())
                            add_obj.save()
                    else:
                        if customusercourses.exists():
                            customusercourses.first().course.remove(courses.first())

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
