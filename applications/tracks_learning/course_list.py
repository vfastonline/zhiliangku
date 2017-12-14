#!encoding:utf-8
import json
import logging
import traceback

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.generic import View

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


# @class_view_decorator(user_login_required)
class CourseList(View):
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
            category_id = self.request.GET.get("category_id")  # 课程类别
            coursepath_id = self.request.GET.get("coursepath_id", 0)  # 课程方向
            technology_id = self.request.GET.get("technology_id", 0)  # 技术分类
            page_number = self.request.GET.get("page", 1)  # 页码

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
                course_objs = Course.objects.filter(tech__in=techs)

            # 按技术分类查询，课程列表页
            if technology_id:
                course_objs = Course.objects.filter(tech__id=technology_id)

            # 提供分页数据
            page_obj = Paginator(course_objs, 12)
            total_count = page_obj.count  # 记录总数
            num_pages = page_obj.num_pages  # 总页数
            page_range = list(page_obj.page_range)  # 页码列表
            paginator_dict = {
                "total_count": total_count,
                "num_pages": num_pages,
                "page_range": page_range,
                "page_number": page_number
            }
            result_dict["paginator"] = paginator_dict

            try:
                course_objs = page_obj.page(page_number).object_list
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


# @class_view_decorator(user_login_required)
class CourseDetail(View):
    """课程详情"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": dict()}
        try:
            filter_param = dict()
            course_id = json.loads(request.body).get('course_id')
            logging.getLogger().error(course_id)
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

                    # 假数据，待汇总
                    detail["schedule"] = 0.3  # 课程完成进度
                    detail["last_time_learn"] = "修改进程优先级"  # 上次学到
                    detail["remaining_time_hour"] = 2  # 剩余时长小时数
                    detail["remaining_time_minute"] = 15  # 剩余时长分钟数
                    detail["is_collect"] = 1  # 用户是否收藏，1：收藏，0：未收藏

                    detail["sections"] = list()
                    for one_section in course_obj.Section.all().order_by("sequence"):  # 查询课程下所有章节信息
                        section = {
                            "id": one_section.id,
                            "title": one_section.title,
                            "sequence": one_section.sequence,
                            "desc": one_section.desc,
                        }
                        detail["sections"].append(section)
            result_dict["data"] = detail
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
