#!encoding:utf-8

from django.views.generic import View

from applications.custom_user.models import *
from applications.custom_user.views import CryptKey
from applications.custom_user.views import send_activation_mail
from lib.encrypt import PyCrypt
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import *

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
            custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
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
            custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
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
        }
        try:
            param_dict = json.loads(request.body)
            custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
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
        }
        try:
            param_dict = json.loads(request.body)
            custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
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
            custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
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
            custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
            customusers = CustomUser.objects.filter(id=custom_user_id)
            data_dict = dict()

            if customusers.exists():
                customuser = customusers.first()
                data_dict["receiver"] = customuser.receiver
                data_dict["address"] = customuser.address
                data_dict["contact_number"] = customuser.contact_number

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
            custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
            receiver = param_dict.get('receiver', "")  # 收货人
            address = param_dict.get('address', "")  # 收货地址
            contact_number = param_dict.get('contact_number', "")  # 联系电话

            customusers = CustomUser.objects.filter(id=custom_user_id)
            data_dict = dict()
            if customusers.exists():
                customuser = customusers.first()
                customuser.receiver = receiver
                customuser.address = address
                customuser.contact_number = contact_number
                customuser.save()

                data_dict["receiver"] = customuser.receiver
                data_dict["address"] = customuser.address
                data_dict["contact_number"] = customuser.contact_number
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
