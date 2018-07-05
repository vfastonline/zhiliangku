#!encoding:utf-8
import datetime

from django.views.generic import View

from backstage.home.models import *
from lib.permissionMixin import class_view_decorator, teacher_login_required
from lib.util import *
from lib.base_redis import redis_db


@class_view_decorator(teacher_login_required)
class GetLearnTaskScheduleBydate(View):
	"""根据日期获取学习任务完成进度"""

	def __init__(self):
		super(GetLearnTaskScheduleBydate, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": {
				"schedule": 0,
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
						values = ["schedule", "average", "improve", "complete", "undone", "excess_complete"]
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
	:param task_date:
	:return:
	"""
	result = {
		"schedule": 0,
		"average": 0,
		"improve": 0,
		"complete": 0,
		"undone": 0,
		"excess_complete": 0
	}
	try:
		pass
	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())
	finally:
		return result
