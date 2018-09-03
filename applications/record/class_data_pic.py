#!encoding:utf-8
from django.db.models import Sum
from rest_framework import status
from rest_framework.views import APIView

from applications.custom_user.models import *
from applications.exercise.models import UserExercise
from applications.record.models import WatchRecord
from applications.tracks_learning.models import *
from lib.api_response_handler import JsonResponse
from lib.permissionMixin import class_view_decorator,teacher_login_required

@class_view_decorator(teacher_login_required)
class ClassDataGraph(APIView):
	"""今日学习数据柱状图"""

	def get(self, request, *args, **kwargs):
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		data = list()
		try:
			class_id = self.request.GET.get("class_id")
			# class_id=1
			today_date = get_day_of_day(0)
			if class_id:
				class_user_id = CustomUserClass.objects.filter(id=class_id).values("customuser__id")
				user_list = []
				for user_id in class_user_id:
					user_list.append(user_id["customuser__id"])

				# 视频
				param = dict(user_id__in=user_list, create_time__startswith=today_date)
				sum_watch = WatchRecord.objects.filter(**param).aggregate(sum=Sum("total_duration")).get("sum", "")
				time_range = [[1200, 3000], [3001, 4200], [4201, 6600], [6601, 7800], [7801, 86400]]
				range_vide_rate = []
				for times in time_range:
					param = dict(user_id__in=user_list, create_time__startswith=today_date, total_duration__range=times)
					range_watch_num = WatchRecord.objects.filter(**param).aggregate(sum=Sum("total_duration")).get(
						"sum", "")
					if not range_watch_num:
						range_watch_num = 0
					watch_rate = round(range_watch_num / sum_watch, 2)
					range_vide_rate.append(watch_rate)

				# 练习
				param = dict(custom_user_id__in=user_list, current_time__startswith=today_date)
				sum_exercise = UserExercise.objects.filter(**param).aggregate(sum=Sum("times")).get("sum", "")

				exercise_range_times = [[5, 10], [11, 20], [21, 50], [51, 100]]
				exercise_range_rate = []
				for times in exercise_range_times:
					param = dict(custom_user_id__in=user_list, current_time__startswith=today_date, times__range=times)
					exercise_times = UserExercise.objects.filter(**param).aggregate(sum=Sum("times")).get("sum", "")
					if not exercise_times:
						exercise_times = 0
					exercise_rate = round(exercise_times / sum_exercise, 2)
					exercise_range_rate.append(exercise_rate)

				data = {
					"range_vide_rate": range_vide_rate,  # 区间时间视频率
					"exercise_range_rate": exercise_range_rate  # 练习次数频率
				}

		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_500_INTERNAL_SERVER_ERROR
			msg = traceback.format_exc()
		finally:
			return JsonResponse(data=data, err=err, msg=msg)

