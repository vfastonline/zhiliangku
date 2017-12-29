#!encoding:utf-8
import json

from django.core.paginator import Paginator
from django.db.models import *
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from applications.custom_user.models import *
from applications.record.models import WatchRecord
from applications.tracks_learning.models import *
from lib.permissionMixin import class_view_decorator, user_login_required


class IndexCourseList(View):
    """首页-热门课程"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": [],
        }
        try:
            # 课程数据
            course_objs = Course.objects.filter(home_show=True)
            result_dict["data"] = [
                {
                    "id": one.id,
                    "name": one.name,
                    "tech": [one_tech.name for one_tech in one.tech.all()] if one.tech.all().exists() else list(),
                    "course_img": one.course_img.url if one.course_img else "",
                    "lecturer": one.lecturer.nickname if one.lecturer else "",
                    "avatar": one.lecturer.avatar.url if one.lecturer.avatar else "",
                }
                for one in course_objs
            ]

        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class QuestionPathInfo(View):
    """课程方向"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": [],
        }
        try:
            # 课程数据
            coursepaths = CoursePath.objects.filter()
            result_dict["data"] = [
                {
                    "id": one.id,
                    "name": one.name,
                }
                for one in coursepaths
            ]

        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class CourseList(View):
    """获取课程信息"""

    def get(self, request, *args, **kwargs):
        template_name = "tracks/course/list/index.html"
        return render(request, template_name, {})


class CourseListInfo(View):
    """获取课程信息"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": [],
            "filter": {
                "course_path": [{"name": "全部", "id": 0, "active": 1}],
                "technology": [{"name": "全部", "id": 0, "active": 1}]
            },
            "paginator": {}
        }
        try:
            # 获取查询参数
            category_id = int(self.request.GET.get("category_id", 0))  # 课程类别
            coursepath_id = int(self.request.GET.get("coursepath_id", 0))  # 课程方向
            technology_id = int(self.request.GET.get("technology_id", 0))  # 技术分类
            page = int(self.request.GET.get("page", 1))  # 页码
            per_page = int(self.request.GET.get("per_page", 12))  # 每页显示条目数

            course_objs = Course.objects.all()

            # 按课程类别查询，路线详情页面
            if category_id:
                coursecategory_objs = CourseCategory.objects.filter(id=category_id).order_by("sequence")
                if coursecategory_objs.exists():
                    course_objs = coursecategory_objs.first().courses.all()

            # 按方向查询，课程列表页
            if coursepath_id and not technology_id:
                coursepaths = CoursePath.objects.filter(id=coursepath_id).first()
                techs = coursepaths.tech.all()
                course_objs = list(set(list(Course.objects.filter(tech__in=techs))))

            # 按技术分类查询，课程列表页
            if technology_id:
                course_objs = Course.objects.filter(tech__id=technology_id)

            # 提供分页数据
            if not category_id:
                page_obj = Paginator(course_objs, per_page)
                total_count = page_obj.count  # 记录总数
                num_pages = page_obj.num_pages  # 总页数
                page_range = list(page_obj.page_range)  # 页码列表
                paginator_dict = {
                    "total_count": total_count,
                    "num_pages": num_pages,
                    "page_range": page_range,
                    "page": page,
                    "per_page": per_page
                }
                result_dict["paginator"] = paginator_dict

                try:
                    course_objs = page_obj.page(page).object_list
                except:
                    course_objs = list()

            # 课程数据
            result_dict["data"] = [
                {
                    "id": one.id,
                    "name": one.name,
                    "tech": [one_tech.name for one_tech in one.tech.all()] if one.tech.all().exists() else list(),
                    "course_img": one.course_img.url if one.course_img else "",
                    "lecturer": one.lecturer.nickname if one.lecturer else "",
                    "avatar": one.lecturer.avatar.url if one.lecturer.avatar else "",
                }
                for one in course_objs
            ]

            # 组装过滤数据
            if not category_id:
                filter_result = self.get_filter_data(coursepath_id, technology_id)
                result_dict["filter"] = filter_result

        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))

    @staticmethod
    def get_filter_data(course_path_id, technology_id):
        """组装过滤数据
        :param course_path_id: 课程方向ID
        :param technology_id: 技术分类ID
        :return:课程方向+课程技术分类信息
        """
        result_dict = {
            "course_path": [{"name": "全部", "id": 0, "active": 1}],
            "technology": [{"name": "全部", "id": 0, "active": 1}]
        }
        try:
            course_paths = CoursePath.objects.all().values()
            if course_paths:
                result_dict["course_path"].extend(course_paths)

            # 增加方向选中flag
            for one in result_dict["course_path"]:
                if int(one.get("id", 0)) == int(course_path_id):
                    one.update({"active": 1})
                    if int(course_path_id) != 0:
                        result_dict["course_path"][0].pop("active")
                    break

            # 组装过滤数据-方向-技术分类
            technologys = list()
            if not course_path_id or course_path_id == "0":
                technologys = Technology.objects.all().values("id", "name")
            else:
                technology_objs = CoursePath.objects.filter(id=course_path_id)
                if technology_objs.exists():
                    technologys = technology_objs.first().tech.all().values("id", "name")
            result_dict["technology"].extend(technologys)

            # 增加分类选中flag
            for one in result_dict["technology"]:
                if int(one.get("id", 0)) == int(technology_id):
                    one.update({"active": 1})
                    if int(technology_id) != 0:
                        result_dict["technology"][0].pop("active")
                    break

        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
        finally:
            return result_dict


class CourseDetail(View):
    """课程详情"""

    def get(self, request, *args, **kwargs):
        template_name = "tracks/course/detail/index.html"
        return render(request, template_name, {})


class CourseDetailInfo(View):
    """课程详情"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": dict()}
        try:
            filter_param = dict()
            course_id = int(request.GET.get('course_id', 0))
            include_video = int(request.GET.get('include_video', 0))  # 是否包含视频信息
            custom_user_id = int(request.GET.get('custom_user_id', 0))  # 用户ID
            detail = dict()
            if course_id:
                filter_param["id"] = course_id
                course_objs = Course.objects.filter(**filter_param)
                if course_objs.exists():
                    course_obj = course_objs.first()
                    detail["id"] = course_obj.id
                    detail["name"] = course_obj.name
                    detail["lecturer"] = course_obj.lecturer.nickname if course_obj.lecturer else ""
                    detail["course_img"] = course_obj.course_img.url if course_obj.course_img else ""
                    detail["prerequisites"] = course_obj.prerequisites
                    detail["learn"] = course_obj.learn
                    detail["tech"] = [one_tech.name for one_tech in
                                      course_obj.tech.all()] if course_obj.tech.all().exists() else list()
                    detail["avatar"] = course_obj.lecturer.avatar.url if course_obj.lecturer.avatar else ""
                    detail["position"] = course_obj.lecturer.position if course_obj.lecturer.position else ""

                    # 默认，汇总数据
                    detail["schedule"] = 0  # 课程完成进度
                    last_time_learn_obj = course_obj.Section.order_by("sequence").first().Videos.order_by(
                        "sequence").first()
                    detail["last_time_learn"] = last_time_learn_obj.name  # 上次学到
                    detail["last_time_learn_id"] = last_time_learn_obj.id  # 上次学到ID

                    # 课程时长
                    duration_sum = Video.objects.filter(section__in=course_obj.Section.all()).aggregate(
                        Sum('duration')).get("duration__sum")
                    detail["total_time"] = 0
                    if duration_sum:
                        detail["total_time"] = duration_sum  # 课程总时长，分钟

                    # 剩余时长
                    detail["remaining_time"] = 0  # 剩余时长，分钟
                    watch_total_time = 0
                    watch_total_time_sum = WatchRecord.objects.filter(user_id=custom_user_id, course=course_obj).values(
                        "video_process").aggregate(Sum('video_process')).get("video_process__sum")  # 秒
                    if watch_total_time_sum:
                        watch_total_time = watch_total_time_sum

                    # 计算剩余时长
                    if duration_sum:
                        if watch_total_time:
                            remaining_seconds = (duration_sum * 60) - watch_total_time_sum
                            minutes, seconds = divmod(remaining_seconds, 60)
                            detail["remaining_time"] = minutes
                            detail["schedule"] = float("%.2f" % (float(remaining_seconds) / float(duration_sum * 60)))
                        else:
                            detail["remaining_time"] = duration_sum
                            detail["schedule"] = 1

                    # 是否收藏
                    detail["is_collect"] = 0  # 用户是否收藏，1：收藏，0：未收藏
                    collect_filter = {
                        "custom_user_id": custom_user_id,
                        "course__in": [course_obj],
                    }
                    customusercourses = CustomUserCourse.objects.filter(**collect_filter)
                    if customusercourses.exists():
                        detail["is_collect"] = 1  # 用户是否收藏，1：收藏，0：未收藏

                    # 用户是否有本课程学习记录
                    detail["is_study_record"] = 0  # 默认用户无学习记录,
                    watchrecord_param = {
                        "user__id": custom_user_id,
                        "course": course_obj,
                    }
                    watchrecords = WatchRecord.objects.filter(**watchrecord_param).order_by("-create_time")
                    if watchrecords.exists():  # 有学习记录
                        detail["is_study_record"] = 1
                        detail["last_time_learn"] = watchrecords.first().video.name  # 上次学到
                        detail["last_time_learn_id"] = watchrecords.first().video.id  # 上次学到ID

                    # 查询课程下所有章节信息
                    detail["sections"] = list()
                    for one_section in course_obj.Section.all().order_by("sequence"):
                        section = {
                            "id": one_section.id,
                            "title": one_section.title,
                            "sequence": one_section.sequence,
                            "desc": one_section.desc,
                        }
                        if include_video:  # 课程详情是否带视频信息
                            videos = one_section.Videos.all().order_by("sequence")
                            video_list = list()
                            if videos.exists():
                                for video in videos:
                                    video_dict = dict()
                                    video_dict["id"] = video.id
                                    video_dict["name"] = video.name
                                    video_dict["type"] = video.type
                                    video_dict["type_name"] = video.get_type_display()
                                    video_dict["live_start_time"] = video.live_start_time.strftime("%M:%S") \
                                        if video.live_start_time else ""
                                    video_dict["is_complete"] = 0

                                    watchrecord_param = {
                                        "user__id": custom_user_id,
                                        "video": video,
                                        "course": course_obj,
                                        "status": 1
                                    }
                                    watchrecords = WatchRecord.objects.filter(**watchrecord_param)
                                    if watchrecords.exists():
                                        video_dict["is_complete"] = 1

                                    video_list.append(video_dict)
                            if video_list:
                                section["videos"] = video_list

                        detail["sections"].append(section)
            result_dict["data"] = detail
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
