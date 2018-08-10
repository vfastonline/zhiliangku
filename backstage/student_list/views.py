#!encoding:utf-8
import datetime
from django.db.models import Sum
from rest_framework import status
from rest_framework.views import APIView

from applications.record.models import *
from applications.tracks_learning.models import *
from lib.api_response_handler import *


from lib.permissionMixin import class_view_decorator, teacher_login_required



@class_view_decorator(teacher_login_required)
class StudentList(APIView):
	"""
	查询学员列表信息
	"""

	def get(self, request, *args, **kwargs):
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		data = list()
		paginator = dict()
		try:
			name = self.request.GET.get("name", "")  # 姓名
			page = self.request.GET.get("page", 1)  # 页码
			per_page = self.request.GET.get("per_page", 10)  # 每页显示条目数

			param = dict(nickname__icontains=name)
			param = get_kwargs(param)
			user_list = CustomUser.objects.filter(**param)

			# 提供分页数据
			if not page: page = 1
			if not per_page: page = 10
			page_obj = Paginator(user_list, per_page)
			total_count = page_obj.count  # 记录总数
			num_pages = page_obj.num_pages  # 总页数
			page_range = list(page_obj.page_range)  # 页码列表
			paginator = {
				"total_count": total_count,
				"num_pages": num_pages,
				"page_range": page_range,
				"page": page,
				"per_page": per_page
			}

			try:
				user_list = page_obj.page(page).object_list
			except:
				user_list = list()

			data_list = []
			for user in user_list:
				watchrecords = WatchRecord.objects.filter(user=user).order_by('-create_time')
				if watchrecords.exists():
					# 秒转时分秒
					total_duration_seconds = watchrecords.annotate(sum=Sum("video_process")).values("sum")
					total_duration_seconds = (list(total_duration_seconds))[0]["sum"]
					m, s = divmod(total_duration_seconds, 60)
					h, m = divmod(m, 60)
					total_duration_seconds = ("%02d:%02d:%02d" % (h, m, s))

					watchrecord = watchrecords.first()
					create_time = watchrecord.create_time.strftime("%Y-%m-%d %H:%M:%S")
					progress = (watchrecord.video_process) / (watchrecord.duration) * 100

					result = {
						"nickname": watchrecord.user.nickname,  # 姓名
						"project": watchrecord.course.project.name,  # 项目
						"course": watchrecord.course.name,  # 课程
						"section": watchrecord.video.section.title,  # 章节
						"video": watchrecord.video.name,  # 视频
						"progress": "%d%%" % progress,  # 进度
						"sum_progress": 11,  # 总进度
						"total_duration_seconds": total_duration_seconds,  # 累计观看时间
						"create_time": create_time  # 最新登录时间
					}
					data_list.append(result)
			data = data_list
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_500_INTERNAL_SERVER_ERROR
			msg = traceback.format_exc()
		finally:
			return JsonResponse(data=data, err=err, msg=msg, paginator=paginator)


@class_view_decorator(teacher_login_required)
class StudentInfo(APIView):
	"""
	学员基本信息+当前学习节点
	"""

	def get(self, request, *args, **kwargs):
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		data = list()

		try:
			name = self.request.GET.get("name", "")  # 姓名
			if name:
				param = dict(nickname__icontains=name)
				param = get_kwargs(param)
				user_list = CustomUser.objects.filter(**param)
				data_list = []
				for user in user_list:
					watchrecords = WatchRecord.objects.filter(user=user).order_by('-create_time')

					if watchrecords.exists():
						# 秒转时分秒
						total_duration_seconds = watchrecords.annotate(sum=Sum("video_process")).values("sum")
						total_duration_seconds = (list(total_duration_seconds))[0]["sum"]
						m, s = divmod(total_duration_seconds, 60)
						h, m = divmod(m, 60)
						total_duration_seconds = ("%02d:%02d:%02d" % (h, m, s))

						watchrecord = watchrecords.first()
						create_time = watchrecord.create_time.strftime("%Y-%m-%d %H:%M:%S")
						progress = (watchrecord.video_process) / (watchrecord.duration) * 100

						result = {
							"nickname": watchrecord.user.nickname,  # 姓名
							"project": watchrecord.course.project.name,  # 项目
							"course": watchrecord.course.name,  # 课程
							"section": watchrecord.video.section.title,  # 章节
							"video": watchrecord.video.name,  # 视频
							"progress": "%d%%" % progress,  # 进度
							"sum_progress": 11,  # 总进度
							"total_duration_seconds": total_duration_seconds,  # 累计观看时间
							"create_time": create_time,  # 最新登录时间
							"xx": 0,  # 累计练习时间
							"ss": 0,  # 累计考核时间

							"sex": watchrecord.user.get_sex_display(),  # 姓别
							"institutions": watchrecord.user.institutions,  # 院校
							"birthday": watchrecord.user.birthday,  # 生日
							"is_graduate": watchrecord.user.is_graduate,  # 在校情况
							"education": watchrecord.user.education,  # 学历
							"is_computer": watchrecord.user.is_computer  # 是否计算机专业
						}

					else:
						result = {
							"nickname": user.nickname,  # 姓名
							"sex": user.get_sex_display(),  # 姓别
							"institutions": user.institutions,  # 院校
							"birthday": user.birthday,  # 生日
							"is_graduate": user.is_graduate,  # 在校情况
							"education": user.education,  # 学历
							"is_computer": user.is_computer  # 是否计算机专业
						}
					data_list.append(result)
				data = data_list
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_500_INTERNAL_SERVER_ERROR
			msg = traceback.format_exc()

		finally:
			return JsonResponse(data=data, err=err, msg=msg)


class DateRangeInfo(APIView):
	"""
	日期区间信息
	"""

	def get(self, request, *args, **kwargs):
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		data = list()

		try:
			name=self.request.GET.get("name","")
			date=self.request.GET.get("date","")
			start_date="2018-08-07"
			end_date="2018-08-08"
			if name:
				param = dict(nickname__icontains=name)
				param = get_kwargs(param)
				user_list = CustomUser.objects.filter(**param)
				data_list = []
				for user in user_list:
					print("user",user)
					watchrecords = WatchRecord.objects.filter(user=user, create_time__range=[start_date,end_date])
					print("wa",watchrecords)




		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_500_INTERNAL_SERVER_ERROR
			msg = traceback.format_exc()

		finally:
			return JsonResponse(data=data, err=err, msg=msg)









class LearningTime(APIView):
	"""
	时间分布
	"""

	def get(self, request, *args, **kwargs):
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		data = list()
		try:
			name = self.request.GET.get("name", "")  # 姓名
			date = "2018-08-09"  # self.request.GET.get("date", "")  # 日期
			param = dict(nickname__icontains=name)
			param = get_kwargs(param)
			user_list = CustomUser.objects.filter(**param)

			data_list = []
			for user in user_list:
				watchrecords = WatchRecord.objects.filter(user=user, create_time__startswith=date)
				if watchrecords.exists():
					sum_video_process = 0
					for watchrecord in watchrecords:
						video_process = watchrecord.video_process
						sum_video_process += video_process  # 多个视频

					m, s = divmod(sum_video_process, 60)
					h, m = divmod(m, 60)
					video_process = ("%02d:%02d:%02d" % (h, m, s))  # 视频时间

					result = {
						"video_process": video_process,  # 视频时间
						"xtime": 0,  # 考核时间
						"ytime": 0,  # 练习时间
						"sumtime": 0,  # 总时间
					}
					data_list.append(result)
			data = data_list

		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_500_INTERNAL_SERVER_ERROR
			msg = traceback.format_exc()

		finally:
			return JsonResponse(data=data, err=err, msg=msg)


class LearningVideo(APIView):
	"""
	视频分布
	"""

