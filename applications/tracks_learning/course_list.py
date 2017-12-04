#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.tracks_learning.models import Course


class CourseList(View):
    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": []}
        try:
            course_objs = Course.objects.all()[:8]
            data_list = list()
            for one in course_objs:
                one_dict = dict()
                one_dict["id"] = one.id
                one_dict["name"] = one.name
                one_dict["lecturer"] = ""
                one_dict["tech"] = []
                one_dict["course_img"] = one.course_img.url
                if one.lecturer:
                    one_dict["name"] = one.lecturer.nickname
                if one.tech.all():
                    [one_dict["tech"].append(one_tech.name) for one_tech in one.tech.all()]
                data_list.append(one_dict)
            result_dict["data"] = data_list
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
