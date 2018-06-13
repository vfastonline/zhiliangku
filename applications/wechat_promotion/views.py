#!encoding:utf-8

from django.db.models import F
from django.shortcuts import render
from django.views.generic import View

from applications.wechat_promotion.models import *
from lib.util import *

RK_BROWSE_COUNTER = 'browse_pending_counter_changes'  # 浏览
RK_THUMBS_UP_COUNTER = 'thumbs_up_pending_counter_changes'  # 点赞


class WechatPromotionJl(View):
	"""微信推广-页面-王金龙信息"""

	def get(self, request, *args, **kwargs):
		template_name = "wechat/promotion/jl/index.html"
		return render(request, template_name, {})


class WechatPromotion(View):
	"""微信推广-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "wechat/promotion/index.html"
		return render(request, template_name, {})


class WechatPromotionInfo(View):
	"""学员信息"""

	def get(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success", "data": dict()}
		try:
			name = request.GET.get('name', "")  # 学员名字拼音
			wechatbrowses = WechatBrowse.objects.filter(pinyin=name)
			detail = dict()
			if wechatbrowses.exists():
				wechatbrowses.update(page_views=F('page_views') + 1)
				wechatbrowse = wechatbrowses.first()
				detail["name"] = wechatbrowse.name
				detail["pinyin"] = wechatbrowse.pinyin
				detail["avatar"] = wechatbrowse.avatar.url if wechatbrowse.avatar else ""
				detail["photo2"] = wechatbrowse.photo2.url if wechatbrowse.photo2 else ""
				detail["photo3"] = wechatbrowse.photo3.url if wechatbrowse.photo3 else ""
				detail["photo4"] = wechatbrowse.photo4.url if wechatbrowse.photo4 else ""
				detail["photo5"] = wechatbrowse.photo5.url if wechatbrowse.photo5 else ""
				remark_names = wechatbrowse.remark.strip().split(",")
				wechatremarks = WechatRemark.objects.filter(name__in=remark_names)
				for one_remark in wechatremarks:
					detail[one_remark.name[0]] = {"remark": one_remark.remark, "english": one_remark.english}

			result_dict["data"] = detail
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class GetBackgrounds(View):
	"""获取所有背景图片"""

	def get(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success", "data": list()}
		try:
			wechatbackgrounds = WechatBackground.objects.all()
			for one in wechatbackgrounds:
				result_dict["data"].append({"image": one.image.url if one.image else ""})
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class WechatThumbsUptotal(View):
	"""微信推广-点赞-总数"""

	def get(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success", "total": 0}
		try:
			total = 0
			name = request.GET.get('name', "")  # 学员名字拼音
			wechatbrowses = WechatBrowse.objects.filter(pinyin=name)
			if wechatbrowses.exists():
				total = wechatbrowses.first().thumbs_up
			result_dict["total"] = total
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class WechatThumbsUp(View):
	"""微信推广-点赞"""

	def get(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success"}
		try:
			name = request.GET.get('name', "")
			WechatBrowse.objects.filter(pinyin=name).update(thumbs_up=F('thumbs_up') + 1)
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class WechatShare(View):
	"""微信推广-分享"""

	def get(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success"}
		try:
			name = request.GET.get('name', "")
			WechatBrowse.objects.filter(pinyin=name).update(share=F('share') + 1)
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
