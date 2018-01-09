#!encoding:utf-8
import json

from django.http import HttpResponse
from django.views.generic import View

from applications.custom_user.models import *
from lib.permissionMixin import class_view_decorator, user_login_required

"""职业信息"""


# @class_view_decorator(user_login_required)
class PostMatch(View):
    """岗位匹配度"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": list(),
        }
        try:
            custom_user_id = request.GET.get('custom_user_id', 0)  # 用户ID

            for one in xrange(3):
                one_dict = dict()
                one_dict["company"] = "凯奇谷"
                one_dict["position"] = "Python工程师"
                one_dict["schedule"] = 0.34
                one_dict["logo"] = "aaa"
                result_dict["data"].append(one_dict)
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


# @class_view_decorator(user_login_required)
class PostMatchDetail(View):
    """岗位匹配度详情"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": dict(),
        }
        try:
            custom_user_id = request.GET.get('custom_user_id', 0)  # 用户ID
            data_dict = dict()
            data_dict["treatment_range"] = "6K-8k"
            data_dict["company_info"] = "移动互联网，游戏/上市公司/北京/全职"
            claim_list = list()
            claims = ["1-3年工作经验", "本科及一上"]
            for one in claims:
                one_dict = dict()
                one_dict["checked"] = 1
                one_dict["matches"] = one
                claim_list.append(one_dict)
            data_dict["claim_list"] = claim_list
            result_dict["data"] = data_dict
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


# @class_view_decorator(user_login_required)
class OverallQualityScore(View):
    """综合素质评分"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": list(),
        }
        try:
            custom_user_id = request.GET.get('custom_user_id', 0)  # 用户ID
            result_dict["data"] = [0.7, 0.98, 0.87, 0.82, 0.64, 0.69]
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


# @class_view_decorator(user_login_required)
class FocusOnMyBusiness(View):
    """关注我的企业"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": list(),
        }
        try:
            custom_user_id = request.GET.get('custom_user_id', 0)  # 用户ID
            for one in xrange(3):
                one_dict = dict()
                one_dict["company"] = "凯奇谷"
                one_dict["logo"] = "aaa"
                one_dict["info"] = "创立于2005年9月，是中国领先的互联网安全软件与互联网服务公司，" \
                                   "曾先后获得过鼎晖创投、红杉资本、高原资本、红点投资、Matrix、IDG等" \
                                   "风险投资商总额高达数千万美元的联合投资"
                one_dict["scale"] = 7000
                result_dict["data"].append(one_dict)
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
