#!encoding:utf-8
from __future__ import unicode_literals

from django.core.validators import MinValueValidator
from django.db import models

from lib.storage import ImageStorage


class Carousel(models.Model):
    """轮播图"""
    CATEGORY = (
        ("1", "首页"),
        ("2", "职业路径"),
    )
    name = models.CharField('轮播名称', max_length=50)
    pathwel = models.ImageField('轮播图片', upload_to='carousel/%Y%m%d', storage=ImageStorage())
    category = models.CharField('类别', max_length=1, choices=CATEGORY, default="1")
    sequence = models.PositiveIntegerField('播放顺序', default=1, validators=[MinValueValidator(1)])

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Carousel'
        verbose_name = "轮播图"
        verbose_name_plural = "轮播图"
        unique_together = (("category", "sequence"),)
        ordering = ['sequence']
        index_together = ["category"]
