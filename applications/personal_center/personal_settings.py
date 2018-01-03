#!encoding:utf-8
import json

from django.http import HttpResponse
from django.views.generic import View

from applications.custom_user.models import *
from lib.permissionMixin import class_view_decorator, user_login_required

"""个人设置"""


# @class_view_decorator(user_login_required)
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
            custom_user_id = int(param_dict.get('custom_user_id', 0))  # 必填，用户ID
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


# @class_view_decorator(user_login_required)
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


# @class_view_decorator(user_login_required)
# class AccountBindEmail(View):
#     """账号绑定--邮箱"""
#
#     def post(self, request, *args, **kwargs):
#         result_dict = {
#             "err": 0,
#             "msg": "success",
#             "data": dict(),
#         }
#         try:
#             param_dict = json.loads(request.body)
#             custom_user_id = int(param_dict.get('custom_user_id', 0))  # 必填，用户ID
#             nickname = param_dict.get('nickname', "")  # 必填，昵称
#             sex = param_dict.get('sex')  # 必填，性别
#             signature = param_dict.get('signature', "")  # 个性签名
#
#             customusers = CustomUser.objects.filter(id=custom_user_id)
#             data_dict = dict()
#             if customusers.exists():
#                 customuser = customusers.first()
#                 customuser.nickname = nickname
#                 customuser.signature = signature
#                 customuser.sex = sex
#                 customuser.save()
#
#                 data_dict["nickname"] = customuser.nickname
#                 data_dict["signature"] = customuser.signature if customuser.signature else ""
#                 data_dict["sex"] = customuser.get_sex_display()
#             else:
#                 result_dict["msg"] = "找不到对应用户"
#             result_dict["data"] = data_dict
#         except:
#             traceback.print_exc()
#             logging.getLogger().error(traceback.format_exc())
#             result_dict["err"] = 1
#             result_dict["msg"] = traceback.format_exc()
#         finally:
#             return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


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
