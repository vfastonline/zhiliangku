#!encoding:utf-8
from __future__ import unicode_literals

from colorfield.fields import ColorField
from django.core.validators import MinValueValidator
from django.db import models

from lib.storage import ImageStorage


class Path(models.Model):
    """职业路径"""
    name = models.CharField('路径名称', max_length=255)
    home_show = models.BooleanField("是否首页展示", default=False, help_text="首页展示3个职业路径，请查询已勾选个数后设置。")
    lowest_salary = models.PositiveIntegerField("最低平均月薪", default=0)
    highest_salary = models.PositiveIntegerField("最高平均月薪", default=0)
    path_img = models.ImageField('路径介绍图片', upload_to='path/%Y%m%d', storage=ImageStorage())
    desc = models.TextField('路径简介', max_length=1000, blank=True, null=True, default='')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Path'
        verbose_name = "职业路径"
        verbose_name_plural = "职业路径"


class PathStage(models.Model):
    """职业路径阶段"""
    path = models.ForeignKey(Path, verbose_name="职业路径", related_name='PathStage')
    name = models.CharField('路线阶段名称', max_length=255)
    sequence = models.PositiveIntegerField('路线阶段顺序', default=1, validators=[MinValueValidator(1)])

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'PathStage'
        verbose_name = "职业路径阶段"
        verbose_name_plural = "职业路径阶段"
        unique_together = (("path", "sequence"),)
        ordering = ['sequence']


class CourseCategory(models.Model):
    """课程类别"""
    path_stage = models.ForeignKey(PathStage, verbose_name="职业路径阶段", related_name='CourseCategory')
    name = models.CharField('课程类别名称', max_length=255)
    sequence = models.PositiveIntegerField('路线阶段顺序', default=1, validators=[MinValueValidator(1)])
    courses = models.ManyToManyField("Course", verbose_name=u"包含课程", blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'CourseCategory'
        verbose_name = "课程类别"
        verbose_name_plural = "课程类别"
        unique_together = (("path_stage", "sequence"),)
        ordering = ['sequence']


class Course(models.Model):
    """课程"""
    name = models.CharField('课程名称', max_length=50)
    home_show = models.BooleanField("是否首页展示", default=False, help_text="首页展示8个热门，请查询已勾选个数后设置。")
    lecturer = models.ForeignKey("custom_user.CustomUser", verbose_name="讲师", limit_choices_to={'role': 1}, null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL, help_text='只允许选择角色是”老师“的用户。')
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
