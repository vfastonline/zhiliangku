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
            filter_param = dict()
            category = self.request.GET.get("category")
            if category:
                filter_param["category"] = category

            carousel_objects = Carousel.objects.filter(**filter_param)
            result_dict["data"] = [
                {
                    "id": one.id,
                    "name": one.name,
                    "pathwel": one.pathwel.url,
                    "category_name": one.get_category_display(),
                    "category": one.category,
                    "sequence": one.sequence if one.sequence else 0
                }
                for one in carousel_objects
            ]
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
