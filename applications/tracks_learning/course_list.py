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
                    "name": one.name,
                    "lecturer": one.lecturer.username,
                    "course_img": one.course_img.url,
                    "tech": one.tech.name
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
