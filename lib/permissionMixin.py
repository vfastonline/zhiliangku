# coding=utf-8
import json
import traceback
import logging

from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator

from applications.custom_user.views import CryptKey
from util import validate
from zhiliangku.settings import LOGIN_URL
from django.core.urlresolvers import reverse


# 校验用户是否登录
def user_login_required(function):
    def _wrapped_view(request, *args, **kwargs):
        try:
            token = ""
            try:
                # token = request.GET.get("token", "")
                token = request.COOKIES.get("token")
            except:
                traceback.print_exc()
                logging.getLogger().error(traceback.format_exc())
            # if not token:
            #     try:
            #         token = eval(request.body).get("token", "")
            #     except:
            #         traceback.print_exc()
            #         logging.getLogger().error(traceback.format_exc())
            print "token==", token
            if not token:
                return HttpResponseRedirect(reverse('login', args=(request,), kwargs={'err': 2, "msg": "未登录!"}))
                # return HttpResponse(json.dumps({"err": 2, "msg": "未登录!"}, ensure_ascii=False))

            validate_result = validate(token, CryptKey)
            code = validate_result.get("code")
            msg = validate_result.get("msg")
            if code == 1:
                logging.getLogger().warning("Request forbiden:%s" % msg)
                return HttpResponseRedirect(reverse('login', args=(request,), kwargs={'err': 2, "msg": msg}))
                # return HttpResponse(json.dumps({"err": 2, "msg": msg}, ensure_ascii=False))
        except:
            logging.getLogger().warning("Validate error: %s" % traceback.format_exc())
            return HttpResponseRedirect(reverse('login', args=(request,), kwargs={'err': 1, "msg": '验证异常'}))
            # return HttpResponse(json.dumps({'err': 1, 'msg': '验证异常'}))
        return function(request, *args, **kwargs)

    return _wrapped_view


def class_view_decorator(function_decorator):
    """Convert a function based decorator into a class based decorator usable
    on class based Views.
    Can't subclass the `View` as it breaks inheritance (super in particular),
    so we monkey-patch instead.
    """

    def simple_decorator(view):
        view.dispatch = method_decorator(function_decorator)(view.dispatch)
        return view

    return simple_decorator
