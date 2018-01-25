#!encoding:utf-8
import json

from django.http import HttpResponse
from django.views.generic import View

from applications.custom_user.models import *
from applications.record.models import *
from applications.tracks_learning.course_list import summarize_course_progress
from applications.tracks_learning.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int
from applications.tracks_learning.path_list import user_path_summarize

"""我的课程"""


@class_view_decorator(user_login_required)
class LearnRecently(View):
    """最近学习"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": list(),
        }
        try:
            custom_user_id = str_to_int(request.GET.get('custom_user_id', 0))  # 用户ID

            watchrecords = WatchRecord.objects.filter(user_id=custom_user_id).order_by("-create_time")
            data_list = list()
            if watchrecords.exists():
                for one in watchrecords:
                    data_dict = dict()
                    data_dict["course_name"] = one.course.name
                    data_dict["course_img"] = one.course.course_img.url
                    data_dict["create_time_year"] = one.create_time.strftime("%Y")
                    data_dict["create_time"] = one.create_time.strftime("%m月%d日")
                    data_dict["last_course_id"] = one.course.id  # 最近学习课程ID
                    summarize_dict = summarize_course_progress(custom_user_id, one.course.id)
                    data_dict.update(summarize_dict)
                    data_list.append(data_dict)
            result_dict["data"] = data_list

        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class MyCollect(View):
    """我的收藏"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": list(),
        }
        try:
            custom_user_id = str_to_int(request.GET.get('custom_user_id', 0))  # 用户ID

            customusercourses = CustomUserCourse.objects.filter(custom_user_id=custom_user_id)
            data_list = list()
            if customusercourses.exists():
                for one in customusercourses.first().course.all():
                    data_dict = dict()
                    data_dict["course_id"] = one.id
                    data_dict["course_name"] = one.name
                    data_dict["course_img"] = one.course_img.url
                    summarize_dict = summarize_course_progress(custom_user_id, one.id)
                    data_dict.update(summarize_dict)
                    data_list.append(data_dict)
            result_dict["data"] = data_list

        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class MyPath(View):
    """我的路径"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": list(),
        }
        try:
            custom_user_id = str_to_int(request.GET.get('custom_user_id', 0))  # 用户ID
            
            customuserpaths = CustomUserPath.objects.filter(custom_user_id=custom_user_id)
            data_list = list()
            if customuserpaths.exists():
                for one in customuserpaths.first().path.all():
                    data_dict = dict()
                    data_dict["name"] = one.name
                    data_dict["path_img"] = one.path_img.url
                    data_dict["course_count"] = sum([coursecategory.courses.all().count() for coursecategory in
                                                     CourseCategory.objects.filter(path_stage__path=one)])
                    summarize_dict = user_path_summarize(custom_user_id, one)
                    data_dict.update(summarize_dict)
                    data_list.append(data_dict)
            result_dict["data"] = data_list

        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
