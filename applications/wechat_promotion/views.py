#!encoding:utf-8
from django.db.models import *
from django.db.models import F
from django.shortcuts import render
from django.views.generic import View

from applications.wechat_promotion.models import WechatBrowse
from lib.util import *


class WechatPromotion(View):
	"""微信推广-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "wechat/promotion/index.html"
		try:
			wechatbrowses = WechatBrowse.objects.filter()
			if wechatbrowses.exists():
				wechatbrowses.update(page_views=F('page_views') + 1)
			else:
				WechatBrowse.objects.get_or_create(page_views=1)
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		return render(request, template_name, {})


class WechatThumbsUp(View):
	"""微信推广-点赞"""

	def get(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success"}
		try:
			wechatbrowses = WechatBrowse.objects.filter()
			if wechatbrowses.exists():
				wechatbrowses.update(thumbs_up=F('thumbs_up') + 1)
			else:
				WechatBrowse.objects.get_or_create(page_views=1, thumbs_up=1)
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
