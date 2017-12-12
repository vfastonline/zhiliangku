#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.tracks_learning.models import *
from lib.permissionMixin import class_view_decorator, user_login_required


class IndexPathList(View):
    """获取首页职业路径"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": []}
        try:
            path_objects = Path.objects.filter(home_show=True)
            result_dict["data"] = [
                {
                    "id": one.id,
                    "name": one.name,
                    "path_img": one.path_img.url,
                    "desc": one.desc,
                }
                for one in path_objects
            ]
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class PathList(View):
    """获取职业路径"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": []}
        try:
            path_objects = Path.objects.all()
            result_dict["data"] = [
                {
                    "id": one.id,
                    "name": one.name,
                    "path_img": one.path_img.url,
                    "desc": one.desc,
                    "lowest_salary": one.lowest_salary,
                    "highest_salary": one.highest_salary,
                    "courses_count": sum([coursecategory.courses.all().count() for coursecategory in
                                          CourseCategory.objects.filter(path_stage__path=one)]),
                }
                for one in path_objects
            ]
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class PathDetail(View):
    """获取职业路径详情"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": dict()}
        try:
            filter_param = dict()
            path_id = json.loads(request.body).get('path_id')
            detail = dict()
            if path_id:
                filter_param["id"] = path_id

                path_objs = Path.objects.filter(**filter_param)
                if path_objs.exists():
                    path_obj = path_objs.first()
                    detail["id"] = path_obj.id
                    detail["name"] = path_obj.name
                    detail["desc"] = path_obj.desc
                    detail["path_img"] = path_obj.path_img.url
                    detail["lowest_salary"] = path_obj.lowest_salary
                    detail["highest_salary"] = path_obj.highest_salary
                    detail["courses_count"] = sum([coursecategory.courses.all().count() for coursecategory in
                                                   CourseCategory.objects.filter(path_stage__path=path_obj)])
                    detail["learn_time_consum"] = 31  # 学习耗时
                    detail["path_complete_schedule"] = 0.3  # 路线完成进度
                    detail["complete_number"] = 3  # 完成节数
                    courses_counts = [one.courses.all().count() for one in
                                      CourseCategory.objects.filter(path_stage__in=path_obj.PathStage.all())]
                    courses_total_number = sum(courses_counts)
                    detail["total_number"] = courses_total_number  # 课程总节数

                    detail["pathstages"] = list()
                    for one_path_stage in path_obj.PathStage.all().order_by("sequence"):  # 查询路径下所有阶段信息
                        path_stage = {
                            "id": one_path_stage.id,
                            "name": one_path_stage.name,
                            "sequence": one_path_stage.sequence,
                        }
                        coursecategorys = list()
                        for one_coursecategory in one_path_stage.CourseCategory.all():  # 查询路径阶段下所有课程类别信息
                            course_category = {
                                "id": one_coursecategory.id,
                                "name": one_coursecategory.name,
                                "sequence": one_coursecategory.sequence,
                            }
                            coursecategorys.append(course_category)
                        path_stage.update({"coursecategorys": coursecategorys})
                        detail["pathstages"].append(path_stage)

            result_dict["data"] = detail
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
