#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.slideshow.models import Carousel


class SlideList(View):
    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": []}
        try:
            carousel_objs = Carousel.objects.all()
            result_dict["data"] = [
                {"id": one.id, "name": one.name, "pathwel": one.pathwel.url}
                for one in carousel_objs
            ]
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
