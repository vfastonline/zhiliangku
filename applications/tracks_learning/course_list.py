#!encoding:utf-8
from django.db.models import *
from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from urllib import parse

from applications.record.models import WatchRecord
from applications.tracks_learning.models import *
from applications.tracks_learning.projects_list import project_summarize_course_progress
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import *
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


class SearchForCourse(View):
    """首页--模糊查询--课程信息"""

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
            name = self.request.GET.get("name")
            name = parse.unquote(name)
            page = self.request.GET.get("page", 1)  # 页码
            per_page = self.request.GET.get("per_page", 12)  # 每页显示条目数
            if name:
                # 模糊查询字段：课程名称，先修要求，你将学到什么，课程描述，技术分类
                course_objs = Course.objects.filter(Q(name__icontains=name)
                                                    | Q(prerequisites__icontains=name)
                                                    | Q(learn__icontains=name)
                                                    | Q(description__icontains=name)
                                                    | Q(tech__name__icontains=name)
                                                    )

                if course_objs:
                    course_objs = list(set(list(course_objs)))
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
                            "tech": [one_tech.name for one_tech in
                                     one.tech.all()] if one.tech.all().exists() else list(),
                            "course_img": one.course_img.url if one.course_img else "",
                            "lecturer": one.lecturer.nickname if one.lecturer else "",
                            "avatar": one.lecturer.avatar.url if one.lecturer.avatar else "",
                        }
                        for one in course_objs
                    ]
            filter_result = get_filter_data(0, 0)
            result_dict["filter"] = filter_result

        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


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
                filter_result = get_filter_data(coursepath_id, technology_id)
                result_dict["filter"] = filter_result

        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
            raise Http404()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


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


@class_view_decorator(user_login_required)
class CourseDetail(View):
    """课程详情"""

    def get(self, request, *args, **kwargs):
        template_name = "tracks/course/detail/index.html"
        return render(request, template_name, {})


def section_is_unlock(custom_user_id, section, sections=list(), previous_num=1):
    """章节是否解锁
    :param custom_user_id: 当前登录用户
    :param section: 当前章节
    :param sections: 课程下所有章节
    :param previous_num: 上N个章节
    :return:
    """
    is_unlock = False
    try:
        previous_section = None
        previous_index = sections.index(section) - previous_num
        if previous_index >= 0:
            previous_section = sections[previous_index]

        if not previous_section:  # 没有上一章节
            is_unlock = True
        else:
            previous_section_has_assessment = False  # 上一个章节中有考核
            assessment_video = previous_section.Videos.filter(type="3")  # 上一个课程->章节->考核
            if assessment_video.exists():
                previous_section_has_assessment = True
                filter_param = {
                    "custom_user__id": custom_user_id,
                    "video": assessment_video.first(),
                    "is_pass": True
                }
                unlockvideos = UnlockVideo.objects.filter(**filter_param)
                if unlockvideos.exists():
                    is_unlock = True

            # 上一个章节中都没有考核
            if not previous_section_has_assessment:
                # 迭代查找上一个课程是否有通过考核
                return section_is_unlock(custom_user_id, section, sections, previous_num + 1)
    except:
        traceback.print_exc()
        return is_unlock
    return is_unlock


@class_view_decorator(user_login_required)
class CourseDetailInfo(View):
    """课程详情"""

    def __init__(self):
        super(CourseDetailInfo, self).__init__()
        self.result_dict = {"err": 0, "msg": "success", "data": dict(), "breadcrumbs": ""}
        self.course_id = 0
        self.project_id = 0
        self.custom_user_id = 0
        self.previous_course = None

    def get(self, request, *args, **kwargs):
        try:
            self.course_id = str_to_int(request.GET.get('course_id', 0))
            self.custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID

            detail = dict()
            if self.course_id:
                course_objs = Course.objects.filter(id=self.course_id)
                if course_objs.exists():
                    course = course_objs.first()
                    self.project_id = course.project.id
                    detail["id"] = course.id
                    detail["name"] = course.name
                    detail["lecturer"] = course.lecturer.nickname if course.lecturer else ""
                    detail["avatar"] = course.lecturer.avatar.url if course.lecturer else ""
                    detail["position"] = course.lecturer.position if course.lecturer else ""
                    detail["desc"] = course.desc
                    detail["summary"] = {}

                    # 汇总课程学习进度
                    courses = course.project.Courses.all().order_by("sequence")  # 项目下所有课程
                    summarize_dict = project_summarize_course_progress(self.custom_user_id, course, list(courses))
                    detail["summary"] = summarize_dict

                    # 查询课程下所有章节信息
                    detail["sections"] = list()
                    sections = course.Section.all().order_by("sequence")
                    for one_section in sections:
                        section = {
                            "id": one_section.id,
                            "title": one_section.title,
                        }
                        videos = one_section.Videos.all().order_by("sequence")  # 章节下所有课程列表

                        video_list = list()
                        if videos.exists():
                            # 通过章节中的考核判断视频是否解锁
                            unlock = section_is_unlock(self.custom_user_id, one_section, list(sections))

                            for video in videos:
                                video_dict = dict()
                                video_dict["id"] = video.id
                                video_dict["name"] = video.name
                                video_dict["type"] = video.type
                                video_dict["type_name"] = video.get_type_display()
                                video_dict["is_complete"] = 0
                                video_dict["vid"] = video.vid
                                video_dict["subtitle"] = video.subtitle.url if video.subtitle else ""
                                video_dict["unlock"] = unlock
                                if video.type in ["1", "2"]:
                                    m, s = divmod(video.duration, 60)
                                else:
                                    m, s = divmod(video.assess_time * 60, 60)
                                h, m = divmod(m, 60)
                                video_dict["duration"] = "%02d:%02d:%02d" % (h, m, s)

                                watchrecord_param = {
                                    "user__id": self.custom_user_id,
                                    "video": video,
                                    "course": course,
                                    "status": 1
                                }
                                if video.type == "1":
                                    watchrecords = WatchRecord.objects.filter(**watchrecord_param)
                                    if watchrecords.exists():
                                        video_dict["is_complete"] = 1

                                param = {
                                    "custom_user__id": self.custom_user_id,
                                    "video": video,
                                    "is_pass": True
                                }
                                if video.type == "3":
                                    unlockvideos = UnlockVideo.objects.filter(**param)
                                    if unlockvideos.exists():
                                        video_dict["is_complete"] = 1

                                video_list.append(video_dict)
                        if video_list:
                            section["videos"] = video_list

                        detail["sections"].append(section)
            self.result_dict["data"] = detail

            # 面包屑
            self.make_breadcrumbs()
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            self.result_dict["err"] = 1
            self.result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))

    def get_previous_course(self, course, courses, previous_num):
        """获取上一个课程"""
        try:
            self.previous_course = None
            previous_index = courses.index(course) - previous_num
            if previous_index >= 0:
                self.previous_course = courses[previous_index]
        except:
            traceback.print_exc()

    def make_breadcrumbs(self):
        """制作面包屑"""
        try:
            project_detail_url = "?".join([reverse('tracks:project-detail'), "project_id=%s" % self.project_id])
            self.request.breadcrumbs([
                (u"主页", reverse('home')),
                (u"项目", reverse('tracks:projects')),
                (u"项目课程", project_detail_url),
                (u"课程详情", "#"),
            ])
            self.result_dict["breadcrumbs"] = make_bread_crumbs(self.request)
        except:
            traceback.print_exc()


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
        if course_objs.exists():
            course_obj = course_objs.first()

            # 课程时长
            duration_sum = Video.objects.filter(section__in=course_obj.Section.all()).aggregate(Sum('duration')).get(
                "duration__sum")
            m, s = divmod(duration_sum, 60)
            h, m = divmod(m, 60)
            total_time_str = "%02d:%02d:%02d" % (h, m, s)
            result_dict["total_time"] = total_time_str

            if custom_user_id:

                # 用户已经看了多长时间
                watchrecords = WatchRecord.objects.filter(user_id=custom_user_id, course=course_obj).order_by(
                    "-create_time")
                watch_total_time_sum = watchrecords.values("video_process").aggregate(Sum('video_process')).get(
                    "video_process__sum")  # 秒

                # 计算剩余时长
                if duration_sum and watch_total_time_sum:
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
                remaining_time_str = "%02d:%02d:%02d" % (h, m, s)
                result_dict["remaining_time"] = remaining_time_str
                result_dict["schedule"] = schedule
    except:
        traceback.print_exc()
        logging.getLogger().error(traceback.format_exc())
    finally:
        return result_dict
