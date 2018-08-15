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
from online_status.models import *


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
			user_id = self.request.GET.get("user_id")
			# user_id =6
			if user_id:
				user = CustomUser.objects.get(id=user_id)

				# 最后登录时间
				last_login = OnlineStatus.objects.filter(user__id=user_id).order_by("-last_login").values(
					"last_login").first()
				last_login = last_login["last_login"]

				watchrecords = WatchRecord.objects.filter(user__id=user_id).order_by('-create_time')
				print("watchrecords", watchrecords)

				if watchrecords.exists():
					# 秒转时分秒
					sum_video_time = watchrecords.aggregate(sum_time=Sum("total_duration"))
					m, s = divmod(sum_video_time["sum_time"], 60)
					h, m = divmod(m, 60)
					sum_video_time = ("%02d:%02d:%02d" % (h, m, s))

					watchrecord = watchrecords.first()
					progress = round((watchrecord.video_process) / (watchrecord.duration), 3)

					# 学习节点
					learn_node = watchrecord.course.project.name + watchrecord.course.name + watchrecord.video.section.title + watchrecord.video.name
					# 总练习次数
					sum_exercise = UserExercise.objects.filter(custom_user__id=user_id).aggregate(
						sun_times=Sum("times"))
					sum_exercise = sum_exercise["sun_times"]

					# 考核次数
					sum_assess = 0

					# 总进度
					sum_progress = 0

					result = {
						"nickname": watchrecord.user.nickname,  # 姓名
						"learn_node": learn_node,  # 学习节点
						"progress": progress,  # 进度
						"sum_progress": 0,  # 总进度
						"sum_video_time": sum_video_time,  # 累计观看时间
						"last_login": last_login,  # 最后登录时间
						"sum_exercises": sum_exercise,  # 累计练习次数
						"sum_assess": sum_assess,  # 累计考核次数

						"sex": user.get_sex_display(),  # 姓别
						"institutions": user.institutions,  # 院校
						"birthday": user.birthday,  # 生日
						"is_graduate": user.is_graduate,  # 在校情况
						"education": user.education,  # 学历
						"is_computer": user.is_computer  # 是否计算机专业
					}

					data = result

				else:
					result = {
						"nickname": user.nickname,  # 姓名
						"sex": user.get_sex_display(),  # 姓别
						"institutions": user.institutions,  # 院校
						"birthday": user.birthday,  # 生日
						"is_graduate": user.is_graduate,  # 在校情况
						"education": user.education,  # 学历
						"is_computer": user.is_computer,  # 是否计算机专业
						"last_login": last_login
					}

					data = result
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_500_INTERNAL_SERVER_ERROR
			msg = traceback.format_exc()

		finally:
			return JsonResponse(data=data, err=err, msg=msg)
