#!encoding:utf-8
import random
import string

import requests
from django.views.generic import View

from lib.base_redis import redis_db
from lib.util import *


class GetSignature(View):
	"""获取-Signature"""

	def __init__(self):
		super(GetSignature, self).__init__()
		self.appid = 'wx96fdf187f5c8f9f2'
		self.appsecret = 'a554a61688d97543a146c62d1fcd85b9'
		self.get_access_token_url = 'https://api.weixin.qq.com/cgi-bin/token'
		self.get_ticket_url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket"
		self.result_dict = {"err": 0, "msg": "success", "data": {}}

	def get_access_token(self):
		access_token = ""
		try:
			access_token = redis_db.get("access_token")
		except:
			traceback.print_exc()
		if not access_token:
			params = {
				'appid': self.appid,
				'secret': self.appsecret,
				'grant_type': 'client_credential'
			}
			res = requests.get(self.get_access_token_url, params=params, verify=False).json()
			"""
			{
			u'access_token': u'10_EpnmZniSpsnf1ttZbGMS14O7ZQi7kZPcY52dJLHmcAlEQ_ndwUr4J2HX8s33JqUTjBKV-EDKeImlvYyXqGa9o0_expR7LSgzE5wLFCwzDDb_lHywV396HXhCug8Z4oTsb2OzzRFmuae4UvcENOVdADAXYF', 
			u'expires_in': 7200
			}
			"""
			access_token = res.get("access_token", "")
			expires_in = res.get("expires_in", 1)
			redis_db.setex("access_token", access_token, expires_in)
		return access_token

	def get_ticket(self, access_token):
		ticket = ""
		try:
			ticket = redis_db.get("ticket")
		except:
			traceback.print_exc()
		if not ticket:
			params = {
				'access_token': access_token,
				'type': "jsapi",
			}
			res = requests.get(self.get_ticket_url, params=params, verify=False).json()
			"""
			{
			u'ticket': u'HoagFKDcsGMVCIY2vOjf9g7NsT3wK7wutnW3fBQn4QzUVxV-NwuTVdgkIj_6KLCdrM8PstTUbyCCD3AbHq1Mkw', 
			u'expires_in': 7200, 
			u'errcode': 0, 
			u'errmsg': u'ok'
			}
			"""
			ticket = res.get("ticket", "")
			expires_in = res.get("expires_in", 1)
			redis_db.setex("ticket", ticket, expires_in)
		return ticket

	def get(self, request, *args, **kwargs):

		try:
			urls = self.request.GET.get("urls", "")  # 要分享的url

			# 获取access_token
			access_token = self.get_access_token()

			# 获取ticket
			ticket = self.get_ticket(access_token)

			sign = Sign(ticket, urls)
			self.result_dict["data"] = sign.sign()
			self.result_dict["data"]["appId"] = self.appid
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


class Sign:
	def __init__(self, jsapi_ticket, url):
		self.ret = {
			'nonceStr': self.__create_nonce_str(),
			'jsapi_ticket': jsapi_ticket,
			'timestamp': self.__create_timestamp(),
			'url': url,
		}

	@staticmethod
	def __create_nonce_str():
		return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

	@staticmethod
	def __create_timestamp():
		return int(time.time())

	def sign(self):
		string = '&'.join(['%s=%s' % (key.lower(), self.ret[key]) for key in sorted(self.ret)])
		print string
		self.ret['signature'] = hashlib.sha1(string).hexdigest()
		print self.ret['signature']
		return self.ret
