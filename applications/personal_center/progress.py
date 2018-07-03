#!encoding:utf-8
import datetime
from django.db.models import Count
from django.db.models import Sum
from django.views.generic import View

from applications.record.models import WatchRecord
from applications.tracks_learning.models import Video, UnlockVideo
from applications.tracks_learning.projects_list import project_summarize_course_progress
from applications.exercise.models import UserExercise
from backstage.home.models import LearnTask
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import *


@class_view_decorator(user_login_required)
class GetLearningProgressInfo(View):
	"""个人中心-学习进度-信息"""

	def __init__(self):
		super(GetLearningProgressInfo, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": list(),
		}

	def get(self, request, *args, **kwargs):
		try:
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID

			# 对用户观看记录以项目信息分组查询
			watchrecords = WatchRecord.objects.filter(user__id=custom_user_id).values("course__project").annotate(
				Count('id'))
			time_line_dict = dict()
			for one in watchrecords:
				project_id = one.get("course__project")

				# 查询用户指定项目最近一次学习记录
				filter_param = {
					"user__id": custom_user_id,
					"course__project__id": project_id,
				}
				record = WatchRecord.objects.filter(**filter_param).order_by("-create_time").first()
				create_time = record.create_time.strftime('%Y-%m-%d %H:%M:%S')  # 最近一次项目学习记录时间

				# 项目详细信息
				detail = dict()
				detail["name"] = record.course.project.name
				detail["pathwel"] = record.course.project.pathwel.url if record.course.project.pathwel else ""

				courses = record.course.project.Courses.all()  # 项目下所有课程
				courses_count = courses.count()  # 课程数
				courses_schedule = 0
				for course in courses:
					# 汇总用户每个课程完成百分比
					summarize_param = [custom_user_id, course, list(courses)]
					summarize_dict = project_summarize_course_progress(*summarize_param)
					unlock = summarize_dict.get("unlock")

					# 课程未解锁，跳出汇总
					if not unlock:
						break
					courses_schedule += summarize_dict.get("schedule")
					learn_video_id = summarize_dict.get("learn_video_id")
					if learn_video_id:
						detail["learn_video_id"] = learn_video_id
						detail["learn_course_id"] = summarize_dict.get("learn_course_id")
						detail["video_process"] = summarize_dict.get("video_process")
						detail["learn_video_type"] = summarize_dict.get("learn_video_type")
						detail["learn_video_name"] = summarize_dict.get("learn_video_name")
						detail["learning"] = summarize_dict.get("learning")

				# 项目完成百分比
				detail["schedule"] = float(courses_schedule) / float(courses_count)
				time_line_dict[create_time] = detail

			# 对时间轴排序，观看时间倒序
			data_list = list()
			for i in sorted(time_line_dict.items(), key=lambda e: e[0], reverse=True):
				data_list.append({i[0]: i[1]})
			self.result_dict["data"] = data_list
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class GetLearnTaskInfo(View):
	"""个人中心-今日任务-信息"""

	def __init__(self):
		super(GetLearnTaskInfo, self).__init__()
		self.custom_user_id = 0
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": {
				"task": "",  # 任务目标，项目名称-课程名称-视频名称
				"video_1": "",  # 视频时长，分钟
				"video_2": 0,  # 练习题个数
				"video_3": 0,  # 考核个数
				"video_1_time": 0,  # 视频观看时长，时间累加
				"video_2_time": 0,  # 练习次数
				"video_3_time": 0,  # 考核次数
			},
		}

	def get(self, request, *args, **kwargs):
		try:
			self.custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			today = datetime.date.today()

			# 查询今日任务
			learntasks = LearnTask.objects.filter(create_time=today)
			if learntasks.exists():
				learntask = learntasks.first()

				# 今日任务目标
				video_name = learntask.video.name
				section_name = learntask.video.section.title
				course_name = learntask.video.section.course.name
				project_name = learntask.video.section.course.project.name
				self.result_dict["data"]["task"] = "/".join([project_name, course_name, section_name, video_name])

				videos = Video.objects.filter(section__course__project=learntask.video.section.course.project)

				# 所有视频时长
				video_1 = videos.filter(type="1").aggregate(Sum('duration')).get("duration__sum", 0)
				m, s = divmod(str_to_int(video_1), 60)
				h, m = divmod(m, 60)
				self.result_dict["data"]["video_1"] = "%02d:%02d:%02d" % (h, m, s)

				# 包含练习题个数
				video_2 = videos.filter(type="2").count()
				self.result_dict["data"]["video_2"] = video_2

				# 包含考核个数
				video_3 = videos.filter(type="3").count()
				self.result_dict["data"]["video_3"] = video_3

				# 视频观看累计时长
				filter_param = {
					"user__id": self.custom_user_id,
					"video__section__course__project": learntask.video.section.course.project
				}
				total_duration = WatchRecord.objects.filter(**filter_param).aggregate(Sum('total_duration')).get(
					"total_duration__sum", 0)
				m, s = divmod(str_to_int(total_duration), 60)
				h, m = divmod(m, 60)
				self.result_dict["data"]["video_1_time"] = "%02d:%02d:%02d" % (h, m, s)

				# 练习次数
				filter_param = {
					"custom_user__id": self.custom_user_id,
					"video__section__course__project": learntask.video.section.course.project
				}
				video_2_time = UserExercise.objects.filter(**filter_param).aggregate(Sum('times')).get("times__sum", 0)
				self.result_dict["data"]["video_2_time"] = video_2_time

				# 考核次数
				filter_param = {
					"custom_user__id": self.custom_user_id,
					"video__section__course__project": learntask.video.section.course.project
				}
				video_2_time = UnlockVideo.objects.filter(**filter_param).aggregate(Sum('times')).get("times__sum", 0)
				self.result_dict["data"]["video_3_time"] = video_2_time

		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))

	def get_learn_schedule(self, task_date):
		"""获取任务完成百分比
		:param task_date: 发布任务时间
		:return:
		"""
		try:
			learntasks = LearnTask.objects.filter(create_time=task_date)
			if learntasks.exists():
				learntask = learntasks.first()
				project = learntask.video.section.course.project  # 任务所在项目


		except:
			traceback.print_exc()
