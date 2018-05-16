#!encoding:utf-8
from __future__ import unicode_literals

from colorfield.fields import ColorField
from django.core.validators import MinValueValidator
from django.db import models

from applications.custom_user.models import CustomUser
from applications.live_streaming.models import Live
from lib.storage import ImageStorage


class Technology(models.Model):
	"""技术方向"""
	name = models.CharField('名称', max_length=50)
	color = ColorField('颜色', max_length=50, default='#FFFFFF')
	desc = models.TextField('简介', default='', blank=True, null=True)
	video = models.ForeignKey("Video", verbose_name='总考核', related_name='Technology', blank=True, null=True,
	                          limit_choices_to={'type': 3}, help_text=u"针对本技术方向下所有项目的总考核")

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'Technology'
		verbose_name = "技术方向"
		verbose_name_plural = "技术方向"


class Project(models.Model):
	"""项目说明书"""
	name = models.CharField('名称', max_length=50)
	desc = models.TextField('简介', max_length=1000, blank=True, null=True, default='')
	technology = models.ForeignKey(Technology, verbose_name="技术分类", blank=True, null=True)
	color = ColorField('颜色', max_length=50, default="#00CCFF")
	is_lock = models.BooleanField("锁定", default=True)
	home_show = models.BooleanField("首页展示", default=False)
	pathwel = models.ImageField('介绍图片', upload_to='project/%Y%m%d', storage=ImageStorage(), null=True, blank=True)
	video = models.ForeignKey("Video", verbose_name='项目考核', related_name='Project', blank=True, null=True,
	                          limit_choices_to={'type': 3}, help_text=u"针对本项目下所有课程的考核")

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'Project'
		verbose_name = "项目"
		verbose_name_plural = "项目"


class Course(models.Model):
	"""课程"""

	project = models.ForeignKey(Project, verbose_name='归属项目', related_name='Courses', blank=True, null=True)
	name = models.CharField('名称', max_length=50)
	lecturer = models.ForeignKey(CustomUser, verbose_name='讲师', related_name='Course_custom_user',
	                             limit_choices_to={'role': 1}, blank=True, null=True)
	desc = models.TextField('描述', default="", null=True, blank=True)
	sequence = models.PositiveIntegerField('顺序', default=1, validators=[MinValueValidator(1)], help_text="默认顺序为1")
	update_time = models.DateTimeField("更新时间", auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'Course'
		verbose_name = "课程"
		verbose_name_plural = "课程"
		ordering = ['project', "sequence"]


class Section(models.Model):
	"""课程-章节"""
	course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='所属课程', related_name='Section')
	title = models.CharField('章节标题', max_length=100, default='')
	desc = models.TextField('章节描述', default='', null=True, blank=True)
	sequence = models.PositiveIntegerField('章节顺序', default=1, validators=[MinValueValidator(1)], help_text="默认顺序为1")

	def __unicode__(self):
		return self.title

	class Meta:
		db_table = 'Section'
		verbose_name = "章节"
		verbose_name_plural = "章节"
		ordering = ["course", 'sequence']


class Video(models.Model):
	TYPE = (
		("1", "视频"),
		("2", "练习题"),
		("3", "考核"),
	)
	DOCKER = (
		("0", "Linux"),
		("1", "Java"),
		("2", "Hadoop"),
		("3", "Oracle"),
	)
	section = models.ForeignKey(Section, verbose_name='所属章节', related_name='Videos', blank=True, null=True)
	type = models.CharField('类型', max_length=1, choices=TYPE)
	name = models.CharField('视频/习题名称', max_length=255)
	address = models.FileField('视频', upload_to='video/%y%m%d', null=True, blank=True)
	subtitle = models.FileField('字幕', upload_to='video/%y%m%d', null=True, blank=True, default=' ')
	shell = models.FileField('考核shell', upload_to='shell/%y%m%d', null=True, blank=True)
	docker = models.CharField('Docker类型', max_length=1, choices=DOCKER, null=True, blank=True)
	sequence = models.PositiveIntegerField('显示顺序', default=1, validators=[MinValueValidator(1)], help_text="从1开始，默认：1")
	duration = models.PositiveIntegerField('总时长(秒)', default=0, help_text="视频成功上传后，由后台补全；单位：秒")
	desc = models.TextField('描述', default='', null=True, blank=True)
	notes = models.TextField('讲师笔记', default='', null=True, blank=True)

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'Video'
		verbose_name = "视频"
		verbose_name_plural = "视频"
		ordering = ["section", 'sequence']


class UnlockVideo(models.Model):
	"""学生通过考核记录"""
	video = models.ForeignKey(Video, verbose_name="考核", related_name='UnlockVideos', limit_choices_to={'type': 3})
	custom_user = models.ForeignKey(CustomUser, verbose_name='学生', related_name='UnlockVideoCustomUser',
	                                limit_choices_to={'role': 0}, blank=True, null=True)
	update_time = models.DateTimeField("更新时间", auto_now=True)

	def __unicode__(self):
		return self.video.name

	class Meta:
		db_table = 'UnlockVideo'
		verbose_name = "用户通过考核"
		verbose_name_plural = "用户通过考核"


class Nodus(models.Model):
	"""视频难点"""
	video = models.ForeignKey(Video, verbose_name="视频", limit_choices_to={'type': 1})
	title = models.CharField(max_length=200, verbose_name="标题")
	notes = models.TextField(verbose_name='解析')
	moment = models.PositiveIntegerField(verbose_name='视频时刻', help_text="单位：秒")

	def __unicode__(self):
		return self.title

	class Meta:
		db_table = 'Nodus'
		verbose_name = "视频难点解析"
		verbose_name_plural = "视频难点解析"


class CommonQuestion(models.Model):
	"""视频常见问题"""
	video = models.ForeignKey(Video, verbose_name="视频", limit_choices_to={'type': 1})
	question = models.CharField(max_length=200, verbose_name='问题')
	answer = models.TextField(verbose_name='回答')

	def __unicode__(self):
		return self.question

	class Meta:
		db_table = 'CommonQuestion'
		verbose_name = "视频常见问题"
		verbose_name_plural = "视频常见问题"


class StudentNotes(models.Model):
	"""学生笔记"""
	video = models.ForeignKey(Video, verbose_name="视频", limit_choices_to={'type': 1})
	custom_user = models.ForeignKey(CustomUser, verbose_name="学生", limit_choices_to={'role': 0}, null=True, blank=True)
	title = models.CharField(max_length=200, verbose_name='标题')
	notes = models.TextField(verbose_name='笔记内容')
	create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

	def __unicode__(self):
		return self.title

	class Meta:
		db_table = 'StudentNotes'
		verbose_name = "学生笔记"
		verbose_name_plural = "学生笔记"
