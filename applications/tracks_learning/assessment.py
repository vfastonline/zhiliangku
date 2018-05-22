#!encoding:utf-8

from django.shortcuts import render
from django.views.generic import View

from lib.permissionMixin import class_view_decorator, user_login_required


@class_view_decorator(user_login_required)
class AssessmentDetail(View):
	"""视频考核详情--页面"""

	def get(self, request, *args, **kwargs):
		template_name = "tracks/video/assessment/detail/index.html"
		return render(request, template_name, {})
