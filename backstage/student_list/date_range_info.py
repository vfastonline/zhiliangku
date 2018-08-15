#!encoding:utf-8
from django.db.models import Count
from django.db.models import Sum
from rest_framework import status
from rest_framework.views import APIView

from applications.exercise.models import *
from applications.record.models import *
from backstage.exam_statistics.models import *
from backstage.home.models import *
from lib.api_response_handler import *
from online_status.models import *
from lib.permissionMixin import class_view_decorator, teacher_login_required


@class_view_decorator(teacher_login_required)
class DateRangeInfo(APIView):
	"""
	日期区间信息
	"""

	def get(self, request, *args, **kwargs):
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		data = list()

		try:
			user_id = self.request.GET.get("user_id")
			# user_id = 6
			start_date = self.request.GET.get("start_date", "")
			end_date = self.request.GET.get("end_date", "")
			# start_date = "2018-08-13 00:00:00"
			# end_date = "2018-08-19 00:00:00"

			# 总天数
			d1 = datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
			d2 = datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')
			days = (d2 - d1).days + 1
			if user_id:
				# 考勤
				param = dict(user__id=user_id, last_login__range=[start_date, end_date])
				login_list = OnlineStatus.objects.filter(**param).values("last_login")
				days_num = []
				for login in login_list:
					dt = datetime.datetime.strptime(str(login["last_login"])[0:10], "%Y-%m-%d")
					if dt not in days_num:
						days_num.append(dt)
				sum_no_login = days - len(days_num)
				no_login_rate = round(sum_no_login / days, 3)

				# 违纪
				param = dict(update_time__range=[start_date, end_date])
				sum_learn_task = LearnTask.objects.filter(**param).aggregate(sum=Count("video")).get("sum", "")

				param = dict(custom_user__id=user_id, schedule=1)
				sum_pass_learn = UserLearnTaskSummary.objects.filter(**param).aggregate(
					sum_learn=Count("schedule")).get("sum_learn", "")

				sum_no_learn = sum_learn_task - sum_pass_learn
				no_leaen_rate = round(sum_no_learn / days, 3)

				# 总项目
				param = dict(update_time__range=[start_date, end_date])
				sum_project = LearnTask.objects.filter(**param).values(
					"video__section__course__project__name").annotate(sum=Count("video")).values("sum")

				# 总视频
				sum_video = 0
				for video in sum_project:
					sum_video += video["sum"]

				videos = LearnTask.objects.filter(**param).values("video__id")
				video_list = []
				for video in videos:
					video_list.append(video["video__id"])
				# 参加的项目
				param = dict(user__id=user_id, create_time__range=[start_date, end_date], video__id__in=video_list)
				sum_learn_project = WatchRecord.objects.filter(**param).values(
					"video__section__course__project__name").annotate(sum=Count("video")).values("sum")

				# 观看的视频
				sum_learn_video = 0
				for learn_video in sum_learn_project:
					sum_learn_video += learn_video["sum"]

				# 练习次数
				param = dict(custom_user__id=user_id, video__id__in=video_list)
				sum_exercise = UserExercise.objects.filter(**param).aggregate(sum=Sum("times")).get("sum", "")

				# 通过次数
				param = dict(custom_user__id=user_id, video__id__in=video_list, is_pass=True)
				sum_pass_exercise = UserExercise.objects.filter(**param).aggregate(sum=Count("is_pass")).get("sum", "")

				# 考核数
				sum_assess = 0

				# 通过考核数
				sum_pass_assess = 0

				data = {

					"sum_no_login": sum_no_login,  # 缺勤天数
					"no_login_rate": no_login_rate,  # 缺勤率
					"sum_no_learn": sum_no_learn,  # 违纪天数
					"no_leaen_rate": no_leaen_rate,  # 违纪率
					"sum_project": len(sum_project),  # 总项目
					"sum_learn_project": len(sum_learn_project),  # 参加的项目
					"sum_video": sum_video,  # 总视频
					"sum_learn_video": sum_learn_video,  # 观看的视频
					"sum_exercise": sum_exercise,  # 练习次数
					"sum_pass_exercise": sum_pass_exercise,  # 通过的练习次数
					"sum_assess": sum_assess,  # 考核数
					"sum_pass_assess": sum_pass_assess  # 通过考核数
				}

		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_500_INTERNAL_SERVER_ERROR
			msg = traceback.format_exc()

		finally:
			return JsonResponse(data=data, err=err, msg=msg)
