#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models

from lib.storage import ImageStorage


class Carousel(models.Model):
    """轮播图"""
    CATEGORY = (
        ("1", "首页"),
        ("2", "职业路径"),
        ("3", "个人中心"),
    )
    name = models.CharField('轮播名称', max_length=50)
    pathwel = models.ImageField('轮播图片', upload_to='carousel/%Y%m%d', storage=ImageStorage())
    category = models.CharField('类别', max_length=1, choices=CATEGORY, default="1")
    sequence = models.PositiveIntegerField('播放顺序', blank=True, default=1)
    desc = models.TextField('轮播简介', max_length=1000, blank=True, null=True, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Carousel'
        verbose_name = "轮播图"
        verbose_name_plural = "轮播图"
        # unique_together = (("category", "sequence"),)
        ordering = ["category", 'sequence']
        index_together = ["name", "category"]
