#!encoding:utf-8
import json
import json
import logging
import traceback

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from applications.custom_user.models import CustomUserPath
from applications.record.models import WatchRecord
from applications.tracks_learning.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int


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


class PathList(View):
    """获取职业路径-页面"""

    def get(self, request, *args, **kwargs):
        template_name = "tracks/path/list/index.html"
        return render(request, template_name, {})


class PathListInfo(View):
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


class PathDetail(View):
    """获取职业路径详情"""

    def get(self, request, *args, **kwargs):
        template_name = "tracks/path/detail/index.html"
        return render(request, template_name, {})


class PathDetailInfo(View):
    """获取职业路径详情"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": dict()}
        try:
            filter_param = dict()
            path_id = str_to_int(request.GET.get('path_id', 0))  # 路径ID
            custom_user_id = str_to_int(request.GET.get('custom_user_id', 0))  # 用户ID

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

                    courses_counts = [one.courses.all().count() for one in
                                      CourseCategory.objects.filter(path_stage__in=path_obj.PathStage.all())]
                    courses_total_number = sum(courses_counts)
                    detail["total_number"] = courses_total_number  # 课程总节数

                    detail["pathstages"] = list()
                    for one_path_stage in path_obj.PathStage.all().order_by("sequence"):  # 查询路径下所有阶段信息
                        path_stage = {
                            "id": one_path_stage.id,
                            # "name": one_path_stage.name,
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
                        if coursecategorys:
                            path_stage.update({"coursecategorys": coursecategorys})
                            detail["pathstages"].append(path_stage)

                    # 汇总路线完成情况
                    if custom_user_id:
                        summarize_dict = self.summarize(custom_user_id, path_obj)
                        detail.update(summarize_dict)

            result_dict["data"] = detail
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))

    @staticmethod
    def summarize(custom_user_id, path_obj):
        summarize_dict = {
            "learn_time_consum": "",  # 学习耗时
            "path_complete_schedule": 0,  # 路线完成进度
            "complete_number": 0,  # 完成节数
            "participate": False,  # 用户参与了该路线
        }
        try:
            customuserpaths = CustomUserPath.objects.filter(custom_user__id=custom_user_id, path=path_obj)
            if not customuserpaths.exists():
                return
            summarize_dict["participate"] = True
            coursecategorys = CourseCategory.objects.filter(path_stage__in=path_obj.PathStage.all())
            course_list = list()  # 路线下所有课程
            for one in coursecategorys:
                course_list.extend(list(one.courses.all()))
            course_list = list(set(course_list))

            # 汇总学习耗时
            watch_total_time_sum = WatchRecord.objects.filter(course__in=course_list, user_id=custom_user_id).values(
                "video_process").aggregate(Sum('video_process')).get("video_process__sum")
            m, s = divmod(watch_total_time_sum, 60)
            total_time_str = "%d分%d秒" % (m, s)
            summarize_dict["learn_time_consum"] = total_time_str

            # 汇总完成节数
            filter_param = {
                "course__in": course_list,
                "user_id": custom_user_id,
                "status": 1
            }
            complete_number = WatchRecord.objects.filter(**filter_param).count()
            summarize_dict["complete_number"] = complete_number

            # 汇总路线完成进度
            # 所有课程总时长
            duration_sum = Video.objects.filter(section__course__in=course_list).aggregate(
                Sum('duration')).get("duration__sum")
            schedule = float("%.2f" % (float(watch_total_time_sum) / float(duration_sum)))
            summarize_dict["path_complete_schedule"] = schedule
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
        finally:
            return summarize_dict


@class_view_decorator(user_login_required)
class ParticipatePath(View):
    """参与该学习路径"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "成功参与该学习路径"}
        try:
            param_dict = json.loads(request.body)
            path_id = str_to_int(param_dict.get('path_id', 0))  # 必填，路径ID
            custom_user_id = str_to_int(param_dict.get('custom_user_id', 0))  # 必填，用户ID

            if not path_id:
                result_dict["err"] = 1
                result_dict["msg"] = "缺少学习路径参数"
                return

            if not custom_user_id:
                result_dict["err"] = 1
                result_dict["msg"] = "缺少用户参数"
                return

            paths = Path.objects.filter(id=path_id)
            if not paths.exists():
                result_dict["err"] = 1
                result_dict["msg"] = "学习路径不存在"
                return

            customusers = CustomUser.objects.filter(id=custom_user_id)
            if not customusers.exists():
                result_dict["err"] = 1
                result_dict["msg"] = "用户不存在"
                return

            customuserpaths = CustomUserPath.objects.filter(custom_user__id=custom_user_id)
            if not customuserpaths.exists():
                obj = CustomUserPath.objects.create(custom_user=customusers.first())
                if not obj:
                    result_dict["err"] = 1
                    result_dict["msg"] = "参加学习路径失败"
                    return

                obj.path.add(paths.first())
                obj.save()
                if not obj:
                    result_dict["err"] = 1
                    result_dict["msg"] = "参加学习路径失败"
                    return
            else:
                if not CustomUserPath.objects.filter(custom_user__id=custom_user_id, path__in=paths).exists():
                    obj = customuserpaths.first()
                    obj.path.add(paths.first())
                    obj.save()
                    if not obj:
                        result_dict["err"] = 1
                        result_dict["msg"] = "参加学习路径失败"
                        return
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
