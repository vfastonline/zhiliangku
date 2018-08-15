
#!encoding:utf-8

from rest_framework import status
from rest_framework.views import APIView

from applications.record.models import *
from backstage.exam_statistics.models import *
from backstage.home.models import *
from lib.api_response_handler import *
from lib.permissionMixin import class_view_decorator, teacher_login_required
from online_status.models import *


def time(time):
	m, s = divmod(time, 60)
	h, m = divmod(m, 60)
	new_time = ("%02d:%02d:%02d" % (h, m, s))  # 视频时间
	return new_time


@class_view_decorator(teacher_login_required)
class LearnTime(APIView):
	"""
	时间分布
	"""

	def get(self, request, *args, **kwargs):
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		data = list()
		try:
			name = self.request.GET.get("name", "")  # 姓名=========================================
			date = "2018-08-13"  # self.request.GET.get("date", "")  # 日期
			param = dict(nickname__icontains=name)
			param = get_kwargs(param)
			user_list = CustomUser.objects.filter(**param)

			data_list = []
			for user in user_list:

				watchrecords = WatchRecord.objects.filter(user=user, create_time__startswith=date)

				exercisesrecords = WatchRecord.objects.filter(user=user, video__type=2, create_time__startswith=date)
				assessrecords = WatchRecord.objects.filter(user=user, video__type=3, create_time__startswith=date)
				sum_video_process = 0
				sum_video_exercises = 0
				sum_video_assess = 0

				# 视频时间
				if watchrecords.exists():
					for watchrecord in watchrecords:
						video_process = watchrecord.video_process
						sum_video_process += video_process

				# 练习时间
				if exercisesrecords.exists():
					for exercisesrecord in exercisesrecords:
						video_exercises = exercisesrecord.video_process
						sum_video_exercises += video_exercises

				# 考核时间
				if assessrecords.exists():
					for assessrecord in assessrecords:
						video_assess = assessrecord.video_process
						sum_video_assess += video_assess

				# 总时间
				sum_time = sum_video_process + sum_video_exercises + sum_video_assess

				result = {
					"sum_video_process": time(sum_video_process),  # 视频时间
					"sum_video_exercises": time(sum_video_exercises),  # 考核时间
					"sum_video_assess": time(sum_video_assess),  # 练习时间
					"sum_time": time(sum_time),  # 总时间
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
