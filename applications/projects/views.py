#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.projects.models import *


class PrjectList(View):
    """项目说明"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": []}
        try:
            projects = Project.objects.filter()
            result_dict["data"] = [
                {
                    "id": one.id,
                    "pathwel": one.pathwel.url if one.pathwel else "",
                    "title": one.title,
                    "name": one.name,
                    "desc": one.desc
                }
                for one in projects
            ]
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
