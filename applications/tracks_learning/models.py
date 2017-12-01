#!encoding:utf-8
from __future__ import unicode_literals

from colorfield.fields import ColorField
from applications.custom_user.models import CustomUser
from django.db import models

from lib.storage import ImageStorage


class Path(models.Model):
    """学习路线"""
    name = models.CharField('路线名称', max_length=50)
    path_img = models.ImageField('路线介绍图面', upload_to='path/%Y%m%d', storage=ImageStorage())
    desc = models.TextField('路线简介', max_length=1000, blank=True, null=True, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Path'
        verbose_name = "路线"
        verbose_name_plural = "路线"


class Course(models.Model):
    """课程"""
    name = models.CharField('课程名称', max_length=50)
    lecturer = models.ForeignKey(CustomUser, verbose_name="讲师", limit_choices_to={'role': 1}, null=True, blank=True,
                                 on_delete=models.SET_NULL, help_text='只允许选择角色是”老师“的用户信息。')
    course_img = models.ImageField('课程介绍图片', upload_to='course/%Y%m%d', storage=ImageStorage())
    tech = models.ManyToManyField("Technology", verbose_name='技术分类')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Course'
        verbose_name = "课程"
        verbose_name_plural = "课程"


class Technology(models.Model):
    """技术分类"""
    name = models.CharField('技术类别', max_length=50)
    color = ColorField('颜色', max_length=50, default='#FFFFFF')
    desc = models.TextField('技术简介', default='')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Technology'
        verbose_name = "技术分类"
        verbose_name_plural = "技术分类"
