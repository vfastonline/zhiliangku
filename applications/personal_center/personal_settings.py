#!encoding:utf-8

import urllib2
import urlparse

import requests
from django.http import Http404
from django.views.generic import View

from applications.custom_user.models import *
from applications.custom_user.views import CryptKey
from applications.custom_user.views import send_activation_mail
from lib.encrypt import PyCrypt
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import *
from zhiliangku.settings import MEDIA_ROOT

"""个人设置"""


@class_view_decorator(user_login_required)
class UpdateBasicInfo(View):
    """基本信息修改"""

    def post(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": dict(),
        }
        try:
            param_dict = json.loads(request.body)
            custom_user_id = param_dict.get('custom_user_id', 0)  # 必填，用户ID
            nickname = param_dict.get('nickname', "")  # 必填，昵称
            sex = param_dict.get('sex')  # 必填，性别
            signature = param_dict.get('signature', "")  # 个性签名

            customusers = CustomUser.objects.filter(id=custom_user_id)
            data_dict = dict()
            if customusers.exists():
                customuser = customusers.first()
                customuser.nickname = nickname
                customuser.signature = signature
                customuser.sex = sex
                customuser.save()

                data_dict["nickname"] = customuser.nickname
                data_dict["signature"] = customuser.signature if customuser.signature else ""
                data_dict["sex"] = customuser.get_sex_display()
            else:
                result_dict["msg"] = "找不到对应用户"
            result_dict["data"] = data_dict
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class GetUserAccount(View):
    """账号绑定--获取账号"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": dict(),
        }
        try:
            custom_user_id = request.GET.get('custom_user_id', 0)  # 用户ID
            customuserauths = CustomUserAuths.objects.filter(custom_user_id__id=custom_user_id)
            data_dict = dict()

            if customuserauths.exists():
                for one_auth in customuserauths:
                    identity_type_str = one_auth.identity_type
                    if identity_type_str == "email":
                        data_dict["email"] = one_auth.identifier
                    elif identity_type_str == "phone":
                        data_dict["phone"] = one_auth.identifier
                    elif identity_type_str == "weixin":
                        data_dict["weixin"] = 1
                    elif identity_type_str == "qq":
                        data_dict["qq"] = 1

            result_dict["data"] = data_dict
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class AccountBindPhone(View):
    """账号绑定--手机"""

    def post(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": dict(),
        }
        try:
            param_dict = json.loads(request.body)
            custom_user_id = param_dict.get('custom_user_id', 0)  # 用户ID
            phone = param_dict.get('phone', "")  # 手机号
            password = param_dict.get('password')  # 密码
            verify_code = param_dict.get("verify_code")  # 验证码

            # 校验验证码
            valid_filter = {
                "phone": phone,
                "is_use": False,
                "code": verify_code,
                "expire_time__gt": timezone.now(),
            }
            verifycodes = VerifyCode.objects.filter(**valid_filter)
            if not verifycodes.exists():
                result_dict["err"] = 7
                result_dict["msg"] = "无效的验证码"
                return
            else:
                VerifyCode.objects.filter(phone=phone).delete()

            filter_param = {
                "custom_user_id__id": custom_user_id,
                "identity_type": "email"
            }
            customuserauths = CustomUserAuths.objects.filter(**filter_param)
            filter_param.update({"identity_type": "phone"})
            customuserauths_phone = CustomUserAuths.objects.filter(**filter_param)

            # 有邮箱账号，没有手机账号
            if customuserauths.exists() and not customuserauths_phone.exists():
                credential = customuserauths.first().credential

                user_auth_dict = {
                    "custom_user_id": CustomUser.objects.get(id=custom_user_id),
                    "identity_type": "phone",
                    "identifier": phone,
                    "credential": credential,  # 密码凭证
                    "status": False,
                }

                obj = CustomUserAuths.objects.create(**user_auth_dict)
            elif customuserauths_phone.exists():
                obj = customuserauths_phone.update(identifier=phone)
            else:
                pycrypt_obj = PyCrypt(CryptKey)
                crypt_password = pycrypt_obj.encrypt(password)
                user_auth_dict = {
                    "custom_user_id": CustomUser.objects.get(id=custom_user_id),
                    "identity_type": "phone",
                    "identifier": phone,
                    "credential": crypt_password,  # 密码凭证
                }

                obj = CustomUserAuths.objects.create(**user_auth_dict)
            if not obj:
                result_dict["err"] = 1
                result_dict["msg"] = "手机账号绑定失败"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class AccountBindEmail(View):
    """账号绑定--邮箱"""

    def post(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": dict(),
        }
        try:
            param_dict = json.loads(request.body)
            custom_user_id = param_dict.get('custom_user_id', 0)  # 用户ID
            email = param_dict.get('email', "")  # 邮箱地址
            password = param_dict.get('password')  # 密码

            filter_param = {
                "custom_user_id__id": custom_user_id,
                "identity_type": "phone"
            }
            customuserauths = CustomUserAuths.objects.filter(**filter_param)
            filter_param.update({"identity_type": "email"})
            customuserauths_email = CustomUserAuths.objects.filter(**filter_param)

            is_mail = False
            auth_id = 0

            # 有手机账号，没有邮箱账号
            if customuserauths.exists() and not customuserauths_email.exists():
                credential = customuserauths.first().credential

                user_auth_dict = {
                    "custom_user_id": CustomUser.objects.get(id=custom_user_id),
                    "identity_type": "email",
                    "identifier": email,
                    "credential": credential,  # 密码凭证
                    "status": False,
                }

                obj = CustomUserAuths.objects.create(**user_auth_dict)
                if obj:
                    auth_id = obj.id
                    is_mail = True
            elif customuserauths_email.exists():
                rows = customuserauths_email.update(identifier=email, status=False)
                if rows:
                    auth_id = customuserauths_email.first().id
                    is_mail = True
            else:
                pycrypt_obj = PyCrypt(CryptKey)
                crypt_password = pycrypt_obj.encrypt(password)
                user_auth_dict = {
                    "custom_user_id": CustomUser.objects.get(id=custom_user_id),
                    "identity_type": "email",
                    "identifier": email,
                    "credential": crypt_password,  # 密码凭证
                    "status": False,
                }

                obj = CustomUserAuths.objects.create(**user_auth_dict)
                if obj:
                    auth_id = obj.id
                    is_mail = True

            if is_mail and auth_id:
                send_result = send_activation_mail(email, custom_user_id, auth_id)
                if not send_result:
                    result_dict["err"] = 1
                    result_dict["msg"] = "激活邮件发送失败"
            else:
                result_dict["err"] = 1
                result_dict["msg"] = "邮箱账号绑定失败"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


# @class_view_decorator(user_login_required)
class AccountBindWeiXin(View):
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
            print "33333333333333333"
            # https://open.weixin.qq.com/connect/qrconnect?appid=wx7c9efe7b17c8aef2&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fcustomuser%2fweixin%2flogin&response_type=code&scope=snsapi_login&state=L2FkbWlu#wechat_redirect
            # self.code = self.request.GET.get("code")
            # self.state = self.request.GET.get("state")
            #
            # # 解base64,重定向url
            # self.state = base64.b64decode(self.state)
            #
            # # 2.通过code换取网页授权access_token
            # try:
            #     url = u'https://api.weixin.qq.com/sns/oauth2/access_token'
            #     params = {
            #         'appid': self.appid,
            #         'secret': self.appsecret,
            #         'code': self.code,
            #         'grant_type': 'authorization_code'
            #     }
            #     res = requests.get(url, params=params, verify=False).json()
            #     """res
            #     {
            #         u'openid': u'oz4KJ1j8fwabm3IA1CwFtpE4fJ_M',
            #         u'access_token': u'4_RkYEXcSJBvIyYaRbrUHIQFk3XfQ3Qv0yYpJpDudVrReCaqEKX9X0AmI1K5kvC2WHRGz3bBerbQwfhtbAvECaGA',
            #         u'unionid': u'oQB0n1D3swsSJLAWnb9UMHQ4F4Jk',
            #         u'expires_in': 7200,
            #         u'scope': u'snsapi_login',
            #         u'refresh_token': u'4_DPwMWtOnKvESpKGhXLLP2e2DU0qHH276HSscaOH610Fr6hH4SfaCweeV68OoJEUEYMpMWICTTFOXVg48UigYpA'
            #     }
            #     """
            #     access_token = res["access_token"]
            # except:
            #     traceback.print_exc()
            #     logging.getLogger().info("获取access_token参数错误：\n%s" % traceback.format_exc())
            #     raise Http404()
            #
            # # 3.如果access_token超时，那就刷新
            # # 注意,这里我没有写这个刷新功能,不影响使用,如果想写的话,可以自己去看文档
            #
            # # 4.拉取用户信息
            # try:
            #     user_info_url = u'https://api.weixin.qq.com/sns/userinfo'
            #     params = {
            #         'access_token': res["access_token"],
            #         'openid': res["openid"],
            #     }
            #     res = requests.get(user_info_url, params=params, verify=False).json()
            #     """
            #     {
            #         u'province': u'Beijing',
            #         u'openid': u'oz4KJ1j8fwabm3IA1CwFtpE4fJ_M',
            #         u'headimgurl': u'http: //wx.qlogo.cn/mmopen/vi_32/DYAIOgq83eqic03RMYMUSxqh13fWTTuneZibUDTuG6mruQxwkQqChiajlZF5FFq8Rk7pR6Ll2v3tv8uw7dMzA5Jnw/0',
            #         u'language': u'zh_CN',
            #         u'city': u'Haidian',
            #         u'country': u'CN',
            #         u'sex': 1,
            #         u'unionid': u'oQB0n1D3swsSJLAWnb9UMHQ4F4Jk',
            #         u'privilege': [
            #
            #         ],
            #         u'nickname': u'Maybe'
            #     }
            #     注意,这里有个坑,res['nickname']表面上是unicode编码,
            #     但是里面的串却是str的编码,举个例子,res['nickname']的返回值可能是这种形式
            #     u'\xe9\x97\xab\xe5\xb0\x8f\xe8\x83\x96',直接存到数据库会是乱码.必须要转成
            #     unicode的编码,需要使用
            #     res['nickname'] = res['nickname'].encode('iso8859-1').decode('utf-8')
            #     这种形式来转换.
            #     你也可以写个循环来转化.
            #     for value in res.values():
            #         value = value.encode('iso8859-1').decode('utf-8')
            #     """
            # except:
            #     traceback.print_exc()
            #     logging.getLogger().info("拉取用户信息错误：\n%s" % traceback.format_exc())
            #
            # nickname = res['nickname'].encode('iso8859-1').decode('utf-8')
            # headimgurl = res['headimgurl'].encode('iso8859-1').decode('utf-8')
            # openid = res['openid'].encode('iso8859-1').decode('utf-8')
            #
            # # 校验是否有权限信息
            # custom_user_auths = CustomUserAuths.objects.filter(identity_type="weixin", identifier=openid)
            #
            # # 已经注册，直接登录
            # if custom_user_auths.exists():
            #     custom_user_auth_obj = custom_user_auths.first()
            #     token = get_validate(openid, custom_user_auth_obj.custom_user_id.id, 0, CryptKey)
            #     # result_dict["err"] = 0
            #     # result_dict["msg"] = "success"
            #     # result_dict["data"]["token"] = token
            #     # result_dict["data"]["user"] = {
            #     #     "uid": custom_user_auth_obj.custom_user_id.id,
            #     #     "nickname": custom_user_auth_obj.custom_user_id.nickname,
            #     #     "role": custom_user_auth_obj.custom_user_id.role,
            #     #     "avatar": custom_user_auth_obj.custom_user_id.avatar.url if custom_user_auth_obj.custom_user_id.avatar else "",
            #     #     "position": custom_user_auth_obj.custom_user_id.position,
            #     # }
            #
            #     user_info_str = "uid={uid}&nickname={nickname}&role={role}&avatar={avatar}&position={position}".format(
            #         uid=custom_user_auth_obj.custom_user_id.id,
            #         nickname=custom_user_auth_obj.custom_user_id.nickname,
            #         role=custom_user_auth_obj.custom_user_id.get_role_display(),
            #         avatar=custom_user_auth_obj.custom_user_id.avatar.url if custom_user_auth_obj.custom_user_id.avatar else "",
            #         position=custom_user_auth_obj.custom_user_id.position if custom_user_auth_obj.custom_user_id.position else "",
            #     )
            #     user_info = "user_info=" + base64.b64encode(user_info_str)
            #     if "?" in self.state:
            #         self.state += "&" + user_info
            #     else:
            #         self.state += "?" + user_info
            #
            #         # user_dict = {
            #         #     "nickname": custom_user_auth_obj.custom_user_id.nickname,
            #         #     "uid": custom_user_auth_obj.custom_user_id.id,
            #         #     "avatar": custom_user_auth_obj.custom_user_id.avatar.name
            #         # }
            #         # request.session['token'] = token
            #         # request.session['user'] = user_dict
            #         # request.session['login'] = True
            # else:
            #     create_user = CustomUser.objects.create(nickname=nickname, role=0)
            #     avatar_filename = "_".join([time.strftime('%Y%m%d%H%M%S'), "weixin.jpg"])
            #     avatar_path = os.path.join("custom_user_avatar", str(create_user.id), avatar_filename)
            #     create_user.avatar = avatar_path
            #     create_user.save()
            #
            #     # 下载头像
            #     avatar_abs_path = os.path.join(MEDIA_ROOT, "custom_user_avatar", str(create_user.id))
            #     if not os.path.exists(avatar_abs_path):
            #         os.makedirs(avatar_abs_path)
            #
            #     # resp = urllib2.urlopen(headimgurl)
            #     # real_url_str = str(resp.geturl())
            #     # req = urllib2.Request(real_url_str)
            #     resp = urllib2.urlopen(headimgurl)
            #     resp_html = resp.read()
            #     binfile = open(os.path.join(avatar_abs_path, avatar_filename), "wb")
            #     binfile.write(resp_html)
            #     binfile.close()
            #
            #     if create_user:
            #         user_auth_dict = {
            #             "custom_user_id": create_user,
            #             "identity_type": "weixin",  # 登录类型
            #             "identifier": openid,  # 唯一标识
            #             "credential": access_token,  # 密码凭证
            #         }
            #         create_auth = CustomUserAuths.objects.create(**user_auth_dict)
            #
            #         if create_auth:
            #             # 生成token
            #             token = get_validate(openid, create_user.id, 0, CryptKey)
            #             # result_dict["err"] = 0
            #             # result_dict["msg"] = "success"
            #             # result_dict["data"]["token"] = token
            #             # result_dict["data"]["user"] = {
            #             #     "uid": create_user.id,
            #             #     "nickname": create_user.nickname,
            #             #     "role": create_user.role,
            #             #     "avatar": create_user.avatar.url if create_user.avatar else "",
            #             #     "position": create_user.position,
            #             # }
            #             user_info_str = "uid={uid}&nickname={nickname}&role={role}&avatar={avatar}&position={position}".format(
            #                 uid=create_user.id,
            #                 nickname=create_user.nickname,
            #                 role=create_user.get_role_display(),
            #                 avatar=create_user.avatar.url if create_user.avatar else "",
            #                 position=create_user.position if create_user.position else "",
            #             )
            #             user_info = "user_info=" + base64.b64encode(user_info_str)
            #             if "?" in self.state:
            #                 self.state += "&" + user_info
            #             else:
            #                 self.state += "?" + user_info
            #
            #                 # user_dict = {
            #                 #     "nickname": create_user.nickname,
            #                 #     "uid": create_user.id,
            #                 #     "avatar": create_user.avatar.name
            #                 # }
            #                 # request.session['token'] = token
            #                 # request.session['user'] = user_dict
            #                 # request.session['login'] = True
            #
            #         else:
            #             create_user.delete()
            #             # result_dict["msg"] = "用户权限添加失败"
        except:
            # result_dict["msg"] = traceback.format_exc()
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
        finally:
            print "44444444"
            # res = HttpResponseRedirect(self.state)
            # res.set_cookie("token", token)
            # return res
            # return HttpResponse(json.dumps(result_dict, ensure_ascii=False))

@class_view_decorator(user_login_required)
class AccountBindQQ(View):
    appid = '101447834'
    appkey = '7c57f3120ce94f59dc217f25333b086a'
    code = ''
    state = ''

    def get(self, request, *args, **kwargs):
        result_dict = {
            "msg": "QQ绑定失败",
            "err": 1,
            "data": {}
        }

        token = ""
        try:
            print "222222222"
            # # 第一步获取code跟state
            # # https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&client_id=101447834&redirect_uri=http%3a%2f%2fwww.zhiliangku.com%2fpersonal_center%2fpersonal_settings%2faccountbind%2fqq&state=L2FkbWlu&scope=get_user_info,get_info
            # self.code = self.request.GET.get("code")
            # self.state = self.request.GET.get("state")
            #
            # # 解base64,重定向url
            # self.state = base64.b64decode(self.state)
            #
            # # 2.通过code换取网页授权access_token
            # access_token = ""
            # try:
            #     url = 'https://graph.qq.com/oauth2.0/token'
            #     params = {
            #         'grant_type': 'authorization_code',
            #         'client_id': self.appid,
            #         'client_secret': self.appkey,
            #         'code': self.code,
            #         'redirect_uri': "http://www.zhiliangku.com/customuser/qq/login",
            #
            #     }
            #     res = requests.get(url, params=params, verify=False).text
            #     result = urlparse.urlparse(res)
            #     param_dict = urlparse.parse_qs(result.path, True)
            #     access_tokens = param_dict.get("access_token", [])
            #     expires_ins = param_dict.get("expires_in", [])
            #     refresh_tokens = param_dict.get("refresh_token", [])
            #     if access_tokens:
            #         access_token = access_tokens[0]
            # except:
            #     traceback.print_exc()
            #     logging.getLogger().info("获取access_token参数错误：\n%s" % traceback.format_exc())
            #     raise Http404()
            #
            # # 获取用户OpenID
            # openid = ""
            # try:
            #     me_url = 'https://graph.qq.com/oauth2.0/me'
            #     params = {
            #         'access_token': access_token,
            #     }
            #     res = requests.get(me_url, params=params, verify=False).text
            #     v_str = str(res)[9:-3]
            #     v_json = json.loads(v_str)
            #     openid = v_json.get('openid')
            # except:
            #     traceback.print_exc()
            #     logging.getLogger().info("拉取用户OpenID错误：\n%s" % traceback.format_exc())
            #
            # # 获取用户信息
            # try:
            #     get_user_info_url = 'https://graph.qq.com/user/get_user_info'
            #     params = {
            #         'access_token': access_token,
            #         'oauth_consumer_key': self.appid,
            #         'openid': openid,
            #     }
            #     res = requests.get(get_user_info_url, params=params, verify=False).json()
            #     """
            #     {
            #         "ret":0,
            #         "msg":"",
            #         "nickname":"Peter",
            #         "figureurl":"http://qzapp.qlogo.cn/qzapp/111111/942FEA70050EEAFBD4DCE2C1FC775E56/30",
            #         "figureurl_1":"http://qzapp.qlogo.cn/qzapp/111111/942FEA70050EEAFBD4DCE2C1FC775E56/50",
            #         "figureurl_2":"http://qzapp.qlogo.cn/qzapp/111111/942FEA70050EEAFBD4DCE2C1FC775E56/100",
            #         "figureurl_qq_1":"http://q.qlogo.cn/qqapp/100312990/DE1931D5330620DBD07FB4A5422917B6/40",
            #         "figureurl_qq_2":"http://q.qlogo.cn/qqapp/100312990/DE1931D5330620DBD07FB4A5422917B6/100",
            #         "gender":"男",
            #         "is_yellow_vip":"1",
            #         "vip":"1",
            #         "yellow_vip_level":"7",
            #         "level":"7",
            #         "is_yellow_year_vip":"1"
            #         }
            #     """
            # except:
            #     traceback.print_exc()
            #     logging.getLogger().info("拉取用户信息错误：\n%s" % traceback.format_exc())
            #
            # nickname = res['nickname']  # .encode('iso8859-1').decode('utf-8')
            # headimgurl = res['figureurl_qq_2'].encode('iso8859-1').decode('utf-8')
            #
            # # 校验是否有权限信息
            # custom_user_auths = CustomUserAuths.objects.filter(identity_type="qq", identifier=openid)
            #
            # # 已经注册，直接登录
            # if custom_user_auths.exists():
            #     custom_user_auth_obj = custom_user_auths.first()
            #     token = get_validate(openid, custom_user_auth_obj.custom_user_id.id, 0, CryptKey)
            #     # result_dict["err"] = 0
            #     # result_dict["msg"] = "success"
            #     # result_dict["data"]["token"] = token
            #     # result_dict["data"]["username"] = nickname
            #     # result_dict["data"]["uid"] = custom_user_auth_obj.custom_user_id.id
            #
            #     user_info_str = "uid={uid}&nickname={nickname}&role={role}&avatar={avatar}&position={position}".format(
            #         uid=custom_user_auth_obj.custom_user_id.id,
            #         nickname=custom_user_auth_obj.custom_user_id.nickname,
            #         role=custom_user_auth_obj.custom_user_id.get_role_display(),
            #         avatar=custom_user_auth_obj.custom_user_id.avatar.url if custom_user_auth_obj.custom_user_id.avatar else "",
            #         position=custom_user_auth_obj.custom_user_id.position if custom_user_auth_obj.custom_user_id.position else "",
            #     )
            #     user_info = "user_info=" + base64.b64encode(user_info_str)
            #     if "?" in self.state:
            #         self.state += "&" + user_info
            #     else:
            #         self.state += "?" + user_info
            #
            #         # user_dict = {
            #         #     "nickname": custom_user_auth_obj.custom_user_id.nickname,
            #         #     "uid": custom_user_auth_obj.custom_user_id.id,
            #         #     "avatar": custom_user_auth_obj.custom_user_id.avatar.name
            #         # }
            #         # request.session['token'] = token
            #         # request.session['user'] = user_dict
            #         # request.session['login'] = True
            # else:
            #     create_user = CustomUser.objects.create(nickname=nickname, role=0)
            #     avatar_filename = "_".join([time.strftime('%Y%m%d%H%M%S'), "qq.jpg"])
            #     avatar_path = os.path.join("custom_user_avatar", str(create_user.id), avatar_filename)
            #     create_user.avatar = avatar_path
            #     create_user.save()
            #
            #     avatar_abs_path = os.path.join(MEDIA_ROOT, "custom_user_avatar", str(create_user.id))
            #     if not os.path.exists(avatar_abs_path):
            #         os.makedirs(avatar_abs_path)
            #
            #     # resp = urllib2.urlopen(headimgurl)
            #     # real_url_str = str(resp.geturl())
            #     # req = urllib2.Request(real_url_str)
            #     resp = urllib2.urlopen(headimgurl)
            #     resp_html = resp.read()
            #     binfile = open(os.path.join(avatar_abs_path, avatar_filename), "wb")
            #     binfile.write(resp_html)
            #     binfile.close()
            #
            #     if create_user:
            #         user_auth_dict = {
            #             "custom_user_id": create_user,
            #             "identity_type": "qq",  # 登录类型
            #             "identifier": openid,  # 唯一标识
            #             "credential": access_token,  # 密码凭证
            #         }
            #         create_auth = CustomUserAuths.objects.create(**user_auth_dict)
            #
            #         if create_auth:
            #             token = get_validate(openid, create_user.id, 0, CryptKey)
            #             # result_dict["err"] = 0
            #             # result_dict["msg"] = "success"
            #             # result_dict["data"]["token"] = token
            #             # result_dict["data"]["username"] = nickname
            #             # result_dict["data"]["uid"] = create_user.id
            #
            #             user_info_str = "uid={uid}&nickname={nickname}&role={role}&avatar={avatar}&position={position}".format(
            #                 uid=create_user.id,
            #                 nickname=create_user.nickname,
            #                 role=create_user.get_role_display(),
            #                 avatar=create_user.avatar.url if create_user.avatar else "",
            #                 position=create_user.position if create_user.position else "",
            #             )
            #             user_info = "user_info=" + base64.b64encode(user_info_str)
            #             if "?" in self.state:
            #                 self.state += "&" + user_info
            #             else:
            #                 self.state += "?" + user_info
            #                 # user_dict = {
            #                 #     "nickname": create_user.nickname,
            #                 #     "uid": create_user.id,
            #                 #     "avatar": create_user.avatar.name
            #                 # }
            #                 # request.session['token'] = token
            #                 # request.session['user'] = user_dict
            #                 # request.session['login'] = True
            #
            #         else:
            #             create_user.delete()
            #             # result_dict["msg"] = "用户权限添加失败"
        except:
            # result_dict["msg"] = traceback.format_exc()
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
        finally:
            print "33333333"
            # res = HttpResponseRedirect(self.state)
            # res.set_cookie("token", token)
            # return res
            # return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class ChangePassword(View):
    """密码设置"""

    def post(self, request, *args, **kwargs):
        result_dict = {
            "err": 1,
            "msg": "修改失败",
        }
        try:
            param_dict = json.loads(request.body)
            custom_user_id = param_dict.get('custom_user_id', 0)  # 用户ID
            old_password = param_dict.get('old_password', "")  # 旧密码
            password = param_dict.get('password', "")  # 新密码

            filter_param = {
                "custom_user_id__id": custom_user_id,
                "identity_type__in": ["email", "phone"]
            }
            customuserauths = CustomUserAuths.objects.filter(**filter_param)
            if customuserauths.exists():
                # 比对旧密码
                pycrypt_obj = PyCrypt(CryptKey)
                crypt_password = pycrypt_obj.encrypt(old_password)

                if customuserauths.filter(credential=crypt_password).exists():
                    new_crypt_password = pycrypt_obj.encrypt(password)
                    customuserauths.update(credential=new_crypt_password)
                    result_dict["err"] = 0
                    result_dict["msg"] = "成功重置密码"
                else:
                    result_dict["msg"] = "旧密码错误"
            else:
                result_dict["msg"] = "未绑定邮箱/手机账号"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class UserAddress(View):
    """收货地址"""

    def get(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": dict(),
        }
        try:
            custom_user_id = request.GET.get('custom_user_id', 0)  # 用户ID
            customusers = CustomUser.objects.filter(id=custom_user_id)
            data_dict = dict()

            if customusers.exists():
                customuser = customusers.first()
                data_dict["receiver"] = customuser.receiver
                data_dict["address"] = customuser.address

            result_dict["data"] = data_dict
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))

    def post(self, request, *args, **kwargs):
        result_dict = {
            "err": 0,
            "msg": "success",
            "data": dict(),
        }
        try:
            param_dict = json.loads(request.body)
            custom_user_id = param_dict.get('custom_user_id', 0)  # 用户ID
            receiver = param_dict.get('receiver', "")  # 收货人
            address = param_dict.get('address', "")  # 收货地址

            customusers = CustomUser.objects.filter(id=custom_user_id)
            data_dict = dict()
            if customusers.exists():
                customuser = customusers.first()
                customuser.receiver = receiver
                customuser.address = address
                customuser.save()

                data_dict["receiver"] = customuser.receiver
                data_dict["address"] = customuser.address
            else:
                result_dict["msg"] = "找不到对应用户"
            result_dict["data"] = data_dict
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
