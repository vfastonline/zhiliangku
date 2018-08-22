#!encoding:utf-8
from django.db.models import F, Sum
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.views import APIView

from applications.exercise.models import UserExercise
from applications.record.models import WatchRecord
from applications.tracks_learning.models import *
from lib.api_response_handler import JsonResponse
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int


@class_view_decorator(user_login_required)
class ClassRecord(APIView):
	"""班级学习统计（视频、练习）"""

	def get(self, request, *args, **kwargs):
		err = 0
		msg = "success"
		data = dict(total_video_time=0, avg_study_time=0, total_exercise_time=0, avg_exercise_time=0)
		try:
			class_id = request.GET.get("class_id")  # 班级ID
			total_student = CustomUser.objects.filter(class_s__id=class_id, role=0).count()  # 查询班级对应学生
			total_video_time = WatchRecord.objects.filter(total_student).aggregate(sum=Sum("total_duration"))  # 视频时间
			if total_video_time:
				m, s = divmod(total_video_time, 60)
				total_video_time = "%02d:%02d" % (m, s)
			avg_study_time = total_video_time / total_student  # 平均学习时间

			total_exercise_time = UserExercise.objects.filter(custom_user__class_s__id=class_id,
															  is_pass=True).count()  # 练习完成总次数
			# 人均练习时间

			data = {
				"total_video_time": total_video_time,
				"avg_study_time": avg_study_time,
				"total_exercise_time": total_exercise_time,
				# "avg_exercise_time": avg_exercise_time,
			}
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = 1
			msg = traceback.format_exc()
		finally:
			return JsonResponse(data=data, err=err, msg=msg)
