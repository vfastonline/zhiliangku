#!encoding:utf-8
from __future__ import unicode_literals

import logging
import traceback

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from applications.custom_user.models import CustomUser
from applications.tracks_learning.models import Video
from lib.util import NULL_BLANK_TRUE


class LearnTask(models.Model):
	"""学习任务"""

	video = models.ForeignKey(Video, verbose_name="视频/练习/考核", help_text="今日任务终点", on_delete=models.CASCADE)
	custom_user = models.ForeignKey(CustomUser, verbose_name="创建老师", related_name="TodayTaskCustomUser",
									limit_choices_to={'role': 1}, on_delete=models.CASCADE)
	create_time = models.DateField(verbose_name='创建时间', default=timezone.now)
	update_time = models.DateTimeField("更新时间", auto_now=True)

	def __str__(self):
		return "--".join([self.video.name, self.create_time.strftime("%Y-%m-%d")])

	class Meta:
		db_table = 'LearnTask'
		verbose_name = "学习任务"
		verbose_name_plural = "学习任务"


@receiver(post_save, sender=LearnTask)
def calculate_task_progress(sender, instance, **kwargs):
	"""计算学习任务进度 """
	try:
		task_video = instance.video
		courses = instance.video.section.course.project.Courses.all()
		videos = list(Video.objects.filter(section__course__in=courses))
		task_video_index = videos.index(task_video) + 1
		schedule = float("%.2f" % (float(task_video_index) / float(len(videos))))
		learntasksummarys = LearnTaskSummary.objects.filter(task=instance)
		if learntasksummarys.exists():
			learntasksummarys.update(schedule=schedule)
		else:
			LearnTaskSummary.objects.create(task=instance, schedule=schedule)
	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())


class LearnTaskSummary(models.Model):
	"""班级-学习任务进度汇总--首页饼状图，折线图"""
	task = models.ForeignKey(LearnTask, verbose_name="学习任务", on_delete=models.CASCADE)
	schedule = models.FloatField("目标进度", max_length=10, **NULL_BLANK_TRUE)  # 当前任务占总任务百分比，粒度为一个项目
	average = models.FloatField("班级平均进度", default=0, **NULL_BLANK_TRUE)
	improve = models.FloatField("较昨日提高", default=0, **NULL_BLANK_TRUE)
	complete = models.FloatField("完成目标人数比例", default=0, **NULL_BLANK_TRUE)
	undone = models.FloatField("未完成目标人数比例", default=0, **NULL_BLANK_TRUE)
	excess_complete = models.FloatField("超完成目标人数比例", default=0, **NULL_BLANK_TRUE)
	update_time = models.DateTimeField("更新时间", auto_now=True)

	def __str__(self):
		return self.task.video.name

	class Meta:
		db_table = 'LearnTaskSummary'
		verbose_name = "学习任务汇总"
		verbose_name_plural = "学习任务汇总"


class UserLearnTaskSummary(models.Model):
	"""学生-学习任务进度汇总"""
	custom_user = models.ForeignKey(CustomUser, verbose_name="学生", limit_choices_to={'role': 0}, on_delete=models.CASCADE)
	task = models.ForeignKey(LearnTask, verbose_name="学习任务", on_delete=models.CASCADE)
	schedule = models.FloatField("目标进度", max_length=10, **NULL_BLANK_TRUE)  # 当前任务占总任务百分比，粒度为一个项目

	def __str__(self):
		return "--".join([self.custom_user.nickname, str(self.schedule)])

	class Meta:
		db_table = 'UserLearnTaskSummary'
		verbose_name = "学生学习任务进度汇总"
		verbose_name_plural = "学习任务进度汇总"
