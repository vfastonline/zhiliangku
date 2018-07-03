#!encoding:utf-8
from __future__ import unicode_literals
from django.utils import timezone

from django.db import models

from applications.custom_user.models import CustomUser
from applications.tracks_learning.models import Video


class LearnTask(models.Model):
	"""学习任务"""

	video = models.ForeignKey(Video, verbose_name="视频/练习/考核", help_text="今日任务终点")
	custom_user = models.ForeignKey(CustomUser, verbose_name="创建人", related_name="TodayTaskCustomUser",
									limit_choices_to={'role': 1})
	create_time = models.DateField(verbose_name='创建时间', default=timezone.now)
	update_time = models.DateTimeField("更新时间", auto_now=True)

	def __unicode__(self):
		return self.video.name

	class Meta:
		db_table = 'LearnTask'
		verbose_name = "学习任务"
		verbose_name_plural = "学习任务"
