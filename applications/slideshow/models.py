#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models

from lib.storage import ImageStorage


class Carousel(models.Model):
    """轮播图"""
    name = models.CharField('轮播名称', max_length=50)
    pathwel = models.ImageField('轮播图片', upload_to='carousel/%Y%m%d', storage=ImageStorage())

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Carousel'
        verbose_name = "轮播图"
        verbose_name_plural = "轮播图"
