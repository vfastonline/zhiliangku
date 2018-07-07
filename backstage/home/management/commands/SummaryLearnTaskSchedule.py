#!encoding:utf-8
"""
汇总今天任务完成进度
"""

from django.core.management.base import BaseCommand, CommandError

from backstage.home.get_learn_schedule_by_date import summary_learn_task
from backstage.home.models import *
from lib.util import get_day_of_day


class Command(BaseCommand):
	help = "Total daily learning task progress at 23:50 every day"

	def handle(self, *args, **options):
		"""每天23:50汇总当天总学习任务进度
		:return:
		"""
		try:
			today_date = get_day_of_day(0)  # 当天日期
			summary_dict = summary_learn_task(today_date)  # 当天学习任务汇总结果
			learntasks = LearnTask.objects.filter(create_time=today_date)  # 当天学习任务
			if learntasks.exists():
				LearnTaskSummary.objects.filter(task=learntasks.first()).update(**summary_dict)
		except:
			traceback.print_exc()
			raise CommandError(traceback.format_exc())
