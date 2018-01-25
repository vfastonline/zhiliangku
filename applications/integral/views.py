#!encoding:utf-8
import json
import logging
import traceback

from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from applications.integral.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int


@class_view_decorator(user_login_required)
class Redeem(View):
    """积分兑换--页面"""

    def get(self, request, *args, **kwargs):
        template_name = "integral/redeem/index.html"
        return render(request, template_name, {})


class GetAllGoods(View):
    """所有商品"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": []}
        try:
            gtype = self.request.GET.get("gtype", "0")  # 商品类型
            if gtype == "0":
                goods = Goods.objects.all()
            else:
                goods = Goods.objects.filter(gtype=gtype)

            goods_list = list()
            for one in goods:
                one_dict = dict()
                one_dict["id"] = one.id
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


class GoodsDetail(View):
    """商品详情"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": {}}
        try:
            goods_id = str_to_int(self.request.GET.get("goods_id", 0))  # 商品ID
            goods = Goods.objects.filter(id=goods_id)
            goods_dict = {}
            if goods.exists():
                one = goods.first()
                goods_dict["id"] = one.id
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


@class_view_decorator(user_login_required)
class GetExchangeRecords(View):
    """兑换记录"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": list()}
        try:
            custom_user_id = str_to_int(self.request.GET.get('custom_user_id', 0))  # 用户ID
            exchangerecords = ExchangeRecords.objects.filter(custom_user_id__id=custom_user_id)
            exchangerecords_list = list()
            if exchangerecords.exists():
                for one in exchangerecords:
                    one_dict = dict()
                    one_dict["id"] = one.id
                    one_dict["goods_id"] = one.goods.id
                    one_dict["name"] = one.goods.name
                    one_dict["gtype_name"] = one.goods.get_gtype_display()
                    one_dict["integral"] = one.goods.integral
                    one_dict["stock"] = one.goods.stock
                    one_dict["residue_stock"] = one.goods.residue_stock
                    exchangerecords_list.append(one_dict)
            result_dict["data"] = exchangerecords_list
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class ExchangeGoods(View):
    """兑换商品"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success"}
        try:
            param_dict = json.loads(request.body)
            custom_user_id = str_to_int(param_dict.get('custom_user_id', 0))  # 用户ID
            goods_id = str_to_int(param_dict.get("goods_id", 0))  # 商品ID

            customuser = CustomUser.objects.filter(id=custom_user_id)
            goods = Goods.objects.filter(id=goods_id)
            if customuser.exists() and goods.exists():
                customuser_obj = customuser.first()
                goods_obj = goods.first()
                goods_integral = goods_obj.integral  # 商品积分
                customuser_integral = customuser_obj.integral  # 用户积分
                if goods_integral > customuser_integral:
                    result_dict["err"] = 1
                    result_dict["msg"] = "您的积分不足，抓紧赚取积分！"
                elif goods_obj.residue_stock < 1:
                    result_dict["err"] = 1
                    result_dict["msg"] = "商品库存告急，请稍后兑换。"
                else:
                    # 增加兑换记录
                    obj = ExchangeRecords.objects.create(custom_user=customuser.first(), goods=goods.first())
                    if not obj:
                        result_dict["err"] = 1
                        result_dict["msg"] = "增加兑换记录失败，兑换失败"
                    else:
                        # 扣除用户积分，计算剩余库存
                        customuser.update(integral=F('integral') - goods_integral)
                        goods.update(residue_stock=F('residue_stock') - 1)
            else:
                result_dict["err"] = 1
                result_dict["msg"] = "用户或商品不存在"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
