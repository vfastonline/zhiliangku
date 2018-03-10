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
                "company": "今日头条",
                "position": "Python 研发工程师",
                "post_id": "1",
                "schedule": 0.34,
                "logo": "/media/toutiao.jpg",
            }
            result_dict["data"].append(one_dict)

            one_dict = {
                "company": "京东商城",
                "position": "web 前端开发工程师",
                "post_id": "2",
                "schedule": 0.1,
                "logo": "/media/jingdong.jpg",
            }
            result_dict["data"].append(one_dict)

            one_dict = {
                "company": "链家",
                "position": "Java 开发工程师",
                "post_id": "3",
                "schedule": 0.6,
                "logo": "/media/lianjia.png",
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
            result_dict = {
                "1": {
                    "treatment_range": "25K-45k",
                    "company_info": "六险一金，高薪期权，弹性工作，免费三餐，租房补贴，带薪休假，扁平管理，职业大牛，晋升空间",
                    "claim_list": [
                        {"checked": 1, "matches": "参与系统架构设计、优化，提升系统性能和开发效率，保证高并发高可靠"},
                        {"checked": 1, "matches": "通过不断的技术研究和创新，推动业务的快速发展和高效迭代。 "},
                    ]
                },
                "2": {
                    "treatment_range": "6K-8k",
                    "company_info": "移动互联网，游戏/上市公司/北京/全职",
                    "claim_list": [
                        {"checked": 1, "matches": "1-3年工作经验2"},
                    ]
                },
                "3": {
                    "treatment_range": "6K-8k",
                    "company_info": "移动互联网，游戏/上市公司/北京/全职",
                    "claim_list": [
                        {"checked": 1, "matches": "1-3年工作经验3"},
                    ]
                },
            }
            result_dict["data"] = result_dict[str(post_id)]
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
            one_dict["company"] = "链家"
            one_dict["logo"] = "/media/lianjia.png"
            one_dict["info"] = "链家是集房源信息搜索、产品研发、大数据处理、服务标准建立为一体的以数据驱动的全价值链房产服务平台。" \
                               "提供二手房、新房、租房、旅居房产、海外房产等房产交易服务，并拥有业内独有的房屋数据、人群数据、交易数据，" \
                               "以数据技术驱动服务品质及行业效率的提升。" \
                               "这里拥有600+产品技术团队规模，绝大多数都来自百度、阿里、腾讯、新浪微博、网易、美团、京东、去哪儿网、滴滴、小米等一线互联网公司。" \
                               "这里拥有第一届百度百万美金最高奖核心团队，还有”鸟哥“、”教主“、“囧哥”、“肖师傅”、“阿缪”等技术大牛带你玩转各个专业领域，更有一系列学习课程及技术站专业培养课，等你来挑战。" \
                               "未来五年，链家会以互联网技术和数据化产品，进行线上线下的打通，重构和优化服务流程，制定房产经纪服务标准，为用户提供更省心便捷的服务，实现卓越中国人的居住体验的企业愿景。"
            one_dict["scale"] = 7000
            result_dict["data"].append(one_dict)

            one_dict = dict()
            one_dict["company"] = "京东商城"
            one_dict["logo"] = "/media/jingdong.jog"
            one_dict["info"] = "京东商城目前已成长为中国最大的自营式电商企业，2015年第三季度在中国自营式B2C电商市场的占有率为56.9%*。" \
                               "京东商城致力于打造一站式综合购物平台，服务中国亿万家庭，3C事业部、家电事业部、消费品事业部、服饰家居事业部、生鲜事业部和新通路事业部六大部门领航发力，覆盖用户多元需求。" \
                               "同时，京东商城还为第三方卖家提供在线销售平台和物流等一系列增值服务。" \
                               " 京东拥有中国电商领域规模最大的物流基础设施；通过完善布局，京东将成为全球唯一拥有中小件、大件、冷藏冷冻仓配一体化物流设施的电商企业。" \
                               "截至2016年3月31日，京东在全国范围内拥有7大物流中心，运营了209个大型仓库，拥有5987个配送站和自提点，覆盖全国范围内的2493个区县，仓储设施占地面积约430万平方米。"
            one_dict["scale"] = 2000
            result_dict["data"].append(one_dict)

            one_dict = dict()
            one_dict["company"] = "今日头条"
            one_dict["logo"] = "/media/toutiao.jpg"
            one_dict["info"] = "北京字节跳动科技有限公司成立于2012年3月，是一家技术驱动的移动互联网公司，公司致力于采用先进的推荐引擎技术，" \
                               "提供基于移动设备的信息分发解决方案。公司的主要产品“今日头条”资讯客户端，是一款基于数据挖掘技术的个性化推荐引擎产品，" \
                               "致力于帮助用户在移动互联网上方便快捷地获取最有价值的信息，它会根据用户的兴趣为其推荐内容，对传统信息的分发方式产生了巨大颠覆。" \
                               "“今日头条”的团队是一支拥有丰富创业与成熟公司经验的技术驱动型团队，聚集了来自国内外顶级高校和一流公司的顶尖人才，其推荐引擎、机器学习、数据挖掘等技术在全球视野内拥有竞争优势。" \
                               " 自2012年8月推出后，“今日头条”迅速获得市场认可，长期占据苹果应用商店新闻类榜首。" \
                               "随着大众用户的阅读行为广泛向移动设备迁移，字节跳动获得了高速发展，在行业内已建立起了极高的品牌知名度与影响力。" \
                               "在夯实国内市场的同时，字节跳动也在积极进行国际化部署，目标在全球范围内提供先进的移动互联网信息分发服务，成为全球领先的移动互联网公司。"
            one_dict["scale"] = 7500
            result_dict["data"].append(one_dict)
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
