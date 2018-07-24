#!encoding:utf-8

from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.views import APIView

from lib.permissionMixin import class_view_decorator, teacher_login_required


@class_view_decorator(teacher_login_required)
class ExamStatisticsPage(APIView):
	"""考试统计"""

	def get(self, request, *args, **kwargs):
		return Response(template_name="exam/statistics/index.html")


@class_view_decorator(teacher_login_required)
class ExamGradeEntryPage(APIView):
	"""录入成绩"""

	def get(self, request, *args, **kwargs):
		return Response(template_name="exam/grade/entry/index.html")


@class_view_decorator(teacher_login_required)
class ExamDetailPage(APIView):
	"""考试详情"""

	def get(self, request, *args, **kwargs):
		return Response(template_name="exam/detail/index.html")


@class_view_decorator(teacher_login_required)
class ExamReportPage(APIView):
	"""考试报表"""

	def get(self, request, *args, **kwargs):
		# template_name = "exam/detail/index.html"
		# return render(request, template_name, {})
		return Response(template_name="exam/report/index.html")
