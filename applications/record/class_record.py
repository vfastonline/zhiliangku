#!encoding:utf-8
from django.db.models import Sum
from rest_framework import status
from rest_framework.views import APIView

from applications.custom_user.models import *
from applications.exercise.models import UserExercise
from applications.record.models import WatchRecord
from backstage.home.models import *
from lib.api_response_handler import JsonResponse
from lib.permissionMixin import class_view_decorator, teacher_login_required

@class_view_decorator(teacher_login_required)
class ClassRecord(APIView):
	"""班级学习统计（视频、练习）"""

	def get(self, request, *args, **kwargs):
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		data = list()
		try:
			class_id = self.request.GET.get("class_id")  # 班级ID
			# class_id = 1
			today_date = get_day_of_day(0)  # 今日日期
			project_id = self.request.GET.get("project_id")
			course_id = self.request.GET.get("course_id")
			# project_id=1
			# course_id=1
			# 默认选择今日的任务项目
			if not (project_id and course_id):
				param = dict(create_time__startswith=today_date)
				learn_video_list = LearnTask.objects.filter(**param).values("video__section__course__id",
																			"video__section__course__project__id")
				project_id = learn_video_list[0]["video__section__course__project__id"]
				course_id = learn_video_list[0]["video__section__course__id"]
			if class_id:
				class_user_id = CustomUserClass.objects.filter(id=class_id).values("customuser__id")
				user_list = []
				for user_id in class_user_id:
					user_list.append(user_id["customuser__id"])

				# 视频
				param = dict(user_id__in=user_list, create_time__startswith=today_date)
				sum_video_time = WatchRecord.objects.filter(**param).aggregate(sum=Sum("total_duration")).get("sum", "")
				avg_time = sum_video_time / (len(class_user_id))
				avg_video_time = time_conversion(avg_time)
				sum_video_time = time_conversion(sum_video_time)

				# 练习
				param = dict(custom_user_id__in=user_list, current_time__startswith=today_date)
				exercise_num = UserExercise.objects.filter(**param).aggregate(sum=Sum("times")).get("sum", "")
				exercise_avg_num = exercise_num // len(class_user_id)

				# 某个项目某个课程下的视频
				param = dict(user_id__in=user_list, create_time__startswith=today_date,
							 video__section__course__id=course_id, video__section__course__project__id=project_id)
				sum_video = WatchRecord.objects.filter(**param).values("video").annotate(
					sum=Sum("total_duration")).values("sum", "video__section__course__name",
													  "video__section__course__project__name", "video__name")
				video_node = []
				for video in sum_video:
					node = video["video__section__course__project__name"] + video["video__section__course__name"] + \
						   video["video__name"]
					times = time_conversion(video["sum"])
					video = {"node": node, "times": times}
					video_node.append(video)

				# 某个项目某个课程下的练习
				param = dict(custom_user_id__in=user_list, current_time__startswith=today_date,
							 video__section__course__id=course_id, video__section__course__project__id=project_id)
				sum_exercise = UserExercise.objects.filter(**param).values("video").annotate(sum=Sum("times")).values(
					"sum", "video__section__course__name", "video__section__course__project__name", "video__name")

				exercise_node = []
				for exercises in sum_exercise:
					node = exercises["video__section__course__project__name"] + exercises[
						"video__section__course__name"] + exercises[
							   "video__name"]
					exercise = {"node": node, "num": exercises["sum"]}
					exercise_node.append(exercise)

				data = {
					"sum_video_time": sum_video_time,  # 总视频时间
					"avg_video_time": avg_video_time,  # 平均视频时间
					"exercise_num": exercise_num,  # 练习次数
					"exercise_avg_num": exercise_avg_num,  # 平均练习次数
					# 选择项目下的视频
					"video_node": video_node,  # 视频节点
					"exercise_node": exercise_node  # 练习节点
				}
		except:

			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_500_INTERNAL_SERVER_ERROR
			msg = traceback.format_exc()

		finally:
			return JsonResponse(data=data, err=err, msg=msg)
