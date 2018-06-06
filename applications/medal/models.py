#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from applications.custom_user.models import CustomUser
from lib.storage import *


class Medal(models.Model):
	"""勋章"""
	name = models.CharField('名称', max_length=50)
	pathwel = models.ImageField('图片', upload_to='medal', storage=ImageStorage())

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'Medal'
		verbose_name = "勋章"
		verbose_name_plural = "勋章"


class CustomUserMedal(models.Model):
	"""用户勋章 """

	custom_user = models.ForeignKey(CustomUser, verbose_name="用户", limit_choices_to={'role': 0}, related_name='customusermedal')
	medal = models.ForeignKey(Medal, verbose_name="获得的勋章", blank=True, null=True)
	create_time = models.DateTimeField(verbose_name='获得时间', default=timezone.now)

	def __unicode__(self):
		return self.custom_user.nickname

	class Meta:
		db_table = 'CustomUserMedal'
		verbose_name = "用户勋章"
		verbose_name_plural = "用户勋章"
		ordering = ["-create_time"]
