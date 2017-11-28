#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.tracks_learning.models import Course


class CourseList(View):
    def post(self, request, *args, **kwargs):
        result_dict = {"err": 0, "message": "success", "data": []}
        try:
            course_objs = Course.objects.all().values("name", "lecturer__username", "course_img", "tech__name")
            result_dict["data"] = list(course_objs)
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["message"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
