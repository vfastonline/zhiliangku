#!encoding:utf-8
import json

from django.db.models import F
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
class HandleWatchRecord(View):
	"""增加视频的观看记录"""

	def post(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success"}
		try:
			param_dict = json.loads(request.body)
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			course_id = str_to_int(param_dict.get('course_id', 0))  # 必填，课程ID
			video_id = str_to_int(param_dict.get('video_id', 0))  # 必填，视频ID
			real_play_video_time = str_to_int(param_dict.get('real_play_video_time', 0))  # 当前已观看时长（不包含视频缓冲时间）,秒
			total_duration = str_to_int(param_dict.get('total_duration', 0))  # 累计观看时长，秒
			duration = str_to_int(param_dict.get('duration', 0))  # 视频总时长，秒
			status = str_to_int(param_dict.get('status', 0))  # 1：已看完；0：未看完

			# 查询是否有观看记录
			watchrecords = WatchRecord.objects.filter(user__id=custom_user_id, video__id=video_id, course__id=course_id)
			if watchrecords.exists():
				update_dict = {
					"video_process": real_play_video_time,
					"duration": duration,
					"status": status,
					"total_duration": F('total_duration') + total_duration,
				}
				rows = watchrecords.update(**update_dict)
				if not rows:
					result_dict["err"] = 1
					result_dict["msg"] = "更新用户观看记录失败"
					return
			else:
				# 用户
				user = None
				users = CustomUser.objects.filter(id=custom_user_id)
				if users.exists():
					user = users.first()
				if not user:
					result_dict["err"] = 1
					result_dict["msg"] = "观看用户不存在"
					return

				# 课程
				course = None
				courses = Course.objects.filter(id=course_id)
				if courses.exists():
					course = courses.first()
				if not course:
					result_dict["err"] = 1
					result_dict["msg"] = "课程不存在"
					return

				# 视频
				video = None
				videos = Video.objects.filter(id=video_id)
				if videos.exists():
					video = videos.first()
				if not video:
					result_dict["err"] = 1
					result_dict["msg"] = "视频不存在"
					return

				create_dict = {
					"user": user,
					"video": video,
					"course": course,
					"video_process": real_play_video_time,
					"duration": duration,
					"total_duration": total_duration,
				}
				add_obj = WatchRecord.objects.create(**create_dict)
				if not add_obj:
					result_dict["err"] = 1
					result_dict["msg"] = "添加视频观看记录失败"
					return
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class ClassRecord(APIView):
	"""班级学习统计（视频、练习）"""

	def get(self, request, *args, **kwargs):
		err = 0
		msg = "success"
		data = dict(class_id=0, video_id=0, total_class=0,total_duration=0, avg_duration=0, total_times=0)
		try:
			class_id = request.GET.get("class_id")  # 班级ID

			# 学习总时长
			# 通过班级ID查询班级下所有学生视频观看记录累积观看时长总和，用聚合查询，换算成时分秒
			# 总时长/班级总人数=人均学习时长


			video_id = str_to_int(request.get('video_id', 0))  # 视频ID
			total_duration = str_to_int(request.get('total_dura tion', 0))  # 累计观看时长，秒  显示*小时*分钟
			total_class = CustomUser.objects.filter(class_s__id=class_id, role=0).count()  # 查询班级对应学生
			avg_duration = total_duration / total_class  # 平均观看分钟时长 需要将班级总时长/班级总人数

			total_times = UserExercise.objects.filter(custom_user__class_s__id=class_id, is_pass=True).count()  # 练习完成总次数
			# TODO 存疑 人均学习时间

			data = {
				"class_id": class_id,
				"video_id": video_id,
				"total_duration": total_duration,
				"avg_duration": avg_duration,
				"total_times": total_times
			}
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = 1
			msg = traceback.format_exc()
		finally:
			return JsonResponse(data=data, err=err, msg=msg)


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
			# 视频ID
			# 查询项目-课程-章节-视频名称
			# 判断视频类型，type，1/2
			# 1:
				# 视频观看记录中查询本视频观看次数
				# 观看时长，用分组查询视频，对累积观看时长做累加
				# 查询当前班级，当前视频，分组查询，按学生分组，对累积观看时长大于时长字段的记录查询次数，除以关安次数，得到重看占比
			# 2：
				# 练习记录表，查询当前班级，当前练习视频，总练习次数
				# 。。。，通过的次数
				# 总次数-通过次数=未通过次数


			# TODO 少数据
			#  观看次数
			#  重看占比

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