#!encoding:utf-8
import requests
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


class WechatThumbsUptotal(View):
	"""微信推广-点赞-总数"""

	def get(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success", "total": 0}
		try:
			total = 0
			wechatbrowses = WechatBrowse.objects.filter()
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


class GetAccessToken(View):
	"""获取-AccessToken"""

	def __init__(self):
		super(GetAccessToken, self).__init__()
		self.result_dict = {"err": 0, "msg": "success", "access_token": ""}
		self.appid = 'wx7c9efe7b17c8aef2'
		self.appsecret = '4f44d0ecc91e0dd9ef955885d6cfcb4f'
		self.url = 'https://api.weixin.qq.com/cgi-bin/token'

	def get(self, request, *args, **kwargs):

		try:
			params = {
				'appid': self.appid,
				'secret': self.appsecret,
				'grant_type': 'client_credential'
			}
			res = requests.get(self.url, params=params, verify=False).json()
			"""
			{
			u'access_token': u'10_EpnmZniSpsnf1ttZbGMS14O7ZQi7kZPcY52dJLHmcAlEQ_ndwUr4J2HX8s33JqUTjBKV-EDKeImlvYyXqGa9o0_expR7LSgzE5wLFCwzDDb_lHywV396HXhCug8Z4oTsb2OzzRFmuae4UvcENOVdADAXYF', 
			u'expires_in': 7200
			}
			"""
			self.result_dict["access_token"] = res.get("access_token", "")
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))
