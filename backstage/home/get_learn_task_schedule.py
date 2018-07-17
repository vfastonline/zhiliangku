#!encoding:utf-8
from django.views.generic import View

from backstage.home.models import *
from lib.permissionMixin import class_view_decorator, teacher_login_required
from lib.util import *
import datetime


@class_view_decorator(teacher_login_required)
class GetHasTodayLearnTaskInfo(View):
	"""当天是否有任务发布"""

	def __init__(self):
		super(GetHasTodayLearnTaskInfo, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": False,
		}

	def get(self, request, *args, **kwargs):
		try:
			# 查询昨日目标、进度
			today_date = get_day_of_day(0)
			today_date = datetime.datetime(today_date.year, today_date.month, today_date.day)
			learntasks = LearnTask.objects.filter(create_time=today_date)
			if learntasks.exists():
				self.result_dict["data"] = True
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


@class_view_decorator(teacher_login_required)
class GetTodayTaskScheduleInfo(View):
	"""获取今日预计目标进度"""

	def __init__(self):
		super(GetTodayTaskScheduleInfo, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": {
				"today_date": "",
				"today_task_name": "",
				"today_task_schedule": 0,
			},
		}

	def get(self, request, *args, **kwargs):
		try:
			video_id = str_to_int(request.GET.get('video_id', 0))  # 今日学习任务视频ID

			today_date = get_day_of_day(0)
			self.result_dict["data"]["today_date"] = today_date.strftime('%Y-%m-%d')

			# 查询今日预计目标进度
			task_video = Video.objects.get(id=video_id)
			courses = task_video.section.course.project.Courses.all()
			videos = list(Video.objects.filter(section__course__in=courses))
			task_video_index = videos.index(task_video) + 1
			schedule = float("%.2f" % (float(task_video_index) / float(len(videos))))
			self.result_dict["data"]["today_task_schedule"] = str(schedule)

			# 组装今日目标
			video_name = task_video.name
			section_name = task_video.section.title
			course_name = task_video.section.course.name
			project_name = task_video.section.course.project.name
			today_task_name = "/".join([project_name, course_name, section_name, video_name])
			self.result_dict["data"]["today_task_name"] = today_task_name
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


@class_view_decorator(teacher_login_required)
class GetYesterdayTaskScheduleInfo(View):
	"""获取昨日目标进度"""

	def __init__(self):
		super(GetYesterdayTaskScheduleInfo, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": {
				"yesterday_date": "",  # 昨天日期
				"yesterday_task_name": "",  # 昨天任务名称，项目-课程-章节-视频
				"yesterday_task_schedule": 0,  # 昨日任务目标进度
				"yesterday_completion_ratio": 0,  # 完成昨日目标人数占比
			},
		}

	def get(self, request, *args, **kwargs):
		try:
			# 查询昨日目标、进度
			yesterday_date = get_day_of_day(-1)
			self.result_dict["data"]["yesterday_date"] = yesterday_date.strftime('%Y-%m-%d')
			yesterday_task = LearnTask.objects.filter(create_time=yesterday_date)
			if yesterday_task.exists():
				learntask = yesterday_task.first()
				video_name = learntask.video.name
				section_name = learntask.video.section.title
				course_name = learntask.video.section.course.name
				project_name = learntask.video.section.course.project.name
				yesterday_task_name = "/".join([project_name, course_name, section_name, video_name])
				self.result_dict["data"]["yesterday_task_name"] = yesterday_task_name
				try:
					learntasksummary = LearnTaskSummary.objects.get(task=learntask)
					completion = learntasksummary.complete
					schedule = learntasksummary.schedule
				except:
					schedule = 0
					completion = 0
				self.result_dict["data"]["yesterday_task_schedule"] = schedule
				self.result_dict["data"]["yesterday_completion_ratio"] = completion
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))
