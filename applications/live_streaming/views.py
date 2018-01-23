#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.tracks_learning.models import Video


class IndexLiveList(View):
    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": []}
        try:
            lives = Video.objects.filter(type="3").order_by("live_start_time")
            result_dict["data"] = [
                {
                    "video_id": one.id,
                    "course_id": one.section.course.id,
                    "name": one.name,
                    "pathwel": one.section.course.course_img.url if one.section else "",
                    "desc": one.desc,
                    "status": one.live.status if one.live else "end",
                    "start_time": one.live_start_time.strftime("%H:%M") if one.live_start_time else "",
                }
                for one in lives
            ]
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
