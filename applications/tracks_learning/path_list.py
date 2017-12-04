#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.tracks_learning.models import Path


class PathList(View):
    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": []}
        try:
            path_objs = Path.objects.all()[:3]
            result_dict["data"] = [
                {
                    "id": one.id,
                    "name": one.name,
                    "path_img": one.path_img.url,
                    "desc": one.desc
                }
                for one in path_objs
            ]
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
