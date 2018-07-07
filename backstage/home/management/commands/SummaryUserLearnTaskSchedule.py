#!encoding:utf-8
"""
汇总用户今天任务完成进度
"""

import datetime
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Sum
from applications.custom_user.models import CustomUser
from backstage.home.models import *
from applications.tracks_learning.models import Video

from applications.world_cup.models import *
from lib.util import get_day_of_day
from applications.record.models import WatchRecord


class Command(BaseCommand):
	help = "Aggregate the progress of each student’s task on the same day"

	def handle(self, *args, **options):
		"""每小时汇总每个学员当天任务学习进度
		:return:
		"""
		try:
			today_date = get_day_of_day(0)  # 今天
			learntasks = LearnTask.objects.filter(create_time=today_date)

			# 今天有任务
			if learntasks.exists():
				customusers = CustomUser.objects.filter(role=0)
				video = learntasks.first()
				project = video.section.course.project  # 项目
				videos = list(Video.objects.filter(section__course__project=project))  # 项目下所有视频

				UserLearnTaskSummary.objects.filter(custom_user__in=customusers, task=video).delete()
				summary_list = list()  # 汇总好的结果列表
				for user in customusers:
					filter_param = {"user": user, "course__project": project, "status": 1}
					watchrecords = WatchRecord.objects.filter(**filter_param).order_by("-create_time")
					if not watchrecords.exists():
						summary = UserLearnTaskSummary(custom_user=user, task=video, schedule=0)
						summary_list.append(summary)
						continue

					task_video_index = videos.index(watchrecords.first().video) + 1
					schedule = float("%.2f" % (float(task_video_index) / float(len(videos))))
					summary = UserLearnTaskSummary(custom_user=user, task=video, schedule=schedule)
					summary_list.append(summary)
				if summary_list:
					UserLearnTaskSummary.objects.bulk_create(summary_list)
		except:
			traceback.print_exc()
			raise CommandError(traceback.format_exc())
