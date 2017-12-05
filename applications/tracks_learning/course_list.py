#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.tracks_learning.models import *


class CourseList(View):
    """获取课程信息"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": []}
        try:
            filter_param = dict()
            home_show = self.request.GET.get("home_show")  # 是否首页显示
            category_id = self.request.GET.get("category_id")  # 课程类别
            if home_show:
                filter_param["home_show"] = True if home_show == "true" else False

            course_objs = Course.objects.filter(**filter_param)

            if category_id:
                course_objs = list()
                coursecategory_objs = CourseCategory.objects.filter(id=category_id)
                if coursecategory_objs.exists():
                    course_objs = coursecategory_objs.first().courses.all()

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
