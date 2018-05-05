#!encoding:utf-8
from __future__ import unicode_literals

from django.core.validators import MinValueValidator
from django.db import models

from lib.storage import ImageStorage
from applications.tracks_learning.models import Video


class Project(models.Model):
    """项目说明书"""
    pathwel = models.ImageField('介绍图片', upload_to='introduc/%Y%m%d', storage=ImageStorage())
    title = models.CharField('标题', max_length=50)
    name = models.CharField('名称', max_length=50)
    desc = models.TextField('项目简介', max_length=1000, blank=True, null=True, default='')

    def __unicode__(self):
        return self.title + self.name

    class Meta:
        db_table = 'Project'
        verbose_name = "项目说明书"
        verbose_name_plural = "项目说明书"
