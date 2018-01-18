#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField

from applications.custom_user.models import CustomUser
from applications.tracks_learning.models import CoursePath
from lib.storage import ImageStorage


class EnterpriseInfo(models.Model):
    """企业面信息"""
    company = models.CharField('公司名称', max_length=256)
    email = models.CharField('公司HR邮箱', max_length=256, default="")
    position = models.CharField('招聘职位', max_length=256)
    lowest_monthly_salary = models.CharField('最低月薪', max_length=256)
    highest_monthly_salary = models.CharField('最高月薪', max_length=256)
    duration = models.PositiveIntegerField("评测时长", default=30, help_text="单位：分钟")
    path = models.ForeignKey(CoursePath, verbose_name='方向', blank=True, null=True)
    question_img = models.ImageField('面试题图片', upload_to='interview_questions/%Y%m%d', storage=ImageStorage())
    detail = models.TextField(verbose_name="面试题介绍", default="")
    notes = models.TextField(verbose_name="评测须知", default="")

    def __unicode__(self):
        return self.company

    class Meta:
        db_table = 'EnterpriseInfo'
        verbose_name = "企业信息"
        verbose_name_plural = "企业信息"


class ExaminationQuestion(models.Model):
    RIGHTANSWER = (
        ("1", "A"),
        ("2", "B"),
        ("3", "C"),
        ("4", "D"),
    )
    QTYPE = (
        ("1", "单选题"),
        ("2", "多选题"),
        ("3", "编程题"),
        ("4", "判断题"),
    )
    enterprise = models.ForeignKey(EnterpriseInfo, verbose_name='所属企业', related_name='ExaminationQuestions')
    qtype = models.CharField('考题类型', max_length=1, choices=QTYPE)
    title = models.CharField('问题内容', max_length=255)
    right_answer = MultiSelectField('正确答案', max_length=5, choices=RIGHTANSWER, help_text="可单选，可多选。", blank=True)
    score = models.PositiveIntegerField('得分', default=10)
    tech = models.ManyToManyField("tracks_learning.Technology", verbose_name='技术分类-知识点', blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'ExaminationQuestion'
        verbose_name = "面试题"
        verbose_name_plural = "面试题"
        ordering = ["enterprise"]
        index_together = ["enterprise"]


class ExaminationAnswer(models.Model):
    """选择题选项"""
    RIGHTANSWER = (
        ("1", "A"),
        ("2", "B"),
        ("3", "C"),
        ("4", "D"),
    )
    question = models.ForeignKey(ExaminationQuestion, verbose_name='所属面试题', related_name='ExaminationAnswers')
    option = models.CharField('选项', max_length=1, choices=RIGHTANSWER)
    content = models.CharField('内容', max_length=255)

    def __unicode__(self):
        return self.content

    class Meta:
        db_table = 'ExaminationAnswer'
        verbose_name = "选择题选项"
        verbose_name_plural = "选择题选项"
        ordering = ["question", 'option']
        unique_together = (("question", "option"),)


class AnswerRecord(models.Model):
    """答题记录"""
    question = models.ForeignKey(ExaminationQuestion, verbose_name='所属面试题', related_name='AnswerRecords')
    custom_user = models.ForeignKey(CustomUser, verbose_name="答题用户")
    result = models.BooleanField("正确/错误", default=False, blank=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    def __unicode__(self):
        return self.question.title

    class Meta:
        db_table = 'AnswerRecord'
        verbose_name = "答题记录"
        verbose_name_plural = "答题记录"
        ordering = ["question", '-create_time']


class CompletedInterviewQuestion(models.Model):
    """已完成企业面试题"""
    interview_question = models.ForeignKey(EnterpriseInfo, verbose_name="企业面试题",
                                           related_name="CompletedInterviewQuestions")
    customuser = models.ForeignKey(CustomUser, verbose_name="完成用户")
    complete = models.BooleanField("是否完成", default=False)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now=True)

    def __unicode__(self):
        return self.customuser.nickname

    class Meta:
        db_table = 'CompletedInterviewQuestion'
        verbose_name = "已完成面试题"
        verbose_name_plural = "已完成面试题"
        ordering = ["interview_question", '-create_time']
