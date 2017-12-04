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
