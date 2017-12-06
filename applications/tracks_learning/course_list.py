#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.tracks_learning.models import *
from django.core.paginator import Paginator


class CourseList(View):
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
            home_show = self.request.GET.get("home_show")  # 是否首页显示
            category_id = self.request.GET.get("category_id")  # 课程类别
            coursepath_id = self.request.GET.get("coursepath_id")  # 课程方向
            technology_id = self.request.GET.get("technology_id")  # 技术分类
            page_number = self.request.GET.get("page", 1)  # 页码

            filter_param = dict()
            if home_show == "true":
                filter_param["home_show"] = True

            course_objs = Course.objects.filter(**filter_param)

            # 按课程类别查询
            if category_id:
                course_objs = list()
                coursecategory_objs = CourseCategory.objects.filter(id=category_id)
                if coursecategory_objs.exists():
                    course_objs = coursecategory_objs.first().courses.all()

            # 按技术分类查询
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
            filter_result = self.get_filter_data(coursepath_id)
            result_dict["filter"] = filter_result

        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))

    @staticmethod
    def get_filter_data(course_path_id):
        """组装过滤数据
        :param course_path_id: 课程方向ID
        :return:
        """
        result_dict = {"course_path": [{"name": "全部", "id": 0}], "technology": [{"name": "全部", "id": 0}]}
        try:
            course_paths = CoursePath.objects.all().values()
            if course_paths:
                result_dict["course_path"].extend(course_paths)

            # 组装锅炉数据-方向-技术分类
            technologys = list()
            if not course_path_id:
                technologys = Technology.objects.all().values("id", "name")
            else:
                technology_objs = CoursePath.objects.filter(id=course_path_id)
                if technology_objs.exists():
                    technologys = technology_objs.first().tech.all().values("id", "name")
            result_dict["technology"].extend(technologys)
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
        finally:
            return result_dict
