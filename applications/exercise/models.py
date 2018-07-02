#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from applications.tracks_learning.models import Video
from applications.custom_user.models import CustomUser


class Question(models.Model):
	RIGHTANSWER = (
		("1", "A"),
		("2", "B"),
		("3", "C"),
		("4", "D"),
	)
	video = models.ForeignKey(Video, verbose_name='所属视频', related_name='Questions', limit_choices_to={"type": "2"})
	title = models.CharField('问题内容', max_length=255)
	right_answer = models.CharField('正确答案', max_length=1, choices=RIGHTANSWER)
	detail = models.TextField('习题详解', max_length=255, default="")

	def __unicode__(self):
		return self.title

	class Meta:
		db_table = 'Question'
		verbose_name = "习题"
		verbose_name_plural = "习题"
		ordering = ["video"]
		index_together = ["video"]


class Answer(models.Model):
	RIGHTANSWER = (
		("1", "A"),
		("2", "B"),
		("3", "C"),
		("4", "D"),
	)
	question = models.ForeignKey(Question, verbose_name='所属习题', related_name='Answers')
	option = models.CharField('选项', max_length=1, choices=RIGHTANSWER)
	content = models.TextField('内容', max_length=255, default="")

	def __unicode__(self):
		return self.content

	class Meta:
		db_table = 'Answer'
		verbose_name = "答案"
		verbose_name_plural = "答案"
		ordering = ["question"]
		unique_together = (("question", "option"),)


class UserExercise(models.Model):
	"""用户的练习记录"""
	custom_user = models.ForeignKey(CustomUser, verbose_name='讲师', limit_choices_to={'role': 0})
	video = models.ForeignKey(Video, verbose_name='所属视频', limit_choices_to={"type": "2"})
	times = models.PositiveIntegerField("练习次数", default=1)

	def __unicode__(self):
		return self.custom_user.nickname

	class Meta:
		db_table = 'UserExercise'
		verbose_name = "用户练习记录"
		verbose_name_plural = "用户练习记录"
