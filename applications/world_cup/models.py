#!encoding:utf-8
from __future__ import unicode_literals

import logging
import traceback

from django.db import models
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

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
	"""比赛"""
	country_a = models.ForeignKey('Country', verbose_name="国家A", related_name="tournament_country_a")
	country_b = models.ForeignKey('Country', verbose_name="国家B", related_name="tournament_country_b")
	start_time = models.DateTimeField('开赛时间', help_text="只显示、押注未开赛的赛事")
	a_victory = models.BooleanField('国家A-胜', default=False, help_text="出比赛结果后填写")
	common = models.BooleanField('平', default=False, help_text="出比赛结果后填写")
	b_victory = models.BooleanField('国家B-胜', default=False, help_text="出比赛结果后填写")
	is_summary = models.BooleanField('已汇总', default=False, help_text="系统已经通过定时任务根据比赛结果汇总用户猜球结果并返积分")
	summary_time = models.DateTimeField('汇总时间', blank=True, null=True)
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


@receiver(post_save, sender=BetRecord)
def BetRecord_counter(sender, instance, created, **kwargs):
	"""当有新的用户投注，投注记录总数计数器 +1
	:param sender:
	:param instance:
	:param created:
	:param kwargs:
	:return:
	"""
	try:
		# 只有当这个instance是新创建的，投注记录+1
		if not created:
			return
		BetRecordCount.objects.all().update(count=F('count') + 1)
	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())


class BetRecordCount(models.Model):
	"""用户押注记录总数"""
	count = models.PositiveIntegerField("押注记录总数", default=999)

	def __unicode__(self):
		return str(self.count)

	class Meta:
		db_table = 'BetRecordCount'
		verbose_name = "押注记录总数"
		verbose_name_plural = "押注记录总数"


class Analysis(models.Model):
	"""教你赢球"""
	chart = models.ImageField('分析图', upload_to="analysis", storage=ImageStorage(), max_length=255, blank=True)
	create_time = models.DateField('创建时间', auto_now=True, help_text="当天只显示当天的分析数据")

	def __unicode__(self):
		return str(self.id)

	class Meta:
		db_table = 'Analysis'
		verbose_name = "教你赢球"
		verbose_name_plural = "教你赢球"
