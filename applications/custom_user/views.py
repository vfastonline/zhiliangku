#!encoding:utf-8
import random
import re

from django.shortcuts import render_to_response
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
            else:
                pycrypt_obj = PyCrypt(CryptKey)
                crypt_password = pycrypt_obj.encrypt(password)
                custom_user_auth = custom_user_auths[0]
                custom_user_pwd = custom_user_auth.credential  # 密码凭证
                custom_user_id = custom_user_auth.custom_user_id.id  # 用户ID
                custom_user_role = custom_user_auth.custom_user_id.role  # 用户角色
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


class CustomUserRegister(View):
    """用户注册"""

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
                result_dict["msg"] = "已经注册过账号，请直接登录"
            else:
                create_user = CustomUser.objects.create(nickname=username, role=0)
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
                        user_auth_dict.update({"status": False})
                    create_auth = CustomUserAuths.objects.create(**user_auth_dict)

                    if create_auth:
                        # 生成token
                        token = get_validate(username, create_user.id, 0, CryptKey)
                        result_dict["err"] = 0
                        result_dict["msg"] = "success"
                        result_dict["data"]["token"] = token
                        result_dict["data"]["username"] = username

                        if is_mail:
                            send_result = self.send_activation_mail(username, create_user.id, create_auth.id)
                    else:
                        create_user.delete()
        except:
            result_dict["msg"] = traceback.format_exc()
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))

    @staticmethod
    def send_activation_mail(user_email, customer_user_id, customer_user_auth_id):
        """
        :param user_email: 用户邮箱地址
        :param customer_user_id: 用户ID
        :param customer_user_auth_id: 用户邮箱权限ID
        :return:
        """
        send_result = False
        try:
            mail_subject = "智量酷邮箱账号激活"
            mail_content = "点击此链接完成激活，"
            activation_link = "http://127.0.0.1:8000/customuser/activation?hash="
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
            "msg": "短信验证码发送失败",
            "err": 1,
            "data": {}
        }
        try:
            param_dict = json.loads(request.body)
            phone = param_dict.get("phone")
            code = "".join([str(random.randint(0, 9)) for i in xrange(4)])

            try:
                sendmessage(phone, {'code': code})
                logging.getLogger().info('验证码短信发送成功')

                code = hashlib.new('md5', code).hexdigest()

                result_dict["msg"] = "success"
                result_dict["err"] = 0
                result_dict["data"]["phone_code"] = code
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
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class ActivationCustomUserEmail(View):
    """激活邮箱类型账号"""

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
                    result_dict["err"] = 1
                    result_dict["msg"] = "待激活邮箱账户不存在"
            else:
                result_dict["err"] = 1
                result_dict["msg"] = "邮箱激活参数错误"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = '通过邮箱激活账户异常, %s' % traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


# 短信-找回密码
class RetrievePasswordByPhone(View):
    """短信找回密码"""

    def post(self, request, *args, **kwargs):
        result_dict = {
            "msg": "短信找回密码失败",
            "err": 1,
            "data": {}
        }
        try:
            param_dict = json.loads(request.body)
            phone = param_dict.get("phone")
            new_password = param_dict.get("new_password")
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
                activation_link = "http://127.0.0.1:8000/customuser/retrieve_password_by_email?hash="
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

    # 通过邮箱链接返回重置密码表单
    def get(self, request, *args, **kwargs):
        email = ""
        try:
            email_hash = request.GET.get("hash")
            pycrypt_obj = PyCrypt(CryptKey)
            email = pycrypt_obj.decrypt(email_hash)
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
        finally:
            return render_to_response('email_retrieve_password_form.html', {'email': email})

    def post(self, request, *args, **kwargs):
        result_dict = {
            "msg": "短信找回密码失败",
            "err": 1,
            "data": {}
        }
        try:
            param_dict = json.loads(request.body)
            email = param_dict.get("email")
            new_password = param_dict.get("new_password")
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
