#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from lib.storage import *
from django.core.validators import MinValueValidator


class WechatBrowse(models.Model):
	"""微信推广-浏览-点赞-统计"""
	name = models.CharField('姓名', max_length=255, help_text="学生姓名", blank=True)
	pinyin = models.CharField('姓名拼音', max_length=255, help_text="学生姓名的字母全拼", blank=True)
	remark = models.CharField('评语', max_length=255, blank=True, help_text="每页评语索引用逗号(英文)分隔，例：1A,2B,3C")
	avatar = models.ImageField('头像', upload_to="wechat/avatar", storage=ImageStorage(),
							   default="custom_user_avatar/defaultUserIcon.png")
	photo2 = models.ImageField('第2页照片', upload_to="wechat/photo", storage=ImageStorage(), blank=True, help_text="活动照")
	photo3 = models.ImageField('第3页照片', upload_to="wechat/photo", storage=ImageStorage(), blank=True, help_text="活动照")
	photo4 = models.ImageField('第4页照片', upload_to="wechat/photo", storage=ImageStorage(), blank=True, help_text="活动照")
	photo5 = models.ImageField('第5页照片', upload_to="wechat/photo", storage=ImageStorage(), blank=True, help_text="活动照")
	page_views = models.PositiveIntegerField('浏览量', default=0)
	thumbs_up = models.PositiveIntegerField('打Call', default=0)
	share = models.PositiveIntegerField('分享', default=0)
	create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)

	def __unicode__(self):
		return ",".join([self.name, str(self.page_views), str(self.thumbs_up)])

	class Meta:
		db_table = 'WechatBrowse'
		verbose_name = "学生信息"
		verbose_name_plural = "学生信息"


class WechatBackground(models.Model):
	sequence = models.PositiveIntegerField('顺序', default=1, validators=[MinValueValidator(1)])
	image = models.ImageField('背景图', upload_to="wechat/background", storage=ImageStorage())

	class Meta:
		db_table = 'WechatBackground'
		verbose_name = "背景图"
		verbose_name_plural = "背景图"
		ordering = ["sequence"]


class WechatRemark(models.Model):
	name = models.CharField('评语标识', max_length=255)
	remark = models.TextField('评语', max_length=255)

	def __unicode__(self):
		return "".join([str(self.name), "--", str(self.remark)])

	class Meta:
		db_table = 'WechatRemark'
		verbose_name = "评语"
		verbose_name_plural = "评语"
		ordering = ["name"]
