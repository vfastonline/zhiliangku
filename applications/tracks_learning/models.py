#!encoding:utf-8
from __future__ import unicode_literals

import commands
import logging
import traceback

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from applications.assessment.models import DockerType
from applications.custom_user.models import CustomUser
from applications.live_streaming.models import Live
from lib.storage import *
from zhiliangku.settings import BASE_DIR


class Technology(models.Model):
	"""技术方向"""
	name = models.CharField('名称', max_length=50)
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
	sequence = models.PositiveIntegerField('顺序', default=1, validators=[MinValueValidator(1)], help_text="技术分类下显示顺序")
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
		ordering = ['technology', "sequence"]


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
	section = models.ForeignKey(Section, verbose_name='所属章节', related_name='Videos', blank=True, null=True)
	type = models.CharField('类型', max_length=1, choices=TYPE)
	name = models.CharField('视频/习题名称', max_length=255)
	address = models.FileField('视频', upload_to='video/%y%m%d', null=True, blank=True)
	subtitle = models.FileField('字幕', upload_to='video/%y%m%d', null=True, blank=True, default=' ')
	sequence = models.PositiveIntegerField('显示顺序', default=1, validators=[MinValueValidator(1)], help_text="从1开始，默认：1")
	duration = models.PositiveIntegerField('总时长', default=0, blank=True, help_text="视频成功上传后，由后台补全；单位：秒")
	desc = models.TextField('描述', default='', null=True, blank=True)
	notes = models.TextField('讲师笔记', default='', null=True, blank=True)
	topic = models.TextField('考核题目', default='', null=True, blank=True)
	shell = models.FileField('判题shell', upload_to='shell', storage=ShellStorage(), null=True, blank=True)
	docker = models.ForeignKey(DockerType, verbose_name='Docker类型', null=True, blank=True)
	assess_time = models.PositiveIntegerField('考核时长(分)', default=5, help_text="考核时长，默认5分钟；单位：分")

	# 保利威视信息
	vid = models.CharField("vid", max_length=255, blank=True, null=True, help_text="由保利威视回调接口补充")
	data = models.TextField("视频信息", blank=True, null=True, help_text="由保利威视回调接口补充")

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'Video'
		verbose_name = "视频/练习题/考核"
		verbose_name_plural = "视频/练习题/考核"
		ordering = ["section", 'sequence']


@receiver(post_save, sender=Video)  # 信号的名字，发送者
def add_video_event(sender, instance, **kwargs):  # 回调函数，收到信号后的操作
	"""新增/编辑 考核 保存事件 """
	try:
		# 把本地考核shell上传到docker服务器
		if instance.type == "3":
			if instance.shell:
				command = "scp %s root@docker:/usr/local/share/xiaodu/script/" % (
					os.path.join(BASE_DIR + instance.shell.url))
				commands.getoutput(command)

	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())


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
		verbose_name = "通过考核学生"
		verbose_name_plural = "通过考核学生"


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
		ordering = ["-create_time"]
