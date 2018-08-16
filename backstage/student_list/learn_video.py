#!encoding:utf-8

from django.db.models import Sum
from rest_framework import status
from rest_framework.views import APIView

from applications.exercise.models import *
from applications.record.models import *
from backstage.exam_statistics.models import *
from backstage.home.models import *
from lib.api_response_handler import *
from lib.permissionMixin import class_view_decorator, teacher_login_required


@class_view_decorator(teacher_login_required)
class LearnVideo(APIView):
	"""
	视频分布
	"""

	def get(self, request, *args, **kwargs):
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		data = list()
		try:
			user_id = self.request.GET.get("user_id")
			# user_id = 6
			today_date = get_day_of_day(0)  # 今日日期

			if user_id:

				# 视频时间
				param = dict(user__id=user_id, create_time__startswith=today_date)
				video_list = WatchRecord.objects.filter(**param).order_by("video__id").values("video").annotate(
					sum=Sum("total_duration")).values(
					"sum", "video__name", "video__section__title", "video__section__course__name",
					"video__section__course__project__name")

				video_time = []
				for video in video_list:
					video_node = video["video__section__course__project__name"] + video[
						"video__section__course__name"] + video["video__section__title"] + video["video__name"]
					sum_video_time = video["sum"]
					print(video_node, sum_video_time)

					result = {
						"video_node": video_node,  # 视频节点
						"sum_video_time": sum_video_time  # 视频累计时间
					}

					video_time.append(result)

				# 练习次数
				exercise_list = UserExercise.objects.filter(custom_user__id=user_id).order_by("video__id").annotate(
					sum_times=Sum("times")).values(
					"sum_times", "video__name", "video__section__title", "video__section__course__name",
					"video__section__course__project__name")

				exercise_times = []
				for exercise in exercise_list:
					exercise_node = exercise["video__section__course__project__name"] + exercise[
						"video__section__course__name"] + exercise["video__section__title"] + exercise["video__name"]
					sum_times = exercise["sum_times"]

					result = {
						"exercise_node": exercise_node,  # 练习视频节点
						"sum_times": sum_times,  # 练习次数
					}
					exercise_times.append(result)
				data = {"video_time": video_time, "exercise_times": exercise_times}
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_500_INTERNAL_SERVER_ERROR
			msg = traceback.format_exc()

		finally:
			return JsonResponse(data=data, err=err, msg=msg)
