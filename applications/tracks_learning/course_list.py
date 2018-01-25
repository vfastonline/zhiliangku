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
from django.http import Http404
from lib.util import str_to_int


class IndexCourseList(View):
    """首页-最新/热门/推荐 课程"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": [],
        }
        try:
            recommend = str_to_int(self.request.GET.get("recommend", 0))  # 推荐课程
            latest = str_to_int(self.request.GET.get("latest", 0))  # 最新课程
            popular = str_to_int(self.request.GET.get("popular", 0))  # 热门课程
            course_objs = list()

            # 推荐课程
            if recommend:
                course_objs = Course.objects.filter(recommend=True).order_by("-update_time")[:16]

            # 最新课程
            if latest:
                course_objs = Course.objects.filter().order_by("-id")[:16]

            # 热门课程
            if popular:
                watchrecords = WatchRecord.objects.values("course").annotate(Count('course')).order_by(
                    "-course__count")[:16]
                course_id_list = [one.get("course", 0) for one in watchrecords]
                course_objs = Course.objects.filter(id__in=course_id_list)
                objects_dict = dict([(obj.id, obj) for obj in course_objs])
                course_objs = [objects_dict[one_id] for one_id in course_id_list]

            result_dict["data"] = [
                {
                    "id": one.id,
                    "name": one.name,
                    "recommend": one.recommend,
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
                "course_path": [{"name": "全部", "id": 0}],
                "technology": [{"name": "全部", "id": 0}]
            },
            "paginator": {}
        }
        try:
            # 获取查询参数
            category_id = str_to_int(self.request.GET.get("category_id", 0))  # 课程类别
            coursepath_id = str_to_int(self.request.GET.get("coursepath_id", 0))  # 课程方向
            technology_id = str_to_int(self.request.GET.get("technology_id", 0))  # 技术分类
            page = self.request.GET.get("page", 1)  # 页码
            per_page = self.request.GET.get("per_page", 12)  # 每页显示条目数

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

            # 无课程类，别组装过滤数据
            if not category_id:
                filter_result = self.get_filter_data(coursepath_id, technology_id)
                result_dict["filter"] = filter_result

        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
            raise Http404()
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
            "course_path": [{"name": "全部", "id": 0}],
            "technology": [{"name": "全部", "id": 0}]
        }
        try:
            course_paths = CoursePath.objects.all().values()
            if course_paths:
                result_dict["course_path"].extend(course_paths)

            # 增加方向选中flag
            if not course_path_id and technology_id:
                coursepaths = CoursePath.objects.filter(tech__id__in=[technology_id])
                if coursepaths.exists():
                    course_path_id = coursepaths.first().id

            for one in result_dict["course_path"]:
                if int(one.get("id", 0)) == int(course_path_id):
                    one.update({"active": 1})
                    break

            # 组装过滤数据-方向-技术分类
            technologys = list()
            if not course_path_id:
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
            course_id = str_to_int(request.GET.get('course_id', 0))
            include_video = str_to_int(request.GET.get('include_video', 0))  # 是否包含视频信息
            custom_user_id = str_to_int(request.GET.get('custom_user_id', 0))  # 用户ID
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

                    # 汇总数据学习进度
                    summarize_dict = summarize_course_progress(custom_user_id, course_obj.id)
                    detail["total_time"] = summarize_dict.get("total_time")
                    detail["remaining_time"] = summarize_dict.get("remaining_time")  # 剩余时长，分钟
                    detail["schedule"] = summarize_dict.get("schedule")
                    detail["is_study_record"] = summarize_dict.get("is_study_record")  # 是否有用户无学习记录
                    detail["last_time_learn"] = summarize_dict.get("last_time_learn")  # 最近学习视频名称
                    detail["last_time_learn_id"] = summarize_dict.get("last_time_learn_id")  # 最近学习视频ID
                    detail["last_time_learn_type"] = summarize_dict.get("last_time_learn_type")  # 最近学习视频类型
                    detail["vid"] = summarize_dict.get("vid")  # 最近学习视频类型
                    detail["video_process"] = summarize_dict.get("video_process")  # 最近学习视频观看进度

                    # 是否收藏
                    detail["is_collect"] = 0  # 用户是否收藏，1：收藏，0：未收藏
                    collect_filter = {
                        "custom_user_id": custom_user_id,
                        "course__in": [course_obj],
                    }
                    customusercourses = CustomUserCourse.objects.filter(**collect_filter)
                    if customusercourses.exists():
                        detail["is_collect"] = 1  # 用户是否收藏，1：收藏，0：未收藏

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
            raise Http404()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


def summarize_course_progress(custom_user_id, course_id):
    """汇总课程完成进度
    :param custom_user_id:用户ID
    :param course_id:课程ID
    :return:课程学习进度
    """
    result_dict = {
        "total_time": "",  # 课程总时长，秒
        "remaining_time": "",  # 用户剩余学习时长，秒
        "schedule": 0,  # 课程学习进度
        "is_study_record": 0,  # 是否有课程学习记录
        "last_time_learn": "",  # 最近一次学习视频名称
        "last_time_learn_id": "",  # 最近一次学习视频ID
        "last_time_learn_type": "",  # 最近一次学习视频类型
        "vid": "",  # 最近一次学习视频vid
        "video_process": 0,  # 最近一次学习视频观看进度
    }
    try:
        course_objs = Course.objects.filter(id=course_id)
        if course_objs.exists() and custom_user_id:
            course_obj = course_objs.first()

            # 课程时长
            duration_sum = Video.objects.filter(section__in=course_obj.Section.all()).aggregate(
                Sum('duration')).get("duration__sum")

            # 用户已经看了多长时间
            watchrecords = WatchRecord.objects.filter(user_id=custom_user_id, course=course_obj).order_by(
                "-create_time")
            watch_total_time_sum = watchrecords.values("video_process").aggregate(Sum('video_process')).get(
                "video_process__sum")  # 秒

            # 计算剩余时长
            if duration_sum:
                m, s = divmod(duration_sum, 60)
                h, m = divmod(m, 60)
                total_time_str = "%02d:%02d:%02d" % (h, m, s)
                result_dict["total_time"] = total_time_str
                if watch_total_time_sum:
                    one_watchrecord = watchrecords.first()
                    last_time_learn = one_watchrecord.video.name  # 上次学到
                    last_time_learn_id = one_watchrecord.video.id  # 上次学到视频ID
                    vid = one_watchrecord.video.vid if one_watchrecord.video.vid else ""  # 上次学到视频ID
                    last_time_learn_type = one_watchrecord.video.type  # 上次学到视频类型
                    remaining_time = duration_sum - watch_total_time_sum
                    schedule = float("%.2f" % (float(watch_total_time_sum) / float(duration_sum)))
                    result_dict["is_study_record"] = 1
                    result_dict["last_time_learn"] = last_time_learn
                    result_dict["last_time_learn_id"] = last_time_learn_id
                    result_dict["last_time_learn_type"] = last_time_learn_type
                    result_dict["vid"] = vid
                    result_dict["video_process"] = one_watchrecord.video_process

                else:
                    remaining_time = duration_sum
                    schedule = 0

                    # 默认最近最近学习第一章第一个视频
                    course_sections = course_obj.Section.order_by("sequence")
                    if course_sections:
                        last_time_learn_objs = course_sections.first().Videos.order_by("sequence")
                        if last_time_learn_objs:
                            last_time_learn_obj = last_time_learn_objs.first()
                            result_dict["last_time_learn"] = last_time_learn_obj.name  # 上次学到
                            result_dict["last_time_learn_id"] = last_time_learn_obj.id  # 上次学到视频ID
                            result_dict["last_time_learn_type"] = last_time_learn_obj.type  # 上次学到视频类型
                            result_dict["vid"] = last_time_learn_obj.vid  # 上次学到视频类型

                m, s = divmod(remaining_time, 60)
                h, m = divmod(m, 60)
                remaining_time_str = "02d:%02d:%02d" % (h, m, s)
                result_dict["remaining_time"] = remaining_time_str
                result_dict["schedule"] = schedule
    except:
        traceback.print_exc()
        logging.getLogger().error(traceback.format_exc())
    finally:
        return result_dict
