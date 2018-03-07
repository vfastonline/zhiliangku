#!encoding:utf-8
import json

from django.http import HttpResponse
from django.views.generic import View

from applications.custom_user.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int

"""职业信息"""


@class_view_decorator(user_login_required)
class PostMatch(View):
    """岗位匹配度"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": list(),
        }
        try:
            custom_user_id = str_to_int(request.GET.get('custom_user_id', 0))  # 用户ID

            one_dict = {
                "company": "凯奇谷",
                "position": "Python工程师",
                "post_id": "1",
                "schedule": 0.34,
                "logo": "/media/course/20171204/20171204160021_91.png",
            }
            result_dict["data"].append(one_dict)

            one_dict = {
                "company": "百度",
                "position": "web前端工程师",
                "post_id": "2",
                "schedule": 0.1,
                "logo": "/media/course/20180307/20180307141417_82.jpg",
            }
            result_dict["data"].append(one_dict)

            one_dict = {
                "company": "阿里巴巴",
                "position": "资深Java工程师",
                "post_id": "3",
                "schedule": 0.6,
                "logo": "/media/course/20171204/20180307140057_462.jpg",
            }
            result_dict["data"].append(one_dict)
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class PostMatchDetail(View):
    """岗位匹配度详情"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": dict(),
        }
        try:
            custom_user_id = str_to_int(request.GET.get('custom_user_id', 0))  # 用户ID
            post_id = str_to_int(request.GET.get('post_id', 0))  # 岗位ID
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


@class_view_decorator(user_login_required)
class OverallQualityScore(View):
    """综合素质评分"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": list(),
        }
        try:
            custom_user_id = str_to_int(request.GET.get('custom_user_id', 0))  # 用户ID
            result_dict["data"] = [0.7, 0.98, 0.87, 0.82, 0.64, 0.69]
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class FocusOnMyBusiness(View):
    """关注我的企业"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": list(),
        }
        try:
            custom_user_id = str_to_int(request.GET.get('custom_user_id', 0))  # 用户ID
            one_dict = dict()
            one_dict["company"] = "凯奇谷"
            one_dict["logo"] = "/media/interview_questions/20171227/20171227103821_890.png"
            one_dict["info"] = "创立于2005年9月，是中国领先的互联网安全软件与互联网服务公司，" \
                               "曾先后获得过鼎晖创投、红杉资本、高原资本、红点投资、Matrix、IDG等" \
                               "风险投资商总额高达数千万美元的联合投资"
            one_dict["scale"] = 7000
            result_dict["data"].append(one_dict)

            one_dict["company"] = "百度"
            one_dict["logo"] = "/media/interview_questions/20171227/20171227103713_417.png"
            one_dict["info"] = "百度（纳斯达克：BIDU），全球最大的中文搜索引擎、最大的中文网站。" \
                               "1999年底,身在美国硅谷的李彦宏看到了中国互联网及中文搜索引擎服务的巨大发展潜力，抱着技术改变世界的梦想，" \
                               "他毅然辞掉硅谷的高薪工作，携搜索引擎专利技术，于 2000年1月1日在中关村创建了百度公司。"
            one_dict["scale"] = 8000
            result_dict["data"].append(one_dict)

            one_dict["company"] = "阿里巴巴"
            one_dict["logo"] = "/media/interview_questions/20171227/20171227103541_136.png"
            one_dict["info"] = "阿里巴巴网络技术有限公司（简称：阿里巴巴集团）是以曾担任英语教师的马云为首的18人于1999年在浙江杭州创立。"
            one_dict["scale"] = 7500
            result_dict["data"].append(one_dict)
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
