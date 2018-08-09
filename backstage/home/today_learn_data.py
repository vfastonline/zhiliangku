#!encoding:utf-8
import datetime
from django.db.models import *
from rest_framework import status
from rest_framework.views import APIView

from applications.record.models import WatchRecord
from lib.api_response_handler import *
from lib.base_redis import redis_db
from lib.permissionMixin import class_view_decorator, teacher_login_required
from lib.util import *


@class_view_decorator(teacher_login_required)
class GetLearnFrequency(APIView):
	"""首页-柱状图-今日-学习频率"""

	def __init__(self):
		super(GetLearnFrequency, self).__init__()
		self.data = {}.fromkeys(["5-10", "10-20", "20-50", "50+"], 0)
		self.err = status.HTTP_200_OK
		self.msg = "success"

	def get(self, request, *args, **kwargs):
		try:
			# 查询参数
			class_id = request.GET.get("class_id")  # 班级ID

			# redis，key
			today = datetime.datetime.today()
			get_date_str = today.strftime("%Y-%m-%d")
			redis_learn_frequency_key = "LearnFrequency_%s_%s" % (class_id, get_date_str)  # 缓存key

			# 取缓存
			learn_frequency = redis_db.get(redis_learn_frequency_key)
			if learn_frequency:
				self.data = eval(learn_frequency)
				return

			start_date = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)
			end_date = datetime.datetime(today.year, today.month, today.day, 23, 59, 59)
			filter_param = dict(user__class_s__id=class_id, user__role=0, create_time__range=(start_date, end_date))
			watchrecords = WatchRecord.objects.filter(**filter_param).values("user").annotate(count=Count("id"))
			for one in watchrecords:
				count = one.get("count", 0)
				if 5 <= count < 10:
					self.data["5-10"] += 1
				if 10 <= count < 20:
					self.data["10-20"] += 1
				if 20 <= count < 50:
					self.data["20-50"] += 1
				if count >= 50:
					self.data["50+"] += 1

			# 缓存1小时
			redis_db.setex(redis_learn_frequency_key, self.data, 60 * 60)
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.err = status.HTTP_500_INTERNAL_SERVER_ERROR
			self.msg = traceback.format_exc()
		finally:
			return JsonResponse(data=self.data, err=self.err, msg=self.msg)


@class_view_decorator(teacher_login_required)
class GetLearnDuration(APIView):
	"""首页-柱状图-今日-观看时长"""

	def __init__(self):
		super(GetLearnDuration, self).__init__()
		self.data = {}.fromkeys(["20-50", "50-80", "80-110", "110-130", "130+"], 0)
		self.err = status.HTTP_200_OK
		self.msg = "success"

	def get(self, request, *args, **kwargs):
		try:
			# 查询参数
			class_id = request.GET.get("class_id")  # 班级ID

			# redis，key
			today = datetime.datetime.today()
			get_date_str = today.strftime("%Y-%m-%d")
			redis_learn_duration_key = "LearnDuration_%s_%s" % (class_id, get_date_str)  # 缓存key

			# 取缓存
			learn_duration = redis_db.get(redis_learn_duration_key)
			if learn_duration:
				self.data = eval(learn_duration)
				return

			start_date = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)
			end_date = datetime.datetime(today.year, today.month, today.day, 23, 59, 59)
			filter_param = dict(user__class_s__id=class_id, user__role=0, create_time__range=(start_date, end_date))
			watchrecords = WatchRecord.objects.filter(**filter_param).values("user").annotate(Sum("total_duration"))
			for one in watchrecords:
				total_duration__sum = one.get("total_duration__sum", 0)
				m, s = divmod(total_duration__sum, 60)
				if 20 <= m < 50:
					self.data["20-50"] += 1
				if 50 <= m < 80:
					self.data["50-80"] += 1
				if 80 <= m < 110:
					self.data["80-110"] += 1
				if 110 <= m < 130:
					self.data["110-130"] += 1
				if m >= 130:
					self.data["130+"] += 1

			# 缓存1小时
			redis_db.setex(redis_learn_duration_key, self.data, 60 * 60)
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.err = status.HTTP_500_INTERNAL_SERVER_ERROR
			self.msg = traceback.format_exc()
		finally:
			return JsonResponse(data=self.data, err=self.err, msg=self.msg)
