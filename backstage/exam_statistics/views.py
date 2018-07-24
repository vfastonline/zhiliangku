#!encoding:utf-8

import logging
import traceback

from django.db.models import Count
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from backstage.exam_statistics.models import *


class ExamsCountByNatureView(APIView):
	"""查询各考试性质个数"""

	def get(self, request, *args, **kwargs):
		result_dict = {
			"err": 0,
			"msg": "success",
			"data": {
				"1": 0,
				"2": 0,
				"3": 0,
				"4": 0,
				"5": 0,
			},
		}
		try:
			# 根据考试性质返回考试次数字典列表
			examnaturecounts = ExamNatureCount.objects.filter().values("nature", "count")

			# 组装接口返回值
			result_dict["data"] = examnaturecounts
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			render = JSONRenderer().render(result_dict)
			return Response(render)


class ExamsView(APIView):
	"""考试"""

	# 获取考试信息
	def get(self, request, *args, **kwargs):
		result_dict = {
			"err": 0,
			"msg": "success",
			"data": [],
		}
		try:
			name = request.POST.get('name', "")  # 考试名称
			nature = request.POST.get('nature', "")  # 考试属性

			exams = Exam.objects.filter()
			for exam in exams:
				pass





		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			render = JSONRenderer().render(result_dict)
			return Response(render)

	# 添加考试
	def post(self, request, *args, **kwargs):
		result_dict = {
			"err": 0,
			"msg": "success",
			"data": {},
		}
		try:
			name = request.POST.get('name', "")  # 考试名称
			dates = request.POST.get('dates', "")  # 考试时间
			nature = request.POST.get('nature', "")  # 考试性质
			style = request.POST.get('style', "")  # 考试方式

		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			render = JSONRenderer().render(result_dict)
			return Response(render)

	# 修改考试信息
	def patch(self, request, *args, **kwargs):
		return Response('测试api')


class ExamDetailView(APIView):
	"""考试详情"""

	# 获取考试详情
	def get(self, request, *args, **kwargs):
		result_dict = {
			"err": 0,
			"msg": "success",
			"data": {},
		}
		try:
			pk = kwargs.get('pk', 0)  # 考试名称
			o = request.GET.get('o', 0)  # 排序, desc：降序  asc：升序
			order = "id"
			if o == "asc":
				order = "fraction"
			elif o == "desc":
				order = "-fraction"

			exams = Exam.objects.filter(pk=pk)
			if exams.exists():
				exam = exams.first()
				result_dict["data"] = {
					"id": exam.id,
					"name": exam.name,
					"dates": exam.dates.strftime('%Y-%m-%d'),
					"style": exam.get_style_display(),
					"nature": exam.get_nature_display(),
					"number": exam.number,
					"grades": []
				}
				grades = exam.Grades.all().order_by(order)
				if grades:
					fields = ["custom_user__nickname", "fraction", "remark"]
					grades_list = list(grades.values(*fields))
					result_dict["data"]["grades"] = grades_list

		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			render = JSONRenderer().render(result_dict)
			return Response(result_dict)
