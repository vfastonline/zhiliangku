#!encoding:utf-8
import json

from django.http import HttpResponse
from django.views.generic import View

from applications.custom_user.models import *
from applications.record.models import *
from applications.tracks_learning.course_list import summarize_course_progress
from applications.tracks_learning.models import *
from applications.tracks_learning.path_list import user_path_summarize
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int

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
            custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
            query_sql = 'SELECT * FROM WatchRecord WHERE user_id=%s GROUP BY course_id ORDER BY create_time DESC' % custom_user_id
            watchrecords = WatchRecord.objects.raw(query_sql)

            data_list = list()
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
            custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID

            customusercourses = CustomUserCourse.objects.filter(custom_user_id=custom_user_id)
            data_list = list()
            if customusercourses.exists():
                for one in customusercourses:
                    data_dict = dict()
                    data_dict["course_name"] = one.course.name
                    data_dict["course_img"] = one.course.course_img.url
                    data_dict["create_time_year"] = one.create_time.strftime("%Y")
                    data_dict["create_time"] = one.create_time.strftime("%m月%d日")
                    data_dict["last_course_id"] = one.course.id
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
class MyPath(View):
    """我的路径"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": list(),
        }
        try:
            custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID

            customuserprojects = CustomUserProject.objects.filter(custom_user_id=custom_user_id)
            data_list = list()
            if customuserprojects.exists():
                for one in customuserprojects:
                    data_dict = dict()
                    data_dict["name"] = one.path.name
                    data_dict["path_img"] = one.path.path_img.url
                    data_dict["create_time_year"] = one.create_time.strftime("%Y")
                    data_dict["create_time"] = one.create_time.strftime("%m月%d日")
                    # data_dict["course_count"] = sum([coursecategory.courses.all().count() for coursecategory in
                    #                                  CourseCategory.objects.filter(path_stage__path=one.path)])
                    summarize_dict = user_path_summarize(custom_user_id, one.path)
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
class Recommend(View):
    """推荐课程"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": list(),
        }
        try:
            course_objs = Course.objects.filter()[:4]
            data_list = list()
            if course_objs.exists():
                for one in course_objs:
                    data_dict = dict()
                    data_dict["name"] = one.name
                    data_dict["lecturer"] = one.lecturer.nickname
                    data_dict["description"] = one.desc
                    data_list.append(data_dict)
            result_dict["data"] = data_list

        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
