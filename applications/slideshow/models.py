#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models

from lib.storage import ImageStorage


class Carousel(models.Model):
    """轮播图"""
    name = models.CharField('轮播名称', max_length=50)
    pathwel = models.ImageField('轮播图片', upload_to='carousel/img/%Y/%m/%d', storage=ImageStorage())
    desc = models.TextField('轮播简介', max_length=1000, blank=True, null=True, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Carousel'
        verbose_name = "轮播图"
        verbose_name_plural = "轮播图"
