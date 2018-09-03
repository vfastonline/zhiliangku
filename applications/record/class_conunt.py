#!encoding:utf-8

from django.db.models import Sum, Count
from rest_framework import status
from rest_framework.views import APIView

from applications.custom_user.models import *
from applications.exercise.models import UserExercise
from applications.record.models import WatchRecord
from applications.tracks_learning.models import *
from backstage.home.models import LearnTask
from lib.api_response_handler import JsonResponse
from lib.permissionMixin import class_view_decorator, teacher_login_required

@class_view_decorator(teacher_login_required)
class ClassCountRecord(APIView):
	"""视频统计详情页(视频、练习)"""

	def get(self, request, *args, **kwargs):
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		data = list()
		try:
			class_id = self.request.GET.get("class_id")  # 班级ID
			# class_id = 1
			today_date = get_day_of_day(0)  # 今日日期
			if class_id:
				class_user_id = CustomUserClass.objects.filter(id=class_id).values("customuser__id")
				user_list = []
				for user_id in class_user_id:
					user_list.append(user_id["customuser__id"])

				# 今日任务
				learn_video_list = LearnTask.objects.filter(create_time__startswith=today_date).values("video",
																									   "video__name",
																									   "video__section__course__name",
																									   "video__section__course__project__name")
				video_list = []
				video_node = []
				for video in learn_video_list:
					video_list.append(video["video"])
					node = video["video__section__course__name"] + video["video__section__course__project__name"] + \
						   video["video__name"]
					video_node.append(node)

				# 观看视频
				param = dict(user_id__in=user_list, create_time__startswith=today_date, video_id__in=video_list)
				watch_num = WatchRecord.objects.filter(**param)
				param = dict(user_id__in=user_list, create_time__startswith=today_date, video_id__in=video_list)
				sum_video_time = WatchRecord.objects.filter(**param).aggregate(sum=Sum("total_duration")).get("sum", "")
				if sum_video_time:
					m, s = divmod(sum_video_time, 60)
					sum_video_time = "%02d:%02d" % (m, s)

				param = dict(user_id__in=user_list, create_time__startswith=today_date, video_id__in=video_list,
							 total_duration__gt=F("duration"))
				repeat_num = WatchRecord.objects.filter(**param).annotate(sum=Count("user")).values("sum")
				repeat_rate = round(len(repeat_num) / len(watch_num), 2)

				# 练习
				param = dict(custom_user_id__in=user_list, current_time__startswith=today_date,
							 video__id__in=video_list)
				exercise_num = UserExercise.objects.filter(**param).aggregate(exercise_num=Sum("times")).get(
					"exercise_num",
					"")
				param = dict(custom_user_id__in=user_list, current_time__startswith=today_date,
							 video__id__in=video_list,
							 is_pass=True)
				exercise_pass_num = UserExercise.objects.filter(**param).aggregate(pass_num=Count("is_pass")).get(
					"pass_num",
					"")
				exercise_no_num = exercise_num - exercise_pass_num
				data = {
					"video_node": video_node,  # 视频节点
					"watch_num": len(watch_num),  # 观看次数
					"sum_video_time": sum_video_time,  # 观看时间
					"repeat_rate": repeat_rate,  # 重看比率
					"exercise_num": exercise_num,  # 练习次数
					"exercise_pass_num": exercise_pass_num,  # 练习通过次数
					"exercise_no_num": exercise_no_num  # 未通过次数
				}

		except:

			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_500_INTERNAL_SERVER_ERROR
			msg = traceback.format_exc()

		finally:
			return JsonResponse(data=data, err=err, msg=msg)
