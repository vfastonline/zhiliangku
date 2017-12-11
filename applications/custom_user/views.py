#!encoding:utf-8
import re

from django.views.generic import View

from applications.custom_user.models import *
from lib.encrypt import PyCrypt
from lib.util import *

CryptKey = "25668fbe1a5601eb"


class IsCellphone:
    """http://www.linuxeye.com/program/1760.html"""

    def __init__(self):
        self.p = re.compile(r'^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}$')

    def iscellphone(self, cellphone_number):
        res = self.p.match(cellphone_number)
        if res:
            return True
        else:
            return False


class IsMail:
    def __init__(self):
        self.p = re.compile(r'[^\._][\w\._-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$')

    def ismail(self, mail_str):
        res = self.p.match(mail_str)
        if res:
            return True
        else:
            return False


# 用户登录
class CustomUserLogin(View):
    def post(self, request, *args, **kwargs):
        result_dict = {
            "msg": "",
            "err": 1,
            "data": {}
        }
        try:
            param_dict = json.loads(request.body)
            username = param_dict.get("username")
            password = param_dict.get("password")

            is_mail = IsMail().ismail(username)
            is_cellphone = IsCellphone().iscellphone(username)

            # 权限类型
            identity_type = ""
            if is_mail:
                identity_type = "email"
            if is_cellphone:
                identity_type = "phone"

            # 校验是否有权限信息
            custom_user_auths = CustomUserAuths.objects.filter(identity_type=identity_type, identifier=username)
            if not custom_user_auths:
                result_dict["msg"] = "账号不存在"
            else:
                pycrypt_obj = PyCrypt(CryptKey)
                crypt_password = pycrypt_obj.encrypt(password)
                custom_user_auth = custom_user_auths[0]
                custom_user_pwd = custom_user_auth.credential
                custom_user_id = custom_user_auth.custom_user_id.id
                custom_user_role = custom_user_auth.custom_user_id.role
                if custom_user_pwd != crypt_password:
                    result_dict["msg"] = "密码错误"
                else:
                    token = get_validate(username, custom_user_id, custom_user_role, CryptKey)
                    result_dict["msg"] = "success"
                    result_dict["err"] = 0
                    result_dict["data"]["token"] = token
                    result_dict["data"]["username"] = username
                    result_dict["data"]["uid"] = custom_user_id
        except:
            result_dict["msg"] = traceback.format_exc()
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


# 用户注册
class CustomUserRegister(View):
    def post(self, request, *args, **kwargs):
        result_dict = {
            "msg": "Register Except",
            "err": 1,
            "data": {}
        }
        try:
            param_dict = json.loads(request.body)
            username = param_dict.get("username")
            password = param_dict.get("password")

            is_mail = IsMail().ismail(username)
            is_cellphone = IsCellphone().iscellphone(username)

            # 权限类型
            identity_type = ""
            if is_mail:
                identity_type = "email"
            if is_cellphone:
                identity_type = "phone"

            # 校验是否有权限信息
            custom_user_auths = CustomUserAuths.objects.filter(identity_type=identity_type, identifier=username)

            # 已经注册
            if custom_user_auths.exists():
                result_dict["msg"] = "已经注册过账号，直接登录"
            else:
                create_user = CustomUser.objects.create(nickname=username, role=0)
                if create_user:
                    pycrypt_obj = PyCrypt(CryptKey)
                    crypt_password = pycrypt_obj.encrypt(password)
                    user_auth_dict = {
                        "custom_user_id": create_user,
                        "identity_type": identity_type,
                        "identifier": username,
                        "credential": crypt_password,

                    }
                    create_auth = CustomUserAuths.objects.create(**user_auth_dict)
                    if create_auth:
                        # 生成token
                        token = get_validate(username, create_user.id, 0, CryptKey)
                        result_dict["err"] = 0
                        result_dict["msg"] = "success"
                        result_dict["data"]["token"] = token
                        result_dict["data"]["username"] = username
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))

# 注册验证码校验
# 邮件-找回密码
# 短信-找回密码
