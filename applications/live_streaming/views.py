#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.live_streaming.models import Live


class LiveList(View):
    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": []}
        try:
            live_objs = Live.objects.all().order_by("start_time")
            result_dict["data"] = [
                {
                    "id": one.id,
                    "name": one.name,
                    "pathwel": one.pathwel.url,
                    "desc": one.desc,
                    "status": one.status,
                    "start_time": one.start_time.strftime("%H:%M") if one.start_time else "",
                }
                for one in live_objs
            ]
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
