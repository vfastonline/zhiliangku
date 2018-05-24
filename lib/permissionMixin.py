# coding=utf-8
import logging
import traceback

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse
from django.shortcuts import resolve_url
from django.utils.decorators import method_decorator

from applications.custom_user.views import CryptKey
from util import validate


# 校验用户是否登录
def user_login_required(function):
	def _wrapped_view(request, *args, **kwargs):
		path = request.get_full_path()
		try:
			token = ""
			try:
				token = request.COOKIES.get("token")
			except:
				traceback.print_exc()
				logging.getLogger().error(traceback.format_exc())

			if not token:
				resolved_login_url = resolve_url(reverse('login'))  # 未登录
				return redirect_to_login(path, resolved_login_url, REDIRECT_FIELD_NAME)

			validate_result = validate(token, CryptKey)
			code = validate_result.get("code")
			msg = validate_result.get("msg")
			if code == 1:
				logging.getLogger().warning("Request forbiden:%s" % msg)
				resolved_login_url = resolve_url(reverse('login'))  # Token校验失败
				return redirect_to_login(path, resolved_login_url, REDIRECT_FIELD_NAME)
		except:
			logging.getLogger().warning("Validate error: %s" % traceback.format_exc())
			resolved_login_url = resolve_url(reverse('login'))  # 接口异常
			return redirect_to_login(path, resolved_login_url, REDIRECT_FIELD_NAME)
		return function(request, *args, **validate_result)

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
