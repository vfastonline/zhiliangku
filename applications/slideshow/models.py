#!encoding:utf-8
from __future__ import unicode_literals

from django.core.validators import MinValueValidator
from django.db import models

from applications.tracks_learning.models import Video
from lib.storage import ImageStorage
from lib.util import NULL_BLANK_TRUE


class Carousel(models.Model):
	"""轮播图"""
	CATEGORY = (
		("1", "首页"),
		("2", "职业路径"),
		("3", "个人中心"),
	)
	name = models.CharField('轮播名称', max_length=50)
	pathwel = models.ImageField('轮播图片', upload_to='carousel', storage=ImageStorage())
	category = models.CharField('类别', max_length=1, choices=CATEGORY, default="1")
	video = models.ForeignKey(Video, on_delete=models.SET_NULL, verbose_name='宣传视频',
							  help_text="选填", **NULL_BLANK_TRUE)  # 高薪就业班宣传视频
	sequence = models.PositiveIntegerField('播放顺序', blank=True, default=1, validators=[MinValueValidator(1)],
										   help_text="从1开始，默认顺序为1")
	desc = models.TextField('轮播简介', max_length=1000, default='', **NULL_BLANK_TRUE)

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'Carousel'
		verbose_name = "轮播图"
		verbose_name_plural = "轮播图"
		# unique_together = (("category", "sequence"),)
		ordering = ["category", 'sequence']
		index_together = ["name", "category"]


class WebsiteIntroduce(models.Model):
	"""智量酷介绍（智量酷是什么）"""
	pathwel = models.ImageField('介绍图片', upload_to='introduc/%Y%m%d', storage=ImageStorage())
	title = models.CharField('标题', max_length=50)
	desc = models.TextField('介绍描述', max_length=1000, default='', **NULL_BLANK_TRUE)
	sequence = models.PositiveIntegerField('显示顺序', blank=True, default=1, validators=[MinValueValidator(1)],
										   help_text="从1开始，默认顺序为1")

	def __unicode__(self):
		return self.title

	class Meta:
		db_table = 'WebsiteIntroduce'
		verbose_name = "智量酷是什么"
		verbose_name_plural = "智量酷是什么"
		ordering = ['sequence']


class RecruitmentPlan(models.Model):
	"""企业人才招聘方案"""
	title = models.CharField('标题', max_length=255)
	desc = models.TextField('介绍描述', max_length=1000, default='', **NULL_BLANK_TRUE)
	pathwel = models.ImageField('图片', upload_to='plan/%Y%m%d', storage=ImageStorage(), **NULL_BLANK_TRUE)
	sequence = models.PositiveIntegerField('显示顺序', blank=True, default=1, validators=[MinValueValidator(1)],
										   help_text="从1开始，默认顺序为1")

	def __unicode__(self):
		return self.title

	class Meta:
		db_table = 'RecruitmentPlan'
		verbose_name = "企业人才招聘方案"
		verbose_name_plural = "企业人才招聘方案"
		ordering = ['sequence']
