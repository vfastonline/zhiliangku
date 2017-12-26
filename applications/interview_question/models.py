#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField

from applications.custom_user.models import CustomUser
from lib.storage import ImageStorage


class InterviewQuestions(models.Model):
    """企业面试题"""
    company = models.CharField('公司名称', max_length=256)
    email = models.CharField('公司HR邮箱', max_length=256, default="")
    position = models.CharField('职位', max_length=256)
    amount = models.PositiveIntegerField('题目数', default=0)
    lowest_monthly_salary = models.CharField('最低月薪', max_length=256)
    highest_monthly_salary = models.CharField('最高月薪', max_length=256)
    question_img = models.ImageField('面试题图片', upload_to='interview_questions/%Y%m%d', storage=ImageStorage())
    detail = models.TextField(verbose_name="面试题介绍", default="")
    notes = models.TextField(verbose_name="评测须知", default="")
    duration = models.PositiveIntegerField("评测时长", default=30)

    def __unicode__(self):
        return self.company

    class Meta:
        db_table = 'InterviewQuestions'
        verbose_name = "企业面试题"
        verbose_name_plural = "企业面试题"


class CompletedInterviewQuestion(models.Model):
    """已完成企业面试题"""
    interview_question = models.ForeignKey(InterviewQuestions, verbose_name="企业面试题")
    customuser = models.ForeignKey(CustomUser, verbose_name="完成用户")

    def __unicode__(self):
        return self.customuser

    class Meta:
        db_table = 'CompletedInterviewQuestion'
        verbose_name = "用户已完成企业面试题"
        verbose_name_plural = "用户已完成企业面试题"


class ExaminationQuestion(models.Model):
    RIGHTANSWER = (
        ("1", "A"),
        ("2", "B"),
        ("3", "C"),
        ("4", "D"),
    )
    QTYPE = (
        ("1", "选择题"),
        ("2", "编程题"),
    )
    interview_question = models.ForeignKey(InterviewQuestions, verbose_name='所属面试题',
                                           related_name='ExaminationQuestions')
    qtype = models.CharField('考题类型', max_length=1, choices=QTYPE)
    title = models.CharField('问题内容', max_length=255)
    right_answer = MultiSelectField('正确答案', max_length=5, choices=RIGHTANSWER, help_text="可单选，可多选。")

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'ExaminationQuestion'
        verbose_name = "面试题"
        verbose_name_plural = "面试题"
        ordering = ["interview_question"]
        index_together = ["interview_question"]


class ExaminationAnswer(models.Model):
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
