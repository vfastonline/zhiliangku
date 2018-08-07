#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models

from applications.custom_user.models import CustomUser
from lib.util import NULL_BLANK_TRUE


class DockerType(models.Model):
	"""Docker 类型"""

	name = models.CharField('类型名称', max_length=255)
	image = models.CharField('镜像名称', max_length=255, help_text=u"固定并准确,用于创建docker时补全命令")
	port = models.CharField('镜像端口', max_length=10, help_text=u"先确认阿里云服务器开放端口并没有被其他镜像占用")
	introduce = models.TextField('介绍', default='', **NULL_BLANK_TRUE)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'DockerType'
		verbose_name = "Docker类型"
		verbose_name_plural = "Docker类型"


class DockerPort(models.Model):
	"""Docker 容器端口"""

	container = models.CharField('容器', max_length=255)
	port = models.CharField('端口', max_length=7)
	create = models.DateTimeField('创建时间', auto_now=True)
	maturity = models.DateTimeField('到期时间', blank=True)

	def __str__(self):
		return self.container

	class Meta:
		db_table = 'DockerPort'
		verbose_name = "Docker已分配端口"
		verbose_name_plural = "Docker已分配端口"
