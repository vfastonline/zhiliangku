#!encoding:utf-8
import re
import urllib2
import urlparse

import requests
from django.http import Http404
from django.shortcuts import render
from django.views.generic import View

from applications.custom_user.models import *
from applications.tracks_learning.models import *
from lib.encrypt import PyCrypt
from lib.util import *
from zhiliangku.settings import MEDIA_ROOT

CryptKey = "25668fbe1a5601eb"

emoji_pattern = re.compile(
	u'(\ud83d[\uD800-\uDBFF])|'
	u'(\ud83d[\uDC00-\uDFFF])|'
	u"(\ud83d[\ude00-\ude4f])|"  # emoticons
	u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
	u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
	u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
	u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
	"+", flags=re.UNICODE)


def remove_emoji(text):
	return emoji_pattern.sub(r'', text)


class IsCellphone:
	"""http://www.linuxeye.com/program/1760.html"""

	def __init__(self):
		self.p = re.compile(r'^1\d{10}$')

	def iscellphone(self, cellphone_number):
		try:
			res = self.p.match(cellphone_number)
			if res:
				return True
			else:
				return False
		except:
			traceback.print_exc()
			return False


class IsMail:
	def __init__(self):
		self.p = re.compile(r'[^\._][\w\._-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$')

	def ismail(self, mail_str):
		try:
			res = self.p.match(mail_str)
			if res:
				return True
			else:
				return False
		except:
			traceback.print_exc()
			return False


class CustomUserLogin(View):
	"""用户登录"""

	def post(self, request, *args, **kwargs):
		result_dict = {
			"msg": "",
			"err": 1,
			"data": {}
		}
		token = ""
		try:
			param_dict = json.loads(request.body)
			username = param_dict.get("username")
			password = param_dict.get("password")

			is_mail = IsMail().ismail(username)
			is_cellphone = IsCellphone().iscellphone(username)

			# 权限类型判断
			identity_type = ""
			if is_mail:
				identity_type = "email"
			if is_cellphone:
				identity_type = "phone"

			# 校验是否有权限信息
			custom_user_auths = CustomUserAuths.objects.filter(identity_type=identity_type, identifier=username)
			if not custom_user_auths.exists():
				result_dict["msg"] = "您还没有账号，请先注册"
				result_dict["err"] = 2
			else:
				custom_user_auth = custom_user_auths[0]
				if custom_user_auth.status:
					pycrypt_obj = PyCrypt(CryptKey)
					crypt_password = pycrypt_obj.encrypt(password)
					custom_user_pwd = custom_user_auth.credential  # 密码凭证
					custom_user_id = custom_user_auth.custom_user_id.id  # 用户ID
					custom_user_role = custom_user_auth.custom_user_id.role  # 用户角色，0：学生；1：老师
					if custom_user_pwd != crypt_password:
						result_dict["msg"] = "账号或密码错误"
						result_dict["err"] = 3
					else:
						token = get_validate(username, custom_user_id, custom_user_role, CryptKey)
						result_dict["msg"] = "success"
						result_dict["err"] = 0
						# result_dict["data"]["token"] = token
						result_dict["data"]["user"] = {
							# "uid": custom_user_auth.custom_user_id.id,
							"nickname": custom_user_auth.custom_user_id.nickname,
							"role": custom_user_auth.custom_user_id.role,
							"avatar": custom_user_auth.custom_user_id.avatar.url if custom_user_auth.custom_user_id.avatar else "",
							"position": custom_user_auth.custom_user_id.position if custom_user_auth.custom_user_id.position else "",
						}

				# user_dict = {
				#     "nickname": custom_user_auth.custom_user_id.nickname,
				#     "uid": custom_user_auth.custom_user_id.id,
				#     "avatar": custom_user_auth.custom_user_id.avatar.url if custom_user_auth.custom_user_id.avatar else ""
				# }
				# request.session['token'] = token
				# request.session['user'] = user_dict
				# request.session['login'] = True
				else:
					result_dict["msg"] = "账号未激活"
					result_dict["err"] = 6
		except:
			result_dict["msg"] = traceback.format_exc()
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			res = HttpResponse(json.dumps(result_dict, ensure_ascii=False))
			res.set_cookie("token", token)
			return res


class WeiXinLogin(View):
	"""微信扫码授权第三方登录

	"""
	appid = 'wx7c9efe7b17c8aef2'
	appsecret = '4f44d0ecc91e0dd9ef955885d6cfcb4f'
	code = ''
	state = ''

	def get(self, request, *args, **kwargs):
		# result_dict = {
		#     "msg": "微信登录失败",
		#     "err": 1,
		#     "data": {}
		# }

		token = ""
		try:
			# https://open.weixin.qq.com/connect/qrconnect?appid=wx7c9efe7b17c8aef2&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2flogin&response_type=code&scope=snsapi_login&state=L2FkbWlu#wechat_redirect
			self.code = self.request.GET.get("code")
			self.state = self.request.GET.get("state")
			self.user_id = self.request.GET.get("u")  # 绑定账号用

			# 解base64,重定向url
			self.state = base64.b64decode(self.state)

			# 2.通过code换取网页授权access_token
			try:
				url = u'https://api.weixin.qq.com/sns/oauth2/access_token'
				params = {
					'appid': self.appid,
					'secret': self.appsecret,
					'code': self.code,
					'grant_type': 'authorization_code'
				}
				res = requests.get(url, params=params, verify=False).json()
				"""res
				{
					u'openid': u'oz4KJ1j8fwabm3IA1CwFtpE4fJ_M',
					u'access_token': u'4_RkYEXcSJBvIyYaRbrUHIQFk3XfQ3Qv0yYpJpDudVrReCaqEKX9X0AmI1K5kvC2WHRGz3bBerbQwfhtbAvECaGA',
					u'unionid': u'oQB0n1D3swsSJLAWnb9UMHQ4F4Jk',
					u'expires_in': 7200,
					u'scope': u'snsapi_login',
					u'refresh_token': u'4_DPwMWtOnKvESpKGhXLLP2e2DU0qHH276HSscaOH610Fr6hH4SfaCweeV68OoJEUEYMpMWICTTFOXVg48UigYpA'
				}
				"""
				access_token = res["access_token"]
			except:
				traceback.print_exc()
				logging.getLogger().info("获取access_token参数错误：\n%s" % traceback.format_exc())
				raise Http404()

			# 3.如果access_token超时，那就刷新
			# 注意,这里我没有写这个刷新功能,不影响使用,如果想写的话,可以自己去看文档

			# 4.拉取用户信息
			try:
				user_info_url = u'https://api.weixin.qq.com/sns/userinfo'
				params = {
					'access_token': res["access_token"],
					'openid': res["openid"],
				}
				res = requests.get(user_info_url, params=params, verify=False).json()
				"""
				{
					u'province': u'Beijing',
					u'openid': u'oz4KJ1j8fwabm3IA1CwFtpE4fJ_M',
					u'headimgurl': u'http: //wx.qlogo.cn/mmopen/vi_32/DYAIOgq83eqic03RMYMUSxqh13fWTTuneZibUDTuG6mruQxwkQqChiajlZF5FFq8Rk7pR6Ll2v3tv8uw7dMzA5Jnw/0',
					u'language': u'zh_CN',
					u'city': u'Haidian',
					u'country': u'CN',
					u'sex': 1,
					u'unionid': u'oQB0n1D3swsSJLAWnb9UMHQ4F4Jk',
					u'privilege': [
						
					],
					u'nickname': u'Maybe'
				}
				注意,这里有个坑,res['nickname']表面上是unicode编码,
				但是里面的串却是str的编码,举个例子,res['nickname']的返回值可能是这种形式
				u'\xe9\x97\xab\xe5\xb0\x8f\xe8\x83\x96',直接存到数据库会是乱码.必须要转成
				unicode的编码,需要使用
				res['nickname'] = res['nickname'].encode('iso8859-1').decode('utf-8')
				这种形式来转换.
				你也可以写个循环来转化.
				for value in res.values():
					value = value.encode('iso8859-1').decode('utf-8')
				"""
			except:
				traceback.print_exc()
				logging.getLogger().info("拉取用户信息错误：\n%s" % traceback.format_exc())

			nickname = remove_emoji(res['nickname'].encode('iso8859-1').decode('utf-8'))
			headimgurl = res['headimgurl'].encode('iso8859-1').decode('utf-8')
			openid = res['openid'].encode('iso8859-1').decode('utf-8')

			# 校验是否有权限信息
			custom_user_auths = CustomUserAuths.objects.filter(identity_type="weixin", identifier=openid)

			# 已经注册，直接登录
			if custom_user_auths.exists():
				custom_user_auth_obj = custom_user_auths.first()
				token = get_validate(openid, custom_user_auth_obj.custom_user_id.id, 0, CryptKey)
				# result_dict["err"] = 0
				# result_dict["msg"] = "success"
				# result_dict["data"]["token"] = token
				# result_dict["data"]["user"] = {
				#     "uid": custom_user_auth_obj.custom_user_id.id,
				#     "nickname": custom_user_auth_obj.custom_user_id.nickname,
				#     "role": custom_user_auth_obj.custom_user_id.role,
				#     "avatar": custom_user_auth_obj.custom_user_id.avatar.url if custom_user_auth_obj.custom_user_id.avatar else "",
				#     "position": custom_user_auth_obj.custom_user_id.position,
				# }

				user_info_str = "uid={uid}&nickname={nickname}&role={role}&avatar={avatar}&position={position}".format(
					uid=custom_user_auth_obj.custom_user_id.id,
					nickname=custom_user_auth_obj.custom_user_id.nickname,
					role=custom_user_auth_obj.custom_user_id.get_role_display(),
					avatar=custom_user_auth_obj.custom_user_id.avatar.url if custom_user_auth_obj.custom_user_id.avatar else "",
					position=custom_user_auth_obj.custom_user_id.position if custom_user_auth_obj.custom_user_id.position else "",
				)
				user_info = "user_info=" + base64.b64encode(user_info_str)
				if "?" in self.state:
					self.state += "&" + user_info
				else:
					self.state += "?" + user_info

			# user_dict = {
			#     "nickname": custom_user_auth_obj.custom_user_id.nickname,
			#     "uid": custom_user_auth_obj.custom_user_id.id,
			#     "avatar": custom_user_auth_obj.custom_user_id.avatar.name
			# }
			# request.session['token'] = token
			# request.session['user'] = user_dict
			# request.session['login'] = True
			else:
				if self.user_id:  # 绑定账号
					user_auth_dict = {
						"custom_user_id": CustomUser.objects.get(id=self.user_id),
						"identity_type": "weixin",  # 登录类型
						"identifier": openid,  # 唯一标识
						"credential": access_token,  # 密码凭证
					}
					create_auth = CustomUserAuths.objects.create(**user_auth_dict)
				else:
					create_user = CustomUser.objects.create(nickname=nickname, role=0)
					avatar_filename = "_".join([time.strftime('%Y%m%d%H%M%S'), "weixin.jpg"])
					avatar_path = os.path.join("custom_user_avatar", str(create_user.id), avatar_filename)
					create_user.avatar = avatar_path
					create_user.save()

					# 下载头像
					avatar_abs_path = os.path.join(MEDIA_ROOT, "custom_user_avatar", str(create_user.id))
					if not os.path.exists(avatar_abs_path):
						os.makedirs(avatar_abs_path)

					# resp = urllib2.urlopen(headimgurl)
					# real_url_str = str(resp.geturl())
					# req = urllib2.Request(real_url_str)
					resp = urllib2.urlopen(headimgurl)
					resp_html = resp.read()
					binfile = open(os.path.join(avatar_abs_path, avatar_filename), "wb")
					binfile.write(resp_html)
					binfile.close()

					if create_user:
						user_auth_dict = {
							"custom_user_id": create_user,
							"identity_type": "weixin",  # 登录类型
							"identifier": openid,  # 唯一标识
							"credential": access_token,  # 密码凭证
						}
						create_auth = CustomUserAuths.objects.create(**user_auth_dict)

						if create_auth:
							# 生成token
							token = get_validate(openid, create_user.id, 0, CryptKey)
							# result_dict["err"] = 0
							# result_dict["msg"] = "success"
							# result_dict["data"]["token"] = token
							# result_dict["data"]["user"] = {
							#     "uid": create_user.id,
							#     "nickname": create_user.nickname,
							#     "role": create_user.role,
							#     "avatar": create_user.avatar.url if create_user.avatar else "",
							#     "position": create_user.position,
							# }
							user_info_str = "uid={uid}&nickname={nickname}&role={role}&avatar={avatar}&position={position}".format(
								uid=create_user.id,
								nickname=create_user.nickname,
								role=create_user.get_role_display(),
								avatar=create_user.avatar.url if create_user.avatar else "",
								position=create_user.position if create_user.position else "",
							)
							user_info = "user_info=" + base64.b64encode(user_info_str)
							if "?" in self.state:
								self.state += "&" + user_info
							else:
								self.state += "?" + user_info

						# user_dict = {
						#     "nickname": create_user.nickname,
						#     "uid": create_user.id,
						#     "avatar": create_user.avatar.name
						# }
						# request.session['token'] = token
						# request.session['user'] = user_dict
						# request.session['login'] = True

						else:
							create_user.delete()
		# result_dict["msg"] = "用户权限添加失败"
		except:
			# result_dict["msg"] = traceback.format_exc()
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			res = HttpResponseRedirect(self.state)
			if not self.user_id:
				res.set_cookie("token", token)
			return res


# return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class QQLogin(View):
	appid = '101447834'
	appkey = '7c57f3120ce94f59dc217f25333b086a'
	code = ''
	state = ''

	def get(self, request, *args, **kwargs):
		# result_dict = {
		#     "msg": "QQ登录失败",
		#     "err": 1,
		#     "data": {}
		# }

		token = ""
		try:
			# 第一步获取code跟state
			# https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&client_id=101447834&redirect_uri=http%3A%2F%2Fwww.zhiliangku.com%2Fcustomuser%2Fqq%2Flogin&state=L2FkbWlu&scope=get_user_info,get_info
			self.code = self.request.GET.get("code")
			self.state = self.request.GET.get("state")
			self.user_id = self.request.GET.get("u")  # 绑定账号用

			# 解base64,重定向url
			self.state = base64.b64decode(self.state)

			# 2.通过code换取网页授权access_token
			access_token = ""
			try:
				url = 'https://graph.qq.com/oauth2.0/token'
				params = {
					'grant_type': 'authorization_code',
					'client_id': self.appid,
					'client_secret': self.appkey,
					'code': self.code,
					'redirect_uri': "http://www.zhiliangku.com/customuser/qq/login",

				}
				res = requests.get(url, params=params, verify=False).text
				result = urlparse.urlparse(res)
				param_dict = urlparse.parse_qs(result.path, True)
				access_tokens = param_dict.get("access_token", [])
				expires_ins = param_dict.get("expires_in", [])
				refresh_tokens = param_dict.get("refresh_token", [])
				if access_tokens:
					access_token = access_tokens[0]
			except:
				traceback.print_exc()
				logging.getLogger().info("获取access_token参数错误：\n%s" % traceback.format_exc())
				raise Http404()

			# 获取用户OpenID
			openid = ""
			try:
				me_url = 'https://graph.qq.com/oauth2.0/me'
				params = {
					'access_token': access_token,
				}
				res = requests.get(me_url, params=params, verify=False).text
				v_str = str(res)[9:-3]
				v_json = json.loads(v_str)
				openid = v_json.get('openid')
			except:
				traceback.print_exc()
				logging.getLogger().info("拉取用户OpenID错误：\n%s" % traceback.format_exc())

			# 获取用户信息
			try:
				get_user_info_url = 'https://graph.qq.com/user/get_user_info'
				params = {
					'access_token': access_token,
					'oauth_consumer_key': self.appid,
					'openid': openid,
				}
				res = requests.get(get_user_info_url, params=params, verify=False).json()
				"""
				{
					"ret":0,
					"msg":"",
					"nickname":"Peter",
					"figureurl":"http://qzapp.qlogo.cn/qzapp/111111/942FEA70050EEAFBD4DCE2C1FC775E56/30",
					"figureurl_1":"http://qzapp.qlogo.cn/qzapp/111111/942FEA70050EEAFBD4DCE2C1FC775E56/50",
					"figureurl_2":"http://qzapp.qlogo.cn/qzapp/111111/942FEA70050EEAFBD4DCE2C1FC775E56/100",
					"figureurl_qq_1":"http://q.qlogo.cn/qqapp/100312990/DE1931D5330620DBD07FB4A5422917B6/40",
					"figureurl_qq_2":"http://q.qlogo.cn/qqapp/100312990/DE1931D5330620DBD07FB4A5422917B6/100",
					"gender":"男",
					"is_yellow_vip":"1",
					"vip":"1",
					"yellow_vip_level":"7",
					"level":"7",
					"is_yellow_year_vip":"1"
					} 
				"""
			except:
				traceback.print_exc()
				logging.getLogger().info("拉取用户信息错误：\n%s" % traceback.format_exc())

			nickname = remove_emoji(res['nickname'].encode('iso8859-1').decode('utf-8'))
			headimgurl = res['figureurl_qq_2'].encode('iso8859-1').decode('utf-8')

			# 校验是否有权限信息
			custom_user_auths = CustomUserAuths.objects.filter(identity_type="qq", identifier=openid)

			# 已经注册，直接登录
			if custom_user_auths.exists():
				custom_user_auth_obj = custom_user_auths.first()
				token = get_validate(openid, custom_user_auth_obj.custom_user_id.id, 0, CryptKey)
				# result_dict["err"] = 0
				# result_dict["msg"] = "success"
				# result_dict["data"]["token"] = token
				# result_dict["data"]["username"] = nickname
				# result_dict["data"]["uid"] = custom_user_auth_obj.custom_user_id.id

				user_info_str = "uid={uid}&nickname={nickname}&role={role}&avatar={avatar}&position={position}".format(
					uid=custom_user_auth_obj.custom_user_id.id,
					nickname=custom_user_auth_obj.custom_user_id.nickname,
					role=custom_user_auth_obj.custom_user_id.get_role_display(),
					avatar=custom_user_auth_obj.custom_user_id.avatar.url if custom_user_auth_obj.custom_user_id.avatar else "",
					position=custom_user_auth_obj.custom_user_id.position if custom_user_auth_obj.custom_user_id.position else "",
				)
				user_info = "user_info=" + base64.b64encode(user_info_str)
				if "?" in self.state:
					self.state += "&" + user_info
				else:
					self.state += "?" + user_info

			# user_dict = {
			#     "nickname": custom_user_auth_obj.custom_user_id.nickname,
			#     "uid": custom_user_auth_obj.custom_user_id.id,
			#     "avatar": custom_user_auth_obj.custom_user_id.avatar.name
			# }
			# request.session['token'] = token
			# request.session['user'] = user_dict
			# request.session['login'] = True
			else:
				if self.user_id:  # 绑定账号
					user_auth_dict = {
						"custom_user_id": CustomUser.objects.get(id=self.user_id),
						"identity_type": "qq",  # 登录类型
						"identifier": openid,  # 唯一标识
						"credential": access_token,  # 密码凭证
					}
					create_auth = CustomUserAuths.objects.create(**user_auth_dict)
				else:
					create_user = CustomUser.objects.create(nickname=nickname, role=0)
					avatar_filename = "_".join([time.strftime('%Y%m%d%H%M%S'), "qq.jpg"])
					avatar_path = os.path.join("custom_user_avatar", str(create_user.id), avatar_filename)
					create_user.avatar = avatar_path
					create_user.save()

					avatar_abs_path = os.path.join(MEDIA_ROOT, "custom_user_avatar", str(create_user.id))
					if not os.path.exists(avatar_abs_path):
						os.makedirs(avatar_abs_path)

					# resp = urllib2.urlopen(headimgurl)
					# real_url_str = str(resp.geturl())
					# req = urllib2.Request(real_url_str)
					resp = urllib2.urlopen(headimgurl)
					resp_html = resp.read()
					binfile = open(os.path.join(avatar_abs_path, avatar_filename), "wb")
					binfile.write(resp_html)
					binfile.close()

					if create_user:
						user_auth_dict = {
							"custom_user_id": create_user,
							"identity_type": "qq",  # 登录类型
							"identifier": openid,  # 唯一标识
							"credential": access_token,  # 密码凭证
						}
						create_auth = CustomUserAuths.objects.create(**user_auth_dict)

						if create_auth:
							token = get_validate(openid, create_user.id, 0, CryptKey)
							# result_dict["err"] = 0
							# result_dict["msg"] = "success"
							# result_dict["data"]["token"] = token
							# result_dict["data"]["username"] = nickname
							# result_dict["data"]["uid"] = create_user.id

							user_info_str = "uid={uid}&nickname={nickname}&role={role}&avatar={avatar}&position={position}".format(
								uid=create_user.id,
								nickname=create_user.nickname,
								role=create_user.get_role_display(),
								avatar=create_user.avatar.url if create_user.avatar else "",
								position=create_user.position if create_user.position else "",
							)
							user_info = "user_info=" + base64.b64encode(user_info_str)
							if "?" in self.state:
								self.state += "&" + user_info
							else:
								self.state += "?" + user_info
						# user_dict = {
						#     "nickname": create_user.nickname,
						#     "uid": create_user.id,
						#     "avatar": create_user.avatar.name
						# }
						# request.session['token'] = token
						# request.session['user'] = user_dict
						# request.session['login'] = True

						else:
							create_user.delete()
		# result_dict["msg"] = "用户权限添加失败"
		except:
			# result_dict["msg"] = traceback.format_exc()
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			res = HttpResponseRedirect(self.state)
			if not self.user_id:
				res.set_cookie("token", token)
			return res


# return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class CustomUserRegister(View):
	"""用户注册，"""

	def post(self, request, *args, **kwargs):
		result_dict = {
			"msg": "注册失败",
			"err": 1,
			"data": {}
		}
		token = ""
		try:
			param_dict = json.loads(request.body)
			username = param_dict.get("username")  # 邮箱/手机号，必填
			password = param_dict.get("password")  # 密码，必填
			verify_code = param_dict.get("verify_code")  # 验证码，必填
			invite_code = param_dict.get("invite_code")  # 班级邀请码，必填

			# 校验班级邀请码
			customuserclass = CustomUserClass.check_invite_code(invite_code)
			if not customuserclass:
				result_dict["err"] = 10
				result_dict["msg"] = "无效的班级邀请码！"
				return

			is_mail = IsMail().ismail(username)
			is_cellphone = IsCellphone().iscellphone(username)

			# 权限类型
			identity_type = ""
			if is_mail:
				identity_type = "email"

			if is_cellphone:
				identity_type = "phone"

				# 校验验证码
				valid_filter = {
					"phone": username,
					"is_use": False,
					"code": verify_code,
					"expire_time__gt": timezone.now(),
				}
				verifycodes = VerifyCode.objects.filter(**valid_filter)
				if not verifycodes.exists():
					result_dict["err"] = 7
					result_dict["msg"] = "无效的验证码！"
					return
				else:
					VerifyCode.objects.filter(phone=username).delete()

			# 校验是否有权限信息
			custom_user_auths = CustomUserAuths.objects.filter(identity_type=identity_type, identifier=username)

			# 已经注册
			if custom_user_auths.exists():
				result_dict["msg"] = "已经注册过账号，请直接登录"
				result_dict["err"] = 4
			elif identity_type:
				create_user = CustomUser.objects.create(nickname=username, role=0, class_s=customuserclass)
				if create_user:
					pycrypt_obj = PyCrypt(CryptKey)
					crypt_password = pycrypt_obj.encrypt(password)
					user_auth_dict = {
						"custom_user_id": create_user,
						"identity_type": identity_type,
						"identifier": username,
						"credential": crypt_password,  # 密码凭证
					}
					if is_mail:
						user_auth_dict.update({"status": False})  # 邮箱账户，默认未激活状态
					create_auth = CustomUserAuths.objects.create(**user_auth_dict)

					if create_auth:
						# 生成token
						token = get_validate(username, create_user.id, 0, CryptKey)
						result_dict["err"] = 0
						result_dict["msg"] = "success"
						# result_dict["data"]["token"] = token
						result_dict["data"]["user"] = {
							"uid": create_user.id,
							"nickname": create_user.nickname,
							"role": create_user.role,
							"avatar": create_user.avatar.url if create_user.avatar else "",
							"position": create_user.position if create_user.position else "",
						}

						# user_dict = {
						#     "nickname": create_user.nickname,
						#     "uid": create_user.id,
						#     "avatar": create_user.avatar.url if create_user.avatar else ""
						# }
						# request.session['token'] = token
						# request.session['user'] = user_dict
						# request.session['login'] = True

						if is_mail:
							send_result = send_activation_mail(username, create_user.id, create_auth.id)
							if not send_result:
								result_dict["err"] = 1
								result_dict["msg"] = "激活邮件发送失败"
					else:
						create_user.delete()
						result_dict["msg"] = "用户权限添加失败"
			else:
				result_dict["msg"] = "注册失败，请使用手机号或Email进行注册！"
		except:
			result_dict["msg"] = traceback.format_exc()
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			res = HttpResponse(json.dumps(result_dict, ensure_ascii=False))
			if token:
				res.set_cookie("token", token)
			return res


class CustomUserSendActivationMail(View):
	"""用户触发--发送激活邮箱账户邮件"""

	def post(self, request, *args, **kwargs):
		result_dict = {
			"msg": "激活邮箱账户邮件发送失败",
			"err": 1,
			"data": {}
		}
		try:
			param_dict = json.loads(request.body)
			email = param_dict.get("email")
			# 校验是否有权限信息
			custom_user_auths = CustomUserAuths.objects.filter(identity_type="email", identifier=email)
			if custom_user_auths.exists():
				custom_user_auths_obj = custom_user_auths.first()
				customer_user_id = custom_user_auths_obj.custom_user_id.id
				customer_user_auth_id = custom_user_auths_obj.id
				send_result = send_activation_mail(email, customer_user_id, customer_user_auth_id)
				if send_result:
					result_dict["err"] = 0
					result_dict["msg"] = "激活邮箱账户邮件发送成功"
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


def send_activation_mail(user_email, customer_user_id, customer_user_auth_id):
	"""发送邮箱账号激活邮件
	:param user_email: 用户邮箱地址
	:param customer_user_id: 用户ID
	:param customer_user_auth_id: 用户邮箱权限ID
	:return:
	"""
	send_result = False
	try:
		mail_subject = "智量酷邮箱账号激活"
		mail_content = "点击此链接完成激活，"
		activation_link = "http://www.zhiliangku.com/customuser/activation/result/?hash="
		email_str = "|".join([user_email, str(customer_user_id), str(customer_user_auth_id)])
		pycrypt_obj = PyCrypt(CryptKey)
		crypt_email = pycrypt_obj.encrypt(email_str)
		mail_content = "".join([mail_content, activation_link, crypt_email])
		send_result = sendmail(user_email, mail_subject, mail_content)
	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())
	finally:
		return send_result


class SendSMSVerificationCode(View):
	"""发送短信验证码"""

	def post(self, request, *args, **kwargs):
		result_dict = {
			"msg": "验证码发送失败或超限.",
			"err": 1,
		}
		try:
			param_dict = json.loads(request.body)
			phone = param_dict.get("phone")
			code = "".join([str(random.randint(0, 9)) for i in xrange(4)])

			# 是否有未使用验证码
			verifycodes = VerifyCode.objects.filter(phone=phone, is_use=False, expire_time__gt=timezone.now())
			if verifycodes.exists():
				verifycode_obj = verifycodes.first()
				create_time = verifycode_obj.create_time
				last_seconds = 70 - (timezone.now() - create_time).seconds
				if 0 < last_seconds < 70:
					result_dict["msg"] = "".join([str(last_seconds), "秒后尝试重新发送验证码"])
					result_dict["err"] = 8
				else:
					verifycodes.delete()
			else:
				try:
					is_send = sendmessage(phone, {'code': code})

					logging.getLogger().info('验证码短信发送成功')
					# code = hashlib.new('md5', code).hexdigest()
					if is_send:
						create_dict = {
							"phone": phone,
							"code": code,
							"create_time": timezone.now(),
							"expire_time": timezone.now() + datetime.timedelta(minutes=5),
						}
						VerifyCode.objects.filter(phone=phone).delete()
						VerifyCode.objects.create(**create_dict)
						result_dict["msg"] = "success"
						result_dict["err"] = 0

				except:
					traceback.print_exc()
					logging.getLogger().error('验证码短信发送失败')
					result_dict["err"] = 1
					result_dict["msg"] = '验证码短信发送失败, %s' % traceback.format_exc()
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = '验证码短信发送失败, %s' % traceback.format_exc()
		finally:
			VerifyCode.objects.filter(expire_time__lt=timezone.now()).delete()  # 清除过期验证码
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class ActivationCustomUserEmail(View):
	"""邮件中链接--激活邮箱类型账号"""

	def get(self, request, *args, **kwargs):
		result_dict = {
			"msg": "邮箱激活失败。",
			"err": 1,
			"data": {}
		}
		try:
			hash_str = request.GET.get("hash")
			pycrypt_obj = PyCrypt(CryptKey)
			crypt_str = pycrypt_obj.decrypt(hash_str)
			user_info_list = crypt_str.split("|")
			if len(user_info_list) == 3:
				user_email = user_info_list[0]
				customer_user_id = user_info_list[1]
				customer_user_auth_id = user_info_list[2]
				filter_dict = {
					"id": customer_user_auth_id,
					"custom_user_id": customer_user_id,
					"identity_type": "email",
					"identifier": user_email,
				}
				customuserauths_obj = CustomUserAuths.objects.filter(**filter_dict)
				if customuserauths_obj.exists():
					update_result = customuserauths_obj.update(status=True)
					if update_result:
						result_dict["err"] = 0
						result_dict["msg"] = "邮箱激活成功"
				else:
					result_dict["err"] = 2
					result_dict["msg"] = "待激活邮箱账户不存在"
			else:
				result_dict["err"] = 5
				result_dict["msg"] = "邮箱激活参数错误"
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = '通过邮箱激活账户异常, %s' % traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class ActivationResult(View):
	"""邮箱激活账号结果页面"""

	def get(self, request, *args, **kwargs):
		template_name = "customuser/activation/result/index.html"
		return render(request, template_name, {})


class RetrievePasswordByPhone(View):
	"""短信--找回密码"""

	def post(self, request, *args, **kwargs):
		result_dict = {
			"msg": "短信找回密码失败",
			"err": 1,
			"data": {}
		}
		try:
			param_dict = json.loads(request.body)
			phone = param_dict.get("phone")  # 手机号
			verify_code = param_dict.get("verify_code")  # 验证码
			new_password = param_dict.get("new_password")  # 新密码

			# 校验验证码
			valid_filter = {
				"phone": phone,
				"is_use": False,
				"code": verify_code,
				"expire_time__gt": timezone.now(),
			}
			is_valid = VerifyCode.objects.filter(**valid_filter)
			if not is_valid.exists():
				result_dict["err"] = 7
				result_dict["msg"] = "无效的验证码"
			else:
				filter_dict = {
					"identifier": phone,
					"identity_type": "phone",
				}
				customuserauths_objs = CustomUserAuths.objects.filter(**filter_dict)
				if customuserauths_objs.exists():
					pycrypt_obj = PyCrypt(CryptKey)
					crypt_password = pycrypt_obj.encrypt(new_password)
					update_filter = {
						"custom_user_id": customuserauths_objs.first().custom_user_id,
						"identity_type__in": ["phone", "email"],
					}
					update_result = CustomUserAuths.objects.filter(**update_filter).update(credential=crypt_password)
					if update_result:
						result_dict["err"] = 0
						result_dict["msg"] = "密码重置成功"
				else:
					result_dict["msg"] = "用户账户不存在"

		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = '短信找回密码异常, %s' % traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class SendEmailRetrievePassword(View):
	"""发送邮箱重置密码链接"""

	def post(self, request, *args, **kwargs):
		result_dict = {
			"msg": "找回密码邮箱验证信息发送失败",
			"err": 1,
			"data": {}
		}
		try:
			param_dict = json.loads(request.body)
			email = param_dict.get("email")
			filter_dict = {
				"identifier": email,
				"identity_type": "email",
			}
			customuserauths_objs = CustomUserAuths.objects.filter(**filter_dict)
			if customuserauths_objs.exists():
				mail_subject = "智量酷邮箱密码找回"
				mail_content = "点击此链接完成密码找回，"
				activation_link = "http://www.zhiliangku.com/customuser/retrieve_password_by_email?hash="
				pycrypt_obj = PyCrypt(CryptKey)
				crypt_email = pycrypt_obj.encrypt(email)
				mail_content = "".join([mail_content, activation_link, crypt_email])

				send_result = sendmail(email, mail_subject, mail_content)
				if not send_result:
					result_dict["msg"] = "邮箱密码找回链接发送失败"
				else:
					result_dict["msg"] = "邮箱密码找回链接发送成功"
					result_dict["err"] = 0
			else:
				result_dict["msg"] = "账户不存在"

		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = '找回密码邮箱验证信息发送异常, %s' % traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class RetrievePasswordByEmail(View):
	"""邮件表单找回密码"""

	# 通过邮箱链接返回重置密码表单页面
	def get(self, request, *args, **kwargs):
		template_name = "customuser/retrieve_password_by_email/index.html"
		return render(request, template_name, {})

	def post(self, request, *args, **kwargs):
		result_dict = {
			"msg": "短信找回密码失败",
			"err": 1,
		}
		try:
			param_dict = json.loads(request.body)
			email_hash = param_dict.get("hash")
			new_password = param_dict.get("password")
			pycrypt_obj = PyCrypt(CryptKey)
			email = pycrypt_obj.decrypt(email_hash)
			filter_dict = {
				"identifier": email,
				"identity_type": "email",
			}
			customuserauths_objs = CustomUserAuths.objects.filter(**filter_dict)
			if customuserauths_objs.exists():
				pycrypt_obj = PyCrypt(CryptKey)
				crypt_password = pycrypt_obj.encrypt(new_password)
				update_filter = {
					"custom_user_id": customuserauths_objs.first().custom_user_id,
					"identity_type__in": ["phone", "email"],
				}
				update_result = CustomUserAuths.objects.filter(**update_filter).update(credential=crypt_password)
				if update_result:
					result_dict["err"] = 0
					result_dict["msg"] = "密码重置成功"
			else:
				result_dict["msg"] = "用户账户不存在"

		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = '邮箱找回密码异常, %s' % traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class CustomUserLogout(View):
	"""登出"""

	def post(self, request, *args, **kwargs):
		result_dict = {
			"msg": "登出成功",
			"err": 0,
			"data": {}
		}
		response = HttpResponse(json.dumps(result_dict, ensure_ascii=False))
		response.delete_cookie('token')
		return response


class WeiXinWebPageLogin(View):
	"""针对公众号网页授权登录
	https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx96fdf187f5c8f9f2&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2fwebpage%2flogin&response_type=code&scope=snsapi_userinfo&state=L2FkbWlu&#wechat_redirect
	网页授权地址：https://open.weixin.qq.com/connect/oauth2/authorize
	appid：wx96fdf187f5c8f9f2
	redirect_uri：第三方后台接口地址（UrlEncode），http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2fwebpage%2flogin，http://www.zhiliangku.com/customuser/weixin/webpage/login
	response_type：code
	state：自定义参数，aHR0cDovL3d3dy56aGlsaWFuZ2t1LmNvbS93b3JsZGN1cC90b3BpYw==（登录成功后重定向地址，base64加密）http://www.zhiliangku.com/worldcup/topic
	#wechat_redirect
	"""
	appid = 'wx96fdf187f5c8f9f2'
	appsecret = 'a554a61688d97543a146c62d1fcd85b9'
	code = ''
	state = ''

	def get(self, request, *args, **kwargs):
		# result_dict = {
		#     "msg": "微信登录失败",
		#     "err": 1,
		#     "data": {}
		# }

		token = ""
		try:
			# https://open.weixin.qq.com/connect/qrconnect?appid=wx7c9efe7b17c8aef2&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2flogin&response_type=code&scope=snsapi_login&state=L2FkbWlu#wechat_redirect
			self.code = self.request.GET.get("code")
			self.state = self.request.GET.get("state")
			self.user_id = self.request.GET.get("u")  # 绑定账号用

			# 解base64,重定向url
			self.state = base64.b64decode(self.state)

			# 2.通过code换取网页授权access_token
			try:
				url = u'https://api.weixin.qq.com/sns/oauth2/access_token'
				params = {
					'appid': self.appid,
					'secret': self.appsecret,
					'code': self.code,
					'grant_type': 'authorization_code'
				}
				res = requests.get(url, params=params, verify=False).json()
				"""res
				{
					u'openid': u'oz4KJ1j8fwabm3IA1CwFtpE4fJ_M',
					u'access_token': u'4_RkYEXcSJBvIyYaRbrUHIQFk3XfQ3Qv0yYpJpDudVrReCaqEKX9X0AmI1K5kvC2WHRGz3bBerbQwfhtbAvECaGA',
					u'unionid': u'oQB0n1D3swsSJLAWnb9UMHQ4F4Jk',
					u'expires_in': 7200,
					u'scope': u'snsapi_login',
					u'refresh_token': u'4_DPwMWtOnKvESpKGhXLLP2e2DU0qHH276HSscaOH610Fr6hH4SfaCweeV68OoJEUEYMpMWICTTFOXVg48UigYpA'
				}
				"""
				access_token = res["access_token"]
			except:
				traceback.print_exc()
				logging.getLogger().info("获取access_token参数错误：\n%s" % traceback.format_exc())
				raise Http404()

			# 3.如果access_token超时，那就刷新
			# 注意,这里我没有写这个刷新功能,不影响使用,如果想写的话,可以自己去看文档

			# 4.拉取用户信息
			try:
				user_info_url = u'https://api.weixin.qq.com/sns/userinfo'
				params = {
					'access_token': res["access_token"],
					'openid': res["openid"],
				}
				res = requests.get(user_info_url, params=params, verify=False).json()
				"""
				{
					u'province': u'Beijing',
					u'openid': u'oz4KJ1j8fwabm3IA1CwFtpE4fJ_M',
					u'headimgurl': u'http: //wx.qlogo.cn/mmopen/vi_32/DYAIOgq83eqic03RMYMUSxqh13fWTTuneZibUDTuG6mruQxwkQqChiajlZF5FFq8Rk7pR6Ll2v3tv8uw7dMzA5Jnw/0',
					u'language': u'zh_CN',
					u'city': u'Haidian',
					u'country': u'CN',
					u'sex': 1,
					u'unionid': u'oQB0n1D3swsSJLAWnb9UMHQ4F4Jk',
					u'privilege': [

					],
					u'nickname': u'Maybe'
				}
				注意,这里有个坑,res['nickname']表面上是unicode编码,
				但是里面的串却是str的编码,举个例子,res['nickname']的返回值可能是这种形式
				u'\xe9\x97\xab\xe5\xb0\x8f\xe8\x83\x96',直接存到数据库会是乱码.必须要转成
				unicode的编码,需要使用
				res['nickname'] = res['nickname'].encode('iso8859-1').decode('utf-8')
				这种形式来转换.
				你也可以写个循环来转化.
				for value in res.values():
					value = value.encode('iso8859-1').decode('utf-8')
				"""
			except:
				traceback.print_exc()
				logging.getLogger().info("拉取用户信息错误：\n%s" % traceback.format_exc())

			nickname = remove_emoji(res['nickname'].encode('iso8859-1').decode('utf-8'))
			headimgurl = res['headimgurl'].encode('iso8859-1').decode('utf-8')
			openid = res['openid'].encode('iso8859-1').decode('utf-8')

			# 校验是否有权限信息
			custom_user_auths = CustomUserAuths.objects.filter(identity_type="weixin", identifier=openid)

			# 已经注册，直接登录
			if custom_user_auths.exists():
				custom_user_auth_obj = custom_user_auths.first()
				token = get_validate(openid, custom_user_auth_obj.custom_user_id.id, 0, CryptKey)
				# result_dict["err"] = 0
				# result_dict["msg"] = "success"
				# result_dict["data"]["token"] = token
				# result_dict["data"]["user"] = {
				#     "uid": custom_user_auth_obj.custom_user_id.id,
				#     "nickname": custom_user_auth_obj.custom_user_id.nickname,
				#     "role": custom_user_auth_obj.custom_user_id.role,
				#     "avatar": custom_user_auth_obj.custom_user_id.avatar.url if custom_user_auth_obj.custom_user_id.avatar else "",
				#     "position": custom_user_auth_obj.custom_user_id.position,
				# }

				user_info_str = "uid={uid}&nickname={nickname}&role={role}&avatar={avatar}&position={position}".format(
					uid=custom_user_auth_obj.custom_user_id.id,
					nickname=custom_user_auth_obj.custom_user_id.nickname,
					role=custom_user_auth_obj.custom_user_id.get_role_display(),
					avatar=custom_user_auth_obj.custom_user_id.avatar.url if custom_user_auth_obj.custom_user_id.avatar else "",
					position=custom_user_auth_obj.custom_user_id.position if custom_user_auth_obj.custom_user_id.position else "",
				)
				user_info = "user_info=" + base64.b64encode(user_info_str)
				if "?" in self.state:
					self.state += "&" + user_info
				else:
					self.state += "?" + user_info

			# user_dict = {
			#     "nickname": custom_user_auth_obj.custom_user_id.nickname,
			#     "uid": custom_user_auth_obj.custom_user_id.id,
			#     "avatar": custom_user_auth_obj.custom_user_id.avatar.name
			# }
			# request.session['token'] = token
			# request.session['user'] = user_dict
			# request.session['login'] = True
			else:
				if self.user_id:  # 绑定账号
					user_auth_dict = {
						"custom_user_id": CustomUser.objects.get(id=self.user_id),
						"identity_type": "weixin",  # 登录类型
						"identifier": openid,  # 唯一标识
						"credential": access_token,  # 密码凭证
					}
					create_auth = CustomUserAuths.objects.create(**user_auth_dict)
				else:
					create_user = CustomUser.objects.create(nickname=nickname, role=0)
					avatar_filename = "_".join([time.strftime('%Y%m%d%H%M%S'), "weixin.jpg"])
					avatar_path = os.path.join("custom_user_avatar", str(create_user.id), avatar_filename)
					create_user.avatar = avatar_path
					create_user.save()

					# 下载头像
					avatar_abs_path = os.path.join(MEDIA_ROOT, "custom_user_avatar", str(create_user.id))
					if not os.path.exists(avatar_abs_path):
						os.makedirs(avatar_abs_path)

					# resp = urllib2.urlopen(headimgurl)
					# real_url_str = str(resp.geturl())
					# req = urllib2.Request(real_url_str)
					resp = urllib2.urlopen(headimgurl)
					resp_html = resp.read()
					binfile = open(os.path.join(avatar_abs_path, avatar_filename), "wb")
					binfile.write(resp_html)
					binfile.close()

					if create_user:
						user_auth_dict = {
							"custom_user_id": create_user,
							"identity_type": "weixin",  # 登录类型
							"identifier": openid,  # 唯一标识
							"credential": access_token,  # 密码凭证
						}
						create_auth = CustomUserAuths.objects.create(**user_auth_dict)

						if create_auth:
							# 生成token
							token = get_validate(openid, create_user.id, 0, CryptKey)
							# result_dict["err"] = 0
							# result_dict["msg"] = "success"
							# result_dict["data"]["token"] = token
							# result_dict["data"]["user"] = {
							#     "uid": create_user.id,
							#     "nickname": create_user.nickname,
							#     "role": create_user.role,
							#     "avatar": create_user.avatar.url if create_user.avatar else "",
							#     "position": create_user.position,
							# }
							user_info_str = "uid={uid}&nickname={nickname}&role={role}&avatar={avatar}&position={position}".format(
								uid=create_user.id,
								nickname=create_user.nickname,
								role=create_user.get_role_display(),
								avatar=create_user.avatar.url if create_user.avatar else "",
								position=create_user.position if create_user.position else "",
							)
							user_info = "user_info=" + base64.b64encode(user_info_str)
							if "?" in self.state:
								self.state += "&" + user_info
							else:
								self.state += "?" + user_info

						# user_dict = {
						#     "nickname": create_user.nickname,
						#     "uid": create_user.id,
						#     "avatar": create_user.avatar.name
						# }
						# request.session['token'] = token
						# request.session['user'] = user_dict
						# request.session['login'] = True

						else:
							create_user.delete()
		# result_dict["msg"] = "用户权限添加失败"
		except:
			# result_dict["msg"] = traceback.format_exc()
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			res = HttpResponseRedirect(self.state)
			if not self.user_id:
				res.set_cookie("token", token)
			return res
