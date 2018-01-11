#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from applications.integral.models import *

from lib.permissionMixin import class_view_decorator, user_login_required


@class_view_decorator(user_login_required)
class Redeem(View):
    """积分兑换--页面"""

    def get(self, request, *args, **kwargs):
        template_name = "integral/redeem/index.html"
        return render(request, template_name, {})


# @class_view_decorator(user_login_required)
class GetAllGoods(View):
    """所有商品"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": []}
        try:
            goods = Goods.objects.all()
            goods_list = list()
            for one in goods:
                one_dict = dict()
                one_dict["id"] = one.id
                one_dict["name"] = one.name
                one_dict["name"] = one.name
                one_dict["gtype"] = one.gtype
                one_dict["gtype_name"] = one.get_gtype_display()
                one_dict["style"] = one.style
                one_dict["image"] = one.image.url
                one_dict["integral"] = one.integral
                one_dict["stock"] = one.stock
                one_dict["residue_stock"] = one.residue_stock
                one_dict["detail"] = one.detail
                goods_list.append(one_dict)

            result_dict["data"] = goods_list
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))

# @class_view_decorator(user_login_required)
class GoodsDetail(View):
    """商品详情"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": {}}
        try:
            goods_id = self.request.GET.get("goods_id", 0)  # 商品ID
            goods = Goods.objects.filter(id=goods_id)
            goods_dict = {}
            if goods.exists():
                one = goods.first()
                goods_dict["id"] = one.id
                goods_dict["name"] = one.name
                goods_dict["name"] = one.name
                goods_dict["gtype"] = one.gtype
                goods_dict["gtype_name"] = one.get_gtype_display()
                goods_dict["style"] = one.style
                goods_dict["image"] = one.image.url
                goods_dict["integral"] = one.integral
                goods_dict["stock"] = one.stock
                goods_dict["residue_stock"] = one.residue_stock
                goods_dict["detail"] = one.detail

            result_dict["data"] = goods_dict
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))