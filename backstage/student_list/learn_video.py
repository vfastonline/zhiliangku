#!encoding:utf-8

from django.db.models import Sum
from rest_framework import status
from rest_framework.views import APIView

from applications.record.models import *
from backstage.exam_statistics.models import *
from backstage.home.models import *
from lib.api_response_handler import *
from lib.permissionMixin import class_view_decorator, teacher_login_required
from online_status.models import *


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
			name = self.request.GET.get("name", "")
			date = "2018-08-13"  # self.request.GET.get("date", "")  # 日期
			param = dict(nickname__icontains=name)
			param = get_kwargs(param)
			user_list = CustomUser.objects.filter(**param)

			data_list = []
			for user in user_list:
				# 视频时间
				video_record = WatchRecord.objects.filter(user=user, create_time__startswith=date, video__type=1)

				video_list = video_record.values("course").annotate(video_time=Sum("video_process")).values(
					"video_time", "video__name", "course__name", "course__project__name", "video__section__title")

				# 练习时间
				exercise_record = WatchRecord.objects.filter(user=user, create_time__startswith=date, video__type=2)
				values_list = ["exercise_time", "video__name", "course__name", "course__project__name", "video__section__title"]
				exercise_list = exercise_record.values("course").annotate(exercise_time=Sum("video_process")).values(*values_list)

				for video in video_list:

					exercise_time = 0
					for exercise in exercise_list:

						if exercise["video__name"] in video.values():
							exercise_time = exercise["exercise_time"]

					result = {

						"project": video["course__project__name"],  # 项目
						"course": video["course__name"],  # 课程
						"section": video["video__section__title"],  # 章节
						"video": video["video__name"],  # 视频
						"video_time": video["video_time"],  # 视频时间
						"exercise_time": exercise_time,  # 练习时间

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