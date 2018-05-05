#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.slideshow.models import Carousel, WebsiteIntroduce


class SlideList(View):
    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": []}
        try:
            filter_param = dict()
            category = self.request.GET.get("category")
            if category:
                filter_param["category"] = category

                carousel_objects = Carousel.objects.filter(**filter_param).order_by("sequence")
                result_dict["data"] = [
                    {
                        "id": one.id,
                        "name": one.name,
                        "pathwel": one.pathwel.url,
                        "category_name": one.get_category_display(),
                        "category": one.category,
                        "vid": one.video.vid if one.video else "",
                        "sequence": one.sequence if one.sequence else 0,
                        "desc": one.desc
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


class WebsiteIntroduceList(View):
    """首页，智量酷是什么"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": []}
        try:
            websiteintroduces = WebsiteIntroduce.objects.filter().order_by("sequence")
            result_dict["data"] = [
                {
                    "id": one.id,
                    "title": one.title,
                    "pathwel": one.pathwel.url if one.pathwel else "",
                    "sequence": one.sequence if one.sequence else 0,
                    "desc": one.desc
                }
                for one in websiteintroduces
            ]
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
