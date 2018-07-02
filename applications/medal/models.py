#!encoding:utf-8
from __future__ import unicode_literals

import logging
import traceback

from django.db import models
from django.utils import timezone

from applications.custom_user.models import CustomUser
from lib.storage import *
from lib.util import NULL_BLANK_TRUE


class Medal(models.Model):
	"""勋章"""
	name = models.CharField('名称', max_length=50)
	pathwel = models.ImageField('图片', upload_to='medal', storage=ImageStorage())
	only = models.CharField('系统识别名称', max_length=50, **NULL_BLANK_TRUE)

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'Medal'
		verbose_name = "勋章"
		verbose_name_plural = "勋章"


class CustomUserMedal(models.Model):
	"""用户勋章 """

	custom_user = models.ForeignKey(CustomUser, verbose_name="用户", limit_choices_to={'role': 0},
									related_name='customusermedal')
	medal = models.ForeignKey(Medal, verbose_name="获得的勋章", **NULL_BLANK_TRUE)
	create_time = models.DateTimeField(verbose_name='获得时间', default=timezone.now)

	def __unicode__(self):
		return self.custom_user.nickname

	@staticmethod
	def add_customuser_medal(medal_only, custom_user):
		"""增加用户获得勋章
		:param medal_only: 勋章系统识别名称
		:param custom_user: 用户
		:return: 勋章图片地址
		"""
		pathwel = ""
		try:
			medal = Medal.objects.get(only=medal_only)
			CustomUserMedal.objects.get_or_create(custom_user=custom_user, medal=medal)
			pathwel = medal.pathwel.url if medal.pathwel else ""
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return pathwel

	class Meta:
		db_table = 'CustomUserMedal'
		verbose_name = "用户勋章"
		verbose_name_plural = "用户勋章"
		ordering = ["-create_time"]
