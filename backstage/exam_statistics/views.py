#!encoding:utf-8


from django.db.models import *
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from backstage.exam_statistics.models import *
from lib.permissionMixin import class_view_decorator, teacher_login_required
from lib.util import *


@class_view_decorator(teacher_login_required)
class ExamsCountByNatureView(APIView):
	"""查询各考试性质个数"""

	def get(self, request, *args, **kwargs):
		result_dict = {
			"err": 0,
			"msg": "success",
			"data": [],
		}
		try:
			class_id = request.GET.get("class_id")  # 班级ID

			# 根据考试性质返回考试次数字典列表
			examnaturecounts = ExamNatureCount.objects.filter(class_s__id=class_id).values("nature", "count")

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


# @class_view_decorator(teacher_login_required)
class ExamsView(APIView):
	"""考试
	获取考试
	添加考试
	修改考试
	"""

	# 获取考试
	def get(self, request, *args, **kwargs):
		result_dict = {
			"err": 0,
			"msg": "success",
			"data": [],
			"paginator": {},
		}
		try:
			class_id = request.GET.get("class_id")  # 班级ID
			name = request.GET.get('name', "")  # 考试名称，模糊查询
			nature = request.GET.get('nature', "")  # 考试属性
			start_date = request.GET.get('start_date', "")  # 考试时间段
			end_date = request.GET.get('end_date', "")  # 考试时间段
			page = request.GET.get("page", 1)  # 页码
			per_page = request.GET.get("per_page", 10)  # 每页显示条目数

			param = {
				"class_s__id": class_id,
				"name__icontains": name,
				"nature": nature,
				"dates__gte": start_date,
				"dates__lte": end_date,
			}
			filter_param = get_kwargs(param)
			exams = Exam.objects.filter(**filter_param)

			# 提供分页数据
			if not page: page = 1
			if not per_page: page = 10
			page_obj = Paginator(exams, per_page)
			total_count = page_obj.count  # 记录总数
			num_pages = page_obj.num_pages  # 总页数
			page_range = list(page_obj.page_range)  # 页码列表
			paginator_dict = {
				"total_count": total_count,
				"num_pages": num_pages,
				"page_range": page_range,
				"page": page,
				"per_page": per_page
			}
			result_dict["paginator"] = paginator_dict
			try:
				exams_list = page_obj.page(page).object_list
			except:
				exams_list = list()

			result_list = list()
			for exam in exams_list:
				one_dict = dict()
				one_dict["name"] = exam.name
				one_dict["dates"] = exam.dates.strftime('%Y-%m-%d')
				one_dict["class_s"] = exam.class_s.name if exam.class_s else ""
				one_dict["style"] = exam.get_style_display()
				one_dict["nature"] = exam.get_nature_display()
				one_dict["number"] = exam.number
				result_list.append(one_dict)

			result_dict["data"] = result_list
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			render = JSONRenderer().render(result_dict)
			return Response(result_dict)

	# 添加考试
	def post(self, request, *args, **kwargs):
		result_dict = {
			"err": 0,
			"msg": "success",
		}
		try:
			param_dict = json.loads(request.body)
			class_id = param_dict.get("class_id")  # 班级ID
			name = param_dict.get('name', "")  # 考试名称
			dates = param_dict.get('dates', "")  # 考试时间
			nature = param_dict.get('nature', "")  # 考试性质
			style = param_dict.get('style', "")  # 考试方式
			number = param_dict.get('number', 0)  # 参加人数
			create_param = {
				"class_s__id": class_id,
				"name": name,
				"dates": datetime.datetime.strptime(dates, "%Y-%m-%d"),
				"nature": nature,
				"style": style,
				"number": int(number),
			}
			exams = Exam.objects.create(**create_param)
			if not exams:
				result_dict["err"] = 1
				result_dict["msg"] = "添加考试失败"
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			render = JSONRenderer().render(result_dict)
			return Response(render)

	# 修改考试
	def patch(self, request, *args, **kwargs):
		result_dict = {
			"err": 0,
			"msg": "success",
		}
		try:
			param_dict = json.loads(request.body)
			id = param_dict.get('id', "")  # 考试ID
			name = param_dict.get('name', "")  # 考试名称
			dates = param_dict.get('dates', "")  # 考试时间
			nature = param_dict.get('nature', "")  # 考试性质
			style = param_dict.get('style', "")  # 考试方式
			number = param_dict.get('number', 0)  # 参加人数
			update_param = {
				"name": name,
				"dates": datetime.datetime.strptime(dates, "%Y-%m-%d"),
				"nature": nature,
				"style": style,
				"number": int(number),
			}
			exams = Exam.objects.filter(id=id)
			if not exams.exists():
				result_dict["err"] = 1
				result_dict["msg"] = "考试信息不存在"
			else:
				update_rows = exams.update(**update_param)
				if not update_rows:
					result_dict["err"] = 1
					result_dict["msg"] = "编辑考试信息失败"
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			render = JSONRenderer().render(result_dict)
			return Response(render)


@class_view_decorator(teacher_login_required)
class ExamDetailView(APIView):
	"""
	考试详情
	删除考试
	"""

	# 获取考试详情
	def get(self, request, *args, **kwargs):
		result_dict = {
			"err": 0,
			"msg": "success",
			"data": {},
		}
		try:
			pk = kwargs.get('pk', 0)  # 考试ID
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
			return Response(render)

	# 删除考试信息
	def delete(self, request, *args, **kwargs):
		result_dict = {
			"err": 0,
			"msg": "success",
		}
		try:
			pk = kwargs.get('pk', 0)  # 考试ID
			deleted, _rows_count = Exam.objects.filter(id=pk).delete()
			if not _rows_count:
				result_dict["err"] = 1
				result_dict["msg"] = "删除考试信息失败"
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			render = JSONRenderer().render(result_dict)
			return Response(render)


@class_view_decorator(teacher_login_required)
class ExamEntryGradeView(APIView):
	"""
	获取考试对应班级学生
	录入学生成绩
	"""

	# 获取考试对应班级的学生
	def get(self, request, *args, **kwargs):
		result_dict = {
			"err": 0,
			"msg": "success",
			"data": {},
		}
		try:
			exam_id = request.GET.get('exam_id', 0)  # 考试ID
			exams = Exam.objects.filter(id=exam_id)
			if not exams.exists():
				result_dict["err"] = 1
				result_dict["msg"] = "考试信息不存在"
			else:
				exam = exams.first()
				detail = {
					"name": exam.name,
					"dates": exam.dates.strftime('%Y-%m-%d'),
					"class_s": exam.class_s.name if exam.class_s else "",
					"style": exam.get_style_display(),
					"nature": exam.get_nature_display(),
					"number": exam.number,
					"customusers": []
				}

				# 查询班级对应学生
				customusers = CustomUser.objects.filter(class_s=exam.class_s, role=0)
				result_list = list()
				for one in customusers:
					one_dict = {"id": one.id, "nickname": one.nickname}
					result_list.append(one_dict)
				detail["customusers"] = result_list
				result_dict["data"] = detail
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			render = JSONRenderer().render(result_dict)
			return Response(render)

	# 录入成绩
	def post(self, request, *args, **kwargs):
		result_dict = {
			"err": 0,
			"msg": "success",
			"data": {},
		}
		try:
			param_dict = json.loads(request.body)
			exam_id = param_dict.get("exam_id")
			grades = param_dict.get('grades', [])  # [{"id":1, "fraction":80, "remark":"备注信息"}]

			grade_list = list()
			for one in grades:
				exam_id = exam_id
				custom_user_id = one["id"]
				fraction = one["fraction"]
				remark = one["remark"]
				grade = Grade(exam__id=exam_id, custom_user__id=custom_user_id, fraction=fraction, remark=remark)
				grade_list.append(grade)
			objs = Grade.objects.bulk_create(grade_list)
			if not objs:
				result_dict["err"] = 1
				result_dict["msg"] = "成绩录入失败！"
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			render = JSONRenderer().render(result_dict)
			return Response(render)


@class_view_decorator(teacher_login_required)
class ExamReportView(APIView):
	"""
	考核报表
	"""

	def get(self, request, *args, **kwargs):
		"""
		:param request:
		:param args:
		:param kwargs:
		:return:
			nature:{"7-12":"日考","7-8":"阶段考"}
			data:[{"7-12":"nickname":"张三","max":90,"min":20,"avg":60,"fail":5,"class_max":1,"class_min":1,"7-12":80}]
		"""
		result_dict = {
			"err": 0,
			"msg": "success",
			"data": [],
			"summarys": {},
		}
		try:
			class_id = request.GET.get("class_id")  # 班级ID
			start_date = request.GET.get('start_date', "")  # 考试时间段
			end_date = request.GET.get('end_date', "")  # 考试时间段
			param = {
				"class_s__id": class_id,
				"dates__gte": start_date,
				"dates__lte": end_date,
			}
			filter_param = get_kwargs(param)
			exams = Exam.objects.filter(**filter_param)
			date_list = list()
			for exam in exams:
				dates = exam.dates.strftime('%Y-%m-%d')
				nature = exam.get_nature_display()
				detail = dict()
				detail[dates] = nature
				detail["grade"] = exam.Grades.values("custom_user", "custom_user__nickname", "fraction")
				date_list.append(detail)

			# 按学员分组查询，所有考试总次数，最高分，最低分，平均分
			annotate_param = {
				"num_exam": Count("id"),
				"max": Max("fraction"),
				"min": Min("fraction"),
				"avg": Avg("fraction"),
			}
			custom_user_detail = Grade.objects.values("custom_user").annotate(**annotate_param)
			summarys_dict = dict()

			exam_max_dict = Grade.objects.values("exam").annotate(fraction=Max("fraction"))  # 按考试分组查询，每场考试的最高分
			exam_min_dict = Grade.objects.values("exam").annotate(fraction=Min("fraction"))  # 按考试分组查询，每场考试的最低分
			for one in custom_user_detail:
				custom_user = one.get("custom_user")

				# 按学院分组查询，每场考试不及格分数次数
				filter_param = {"custom_user__id": custom_user, "fraction__lt": 60}
				fail_dict = Grade.objects.filter(**filter_param).values("custom_user").annotate(fail=Count("id"))
				if fail_dict.exists():
					one.update({"fail": fail_dict.first().get("fail", 0)})
				else:
					one.update({"fail": 0})

				# 查询当前用户在每场考试是否拿到最高分，是class_max + 1
				class_max = 0
				for one_param in exam_max_dict:
					one_param["custom_user__id"] = custom_user

					if Grade.objects.filter(**one_param).exists():
						class_max += 1
				one.update({"class_max": class_max})

				# 查询当前用户在每场考试是否拿到最低分，是class_min + 1
				class_min = 0
				for one_param in exam_min_dict:
					one_param["custom_user__id"] = custom_user
					if Grade.objects.filter(**one_param).exists():
						class_min += 1
				one.update({"class_min": class_min})

				# 每个学生的详细统计信息
				summarys_dict[custom_user] = one

			# 日期升序
			result_dict["data"] = date_list
			result_dict["summarys"] = summarys_dict
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			render = JSONRenderer().render(result_dict)
			return Response(render)
