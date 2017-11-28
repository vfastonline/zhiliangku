#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models

from lib.storage import ImageStorage


class Live(models.Model):
    """直播"""
    name = models.CharField('直播名称', max_length=50)
    pathwel = models.ImageField('直播图片', upload_to='live/img/%Y/%m/%d', storage=ImageStorage())
    desc = models.TextField('直播简介', max_length=1000, blank=True, null=True, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Live'
        verbose_name = "直播"
        verbose_name_plural = "直播"
