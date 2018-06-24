#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models

from applications.custom_user.model_form import CustomUser
from lib.storage import *


class Topic(models.Model):
	"""世界杯-题目"""
	RIGHTANSWER = (
		("A", "A"),
		("B", "B"),
	)
	title = models.CharField('题目', max_length=255)
	A = models.CharField('A', max_length=30)
	B = models.CharField('B', max_length=30)
	right = models.CharField('正确答案', max_length=1, choices=RIGHTANSWER)

	def __unicode__(self):
		return self.title

	class Meta:
		db_table = 'Topic'
		verbose_name = "问题"
		verbose_name_plural = "问题"


class Country(models.Model):
	"""国家字典信息 """
	name = models.CharField('国家名称', max_length=255)
	flag = models.ImageField('国旗图片', upload_to="flag", storage=ImageStorage(), max_length=255)

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'Country'
		verbose_name = "国家"
		verbose_name_plural = "国家"


class Tournament(models.Model):
	"""比赛 """
	country_a = models.ForeignKey('Country', verbose_name="国家A", related_name="tournament_country_a")
	country_b = models.ForeignKey('Country', verbose_name="国家B", related_name="tournament_country_b")
	start_time = models.DateTimeField('开赛时间', help_text="只显示、押注未开赛的赛事")
	a_victory = models.BooleanField('国家A-胜', default=False, help_text="出比赛结果后填写")
	common = models.BooleanField('平', default=False, help_text="出比赛结果后填写")
	b_victory = models.BooleanField('国家A-胜', default=False, help_text="出比赛结果后填写")
	is_summary = models.BooleanField('已汇总积分', default=False)
	create_time = models.DateTimeField('创建时间', auto_now=True)

	def __unicode__(self):
		return " vs ".join([self.country_a.name, self.country_b.name])

	class Meta:
		db_table = 'Tournament'
		verbose_name = "比赛"
		verbose_name_plural = "比赛"
		ordering = ["start_time"]


class BetRecord(models.Model):
	"""用户押注记录 """
	user = models.ForeignKey(CustomUser, verbose_name="用户", related_name="betrecord_user")
	tournament = models.ForeignKey('Tournament', verbose_name="比赛（A vs B）", related_name="betrecord_tournament")
	country = models.CharField('胜/平(C)', max_length=10, blank=True, help_text="A:A国家胜；B:B国家胜；C:平")
	integral = models.PositiveIntegerField("押注积分", default=0, help_text="押注积分，押中积分*2返给用户")
	create_time = models.DateTimeField('创建时间', auto_now=True)

	def __unicode__(self):
		return self.user.nickname

	class Meta:
		db_table = 'BetRecord'
		verbose_name = "押注记录"
		verbose_name_plural = "押注记录"
