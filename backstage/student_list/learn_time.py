# !encoding:utf-8
from django.db.models import Sum
from rest_framework import status
from rest_framework.views import APIView

from applications.exercise.models import *
from applications.record.models import *
from applications.tracks_learning.models import *
from backstage.exam_statistics.models import *
from backstage.home.models import *
from lib.api_response_handler import *
from lib.permissionMixin import class_view_decorator, teacher_login_required


@class_view_decorator(teacher_login_required)
class LearnTime(APIView):
	"""
	时间分布
	"""

	def get(self, request, *args, **kwargs):
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		data = dict()
		try:
			user_id = self.request.GET.get("user_id")
			# user_id=6
			today_date = get_day_of_day(0)  # 今日日期

			# 视频时间
			param = dict(user__id=user_id, create_time__startswith=today_date)
			total_video_time = WatchRecord.objects.filter(**param).aggregate(sum=Sum("total_duration")).get("sum","")
			if total_video_time:
				m, s = divmod(total_video_time, 60)
				total_video_time = "%02d:%02d" % (m, s)

			# 练习次数
			param = dict(custom_user__id=user_id)
			sum_exercise = UserExercise.objects.filter(**param).aggregate(sum=Sum("times")).get("sum", "")

			# 考核次数
			param = dict(custom_user__id=user_id,update_time__startswith=today_date)
			sum_unlock = UnlockVideo.objects.filter(**param).aggregate(sum=Sum("times")).get("sum", "")

			data = {
				"total_video_time": total_video_time,  # 视频时间
				"sum_exercise": sum_exercise,  # 练习次数
				"sum_unlock": sum_unlock  # 考核次数
			}

		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_500_INTERNAL_SERVER_ERROR
			msg = traceback.format_exc()

		finally:
			return JsonResponse(data=data, err=err, msg=msg)
