#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class WechatBrowse(models.Model):
	"""微信推广-浏览-点赞-统计"""
	page_views = models.PositiveIntegerField('浏览量', blank=True, null=True, default=0)
	thumbs_up = models.PositiveIntegerField('赞', blank=True, null=True, default=0)
	create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)

	def __unicode__(self):
		return "".join([str(self.page_views), "--", str(self.thumbs_up)])

	class Meta:
		db_table = 'WechatBrowse'
		verbose_name = "微信推广"
		verbose_name_plural = "微信推广"
