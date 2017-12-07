#!encoding:utf-8
from __future__ import unicode_literals

from colorfield.fields import ColorField
from django.core.validators import MinValueValidator
from django.db import models

from lib.storage import ImageStorage
from applications.live_streaming.models import Live


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
        verbose_name = "路径"
        verbose_name_plural = "路径"


class PathStage(models.Model):
    """职业路径阶段"""
    path = models.ForeignKey(Path, verbose_name="职业路径", related_name='PathStage')
    name = models.CharField('路线阶段名称', max_length=255)
    sequence = models.PositiveIntegerField('路线阶段顺序', default=1, validators=[MinValueValidator(1)])

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'PathStage'
        verbose_name = "路径阶段"
        verbose_name_plural = "路径阶段"
        unique_together = (("path", "sequence"),)
        ordering = ['path', "sequence"]


class CourseCategory(models.Model):
    """路径阶段-课程类别"""
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
    prerequisites = models.TextField('先修要求', default="")
    learn = models.TextField('你将学到什么', default="")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Course'
        verbose_name = "课程"
        verbose_name_plural = "课程"


class CoursePath(models.Model):
    """课程方向"""
    name = models.CharField('方向名称', max_length=50)
    tech = models.ManyToManyField("Technology", verbose_name='技术分类')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'CoursePath'
        verbose_name = "方向"
        verbose_name_plural = "方向"


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


class Section(models.Model):
    """课程-章节"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='所属课程', related_name='Section')
    title = models.CharField('章节标题', max_length=100, default='')
    sequence = models.PositiveIntegerField('章节顺序')
    desc = models.TextField('章节描述', default='')

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'Section'
        verbose_name = "章节"
        verbose_name_plural = "章节"
        ordering = ['sequence']


class Video(models.Model):
    """视频"""
    TYPE = (
        ("1", "点播"),
        ("2", "直播回放"),
        ("3", "直播"),
        ("4", "题目"),
    )
    section = models.ForeignKey(Section, verbose_name='所属章节', related_name='Section', blank=True, null=True)
    type = models.CharField('视频类型', max_length=1, choices=TYPE)
    name = models.CharField('视频名称', max_length=255)
    sequence = models.PositiveIntegerField('视频顺序', default=0)
    duration = models.PositiveIntegerField('视频时长', default=1)
    live = models.ForeignKey(Live, verbose_name='直播', related_name='Live', blank=True, null=True)
    live_start_time = models.DateTimeField("直播起始时间", blank=True, null=True)
    live_end_time = models.TimeField("直播终止时间", blank=True, null=True)
    desc = models.TextField('视频描述', default='')

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Video'
        verbose_name = "视频"
        verbose_name_plural = "视频"
        ordering = ['sequence']
