# coding=utf-8
import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator

from applications.custom_user.views import CryptKey
from util import validate


# 校验用户是否登录
def user_login_required(function):
    def _wrapped_view(request, *args, **kwargs):
        token = ""
        try:
            token = request.GET.get("token", "")
        except:
            pass
        if not token:
            try:
                token = json.load(request.body).get("token", "")
            except:
                pass

        if not token:
            return HttpResponse(json.dumps({"err": 1, "msg": "用户未登录!"}, ensure_ascii=False))

        validate_result = validate(token, CryptKey)
        code = validate_result.get("code")
        msg = validate_result.get("msg")
        if code == 1:
            return HttpResponse(json.dumps({"err": 1, "msg": msg}, ensure_ascii=False))
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
