#!encoding:utf-8

from django.db.models import F, Sum
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.views import APIView

from applications.exercise.models import UserExercise
from applications.record.models import WatchRecord
from applications.tracks_learning.models import *
from backstage.home.models import LearnTask
from lib.api_response_handler import JsonResponse
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int


@class_view_decorator(user_login_required)
class ClassCountRecord(View):
	"""视频统计详情页(视频、练习)"""

	def get(self, request, *args, **kwargs):
		err = 0
		msg = "success"
		data = dict(class_id=0,total_duration=0,total_pass_times=0,total_unpass_times=0,total_times=0)
		try:
			class_id = request.GET.get("class_id")  # 班级ID
			video_id = request.GET.get("video_id")  # 视频ID
			user_id = request.GET.get("user_id") #  用户id
			today_date = get_day_of_day(0)  # 今日日期

			param = dict()
			# 查询项目-课程-章节-视频名称
			videos_name = LearnTask.objects.values("video__section__course__project__name")

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

				result = {
					"video_node": video_node,  # 视频节点
					"sum_video_time": sum_video_time  # 视频累计时间
				}

				video_time.append(result)

			# 判断视频类型，type，1/2
			# 1:
				# 视频观看记录中查询本视频观看次数
				# 观看时长，用分组查询视频，对累积观看时长做累加
				# 查询当前班级，当前视频，分组查询，按学生分组，对累积观看时长大于时长字段的记录查询次数，除以观看次数，得到重看占比
			# 视频时间
			param = dict(user__id=user_id, create_time__startswith=today_date)
			total_video_time = WatchRecord.objects.filter(**param).aggregate(sum=Sum("total_duration")).get("sum", "")
			if total_video_time:
				m, s = divmod(total_video_time, 60)
				total_video_time = "%02d:%02d" % (m, s)



			# 2：
				# 练习记录表，查询当前班级，当前练习视频，总练习次数
				# 。。。，通过的次数
				# 总次数-通过次数=未通过次数
			total_pass_times = UserExercise.objects.filter(custom_user__class_s__id=class_id,is_pass=True).count()  # 练习完成通过次数
			total_unpass_times = UserExercise.objects.filter(custom_user__class_s__id=class_id,is_pass=False).count()  # 未通过次数
			total_times = total_pass_times+total_unpass_times  # 练习完成总次数
			data={
				"class_id":class_id,
				# "total_duration":total_duration,
				"total_pass_times":total_pass_times,
				"total_unpass_times":total_unpass_times,
				"total_times":total_times,

			}
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = 1
			msg = traceback.format_exc()
		finally:
			return JsonResponse(data=data, err=err, msg=msg)