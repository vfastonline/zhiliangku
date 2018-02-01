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
                        summarize_dict = user_path_summarize(custom_user_id, path_obj)
                        detail.update(summarize_dict)

            result_dict["data"] = detail
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


def user_path_summarize(custom_user_id, path_obj):
    """汇总路径学习情况
    :param custom_user_id:用户ID
    :param path_obj:路径对象
    :return:
    """
    summarize_dict = {
        "learn_time_consum": "",  # 学习耗时
        "path_complete_schedule": 0,  # 路线完成进度
        "complete_number": 0,  # 完成节数
        "participate": False,  # 用户参与了该路线
        "last_course_id": "",  # 最近一次学习课程ID
        "last_video_type": "",  # 最近一次学习视频类型
        "last_video_id": "",  # 最近一次学习视频ID
        "vid": "",  # 最近一次学习视频vid
        "video_process": 0,  # 最近一次学习视频观看进度
    }
    try:
        # 是否参与该路径
        customuserpaths = CustomUserPath.objects.filter(custom_user__id=custom_user_id, path=path_obj)
        if not customuserpaths.exists():
            return

        summarize_dict["participate"] = True

        # 获取路线下所有课程
        course_list = list()
        coursecategorys = CourseCategory.objects.filter(path_stage__in=path_obj.PathStage.all())
        for one in coursecategorys:
            course_list.extend(list(one.courses.all()))
        course_list = list(set(course_list))

        # 观看记录
        watchrecord_objs = WatchRecord.objects.filter(course__in=course_list, user_id=custom_user_id)

        # 汇总学习耗时
        watch_total_time_sum = watchrecord_objs.values(
            "video_process").aggregate(Sum('video_process')).get("video_process__sum")
        m, s = divmod(watch_total_time_sum, 60)
        h, m = divmod(m, 60)
        total_time_str = "%02d:%02d:%02d" % (h, m, s)
        summarize_dict["learn_time_consum"] = total_time_str

        # 汇总完成节数
        complete_number = watchrecord_objs.filter(status=1).count()
        summarize_dict["complete_number"] = complete_number

        # 汇总路线完成进度
        # 所有课程总时长
        duration_sum = Video.objects.filter(section__course__in=course_list).aggregate(
            Sum('duration')).get("duration__sum")
        schedule = float("%.2f" % (float(watch_total_time_sum) / float(duration_sum)))
        summarize_dict["path_complete_schedule"] = schedule

        # 最近一次观看记录
        last_watchs = watchrecord_objs.filter(status=0).order_by("-create_time")
        if last_watchs.exists():
            last_watch = last_watchs.first()
            summarize_dict["last_course_id"] = last_watch.course.id
            summarize_dict["last_video_type"] = last_watch.video.type
            summarize_dict["last_video_id"] = last_watch.video.id
            summarize_dict["vid"] = last_watch.video.vid if last_watch.video.vid else ""
            summarize_dict["video_process"] = last_watch.video_process
        else:  # 默认路径下第一个课程第一个视频
            if course_list:
                last_course = course_list[0]
                summarize_dict["last_course_id"] = last_course.id

                # 默认最近最近学习第一章第一个视频
                course_sections = last_course.Section.order_by("sequence")
                if course_sections:
                    last_time_learn_objs = course_sections.first().Videos.order_by("sequence")
                    if last_time_learn_objs:
                        last_video = last_time_learn_objs.first()
                        summarize_dict["last_video_type"] = last_video.type
                        summarize_dict["last_video_id"] = last_video.id
                        summarize_dict["vid"] = last_video.vid if last_video.vid else ""
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

            filter_param = {
                "custom_user": customusers.first(),
                "path": paths.first()
            }
            customuserpaths = CustomUserPath.objects.filter(**filter_param)
            if not customuserpaths.exists():
                obj = CustomUserPath.objects.create(**filter_param)
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
