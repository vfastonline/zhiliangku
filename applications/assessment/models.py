#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models


class DockerType(models.Model):
	"""Docker 类型"""

	name = models.CharField('类型名称', max_length=255)
	image = models.CharField('镜像名称', max_length=255, help_text=u"固定并准确,用于创建docker时补全命令")
	introduce = models.TextField('介绍', default='', null=True, blank=True)

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'DockerType'
		verbose_name = "Docker类型"
		verbose_name_plural = "Docker类型"


class DockerPort(models.Model):
	"""Docker 端口"""

	container = models.CharField('容器', max_length=255)
	port = models.CharField('端口', max_length=255)

	def __unicode__(self):
		return self.container

	class Meta:
		db_table = 'DockerPort'
		verbose_name = "Docker端口"
		verbose_name_plural = "Docker端口"
		index_together = ['container', 'port']
