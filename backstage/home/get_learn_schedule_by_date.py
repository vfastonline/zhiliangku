#!encoding:utf-8
import datetime

from django.db.models import Avg
from django.views.generic import View

from applications.exercise.models import UserExercise
from applications.record.models import WatchRecord
from applications.tracks_learning.models import *
from backstage.home.models import *
from lib.base_redis import redis_db
from lib.permissionMixin import class_view_decorator, teacher_login_required
from lib.util import *


@class_view_decorator(teacher_login_required)
class GetLearnTaskScheduleBydate(View):
	"""根据日期获取学习任务完成进度"""

	def __init__(self):
		super(GetLearnTaskScheduleBydate, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": {
				"average": 0,
				"improve": 0,
				"complete": 0,
				"undone": 0,
				"excess_complete": 0,
			},
		}

	def get(self, request, *args, **kwargs):
		try:
			today_date = get_day_of_day(0)
			today_date = datetime.datetime(today_date.year, today_date.month, today_date.day)
			get_date = request.GET.get('get_date', "")  # 今日学习任务视频ID
			if not get_date:
				get_date = today_date
			else:
				get_date = datetime.datetime.strptime(get_date, "%Y-%m-%d")
			get_date_str = get_date.strftime("%Y-%m-%d")

			learn_task_schedule = redis_db.get("LearnTaskSchedule_%s" % get_date_str)
			if learn_task_schedule:
				self.result_dict["data"] = learn_task_schedule
			else:
				if get_date < today_date:  # 历史数据
					learntasks = LearnTask.objects.filter(create_time=get_date)
					if learntasks.exists():
						values = ["average", "improve", "complete", "undone", "excess_complete"]
						summarys = LearnTaskSummary.objects.filter(task=learntasks.first()).values(*values)
						if summarys.exists():
							learn_task_schedule = summarys.first()
							self.result_dict["data"] = learn_task_schedule
							redis_db.set("LearnTaskSchedule_%s" % get_date_str, learn_task_schedule)
				elif get_date == today_date:  # 当天的实时汇总
					learn_task_schedule = summary_learn_task(get_date)
					self.result_dict["data"] = learn_task_schedule
					redis_db.setex("LearnTaskSchedule_%s" % get_date_str, learn_task_schedule, 60 * 30)
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:

			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


def summary_learn_task(task_date):
	"""学习任务时间
	:param task_date:任务日期，date
	:return:
	"""
	result = {
		"average": 0,  # 班级平均进度
		"improve": 0,  # 较昨日提高
		"complete": 0,  # 完成学习任务，完成-超额=完成人数
		"undone": 0,  # 未完成学习任务，总人数-完成=未完成
		"excess_complete": 0  # 超完成进度，完成-超额=完成人数
	}
	try:
		# 学生总人数
		customuser_count = CustomUser.objects.filter(role=0).count()

		# 当天任务目标节点
		learntasks = LearnTask.objects.filter(create_time=task_date)
		if learntasks.exists():
			learntask = learntasks.first()
			video = learntask.video
			video_sequence = learntask.video.sequence  # 顺序
			project = learntask.video.section.course.project  # 项目
			project_sequence = learntask.video.section.course.project.sequence  # 项目顺序
			project_technology = learntask.video.section.course.project.technology  # 项目分类
			# 当前项目分类下，目标项目的下多个项目
			projects = list(Project.objects.filter(technology=project_technology, sequence__gt=project_sequence))

			# 获取超过目标视频的视频信息列表
			video_list = list(Video.objects.filter(section__course__project=project, sequence__gt=video_sequence))
			if not video_list:
				video_list = list(Video.objects.filter(section__course__project__in=projects))

			# 超完成学习任务
			watchrecord_count = WatchRecord.objects.filter(video__in=video_list, status=1).values_list(
				"user", flat=True).distinct()
			userexercise_count = UserExercise.objects.filter(video__in=video_list, is_pass=True).values_list(
				"custom_user", flat=True).distinct()
			unlock_count = UnlockVideo.objects.filter(video__in=video_list, is_pass=True).values_list(
				"custom_user", flat=True).distinct()

			excess_complete_user = list(set(watchrecord_count + userexercise_count + unlock_count))
			result["excess_complete"] = float("%.2f" % (float(len(excess_complete_user)) / float(customuser_count)))

			# 完成学习任务
			watchrecord_count = WatchRecord.objects.filter(video=video, status=1).values_list(
				"user", flat=True).distinct()
			userexercise_count = UserExercise.objects.filter(video=video, is_pass=True).values_list(
				"custom_user", flat=True).distinct()
			unlock_count = UnlockVideo.objects.filter(video=video, is_pass=True).values_list(
				"custom_user", flat=True).distinct()
			complete_user = list(set(watchrecord_count + userexercise_count + unlock_count))

			# 总学生数-完成人数=未完成
			undone = customuser_count - len(complete_user)
			result["undone"] = float("%.2f" % (float(undone) / float(customuser_count)))

			# 完成与超额差集，为完成人员
			complete_user = list(set(complete_user) ^ set(excess_complete_user))
			result["complete"] = float("%.2f" % (float(len(complete_user)) / float(customuser_count)))

			# 平均进度，
			schedule__avg = UserLearnTaskSummary.objects.filter(task=video).aggregate(Avg("schedule")).get(
				"schedule__Avg")
			if not schedule__avg:
				result["average"] = 0
				result["improve"] = 0
			else:
				yesterday_average = 0
				yesterday_learntasks = LearnTask.objects.filter(create_time=task_date - timedelta(days=1))
				if yesterday_learntasks.exists():
					learntasksummarys = LearnTaskSummary.objects.filter(task=yesterday_learntasks.first())
					learntasksummary = learntasksummarys.first()
					yesterday_average = learntasksummary.average
				result["average"] = schedule__avg
				result["improve"] = schedule__avg - yesterday_average
	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())
	finally:
		return result
