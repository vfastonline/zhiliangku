#!encoding:utf-8
from django.shortcuts import render
from django.views.generic import View

from lib.permissionMixin import class_view_decorator, teacher_login_required


@class_view_decorator(teacher_login_required)
class BackStageHomePage(View):
	"""教师端-后台-首页"""

	def get(self, request, *args, **kwargs):
		template_name = "backstage/index/index.html"
		return render(request, template_name, {})
