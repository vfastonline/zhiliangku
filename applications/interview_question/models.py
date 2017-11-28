#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models

from lib.storage import ImageStorage


class InterviewQuestions(models.Model):
    """面试题"""
    company = models.CharField('公司名称', max_length=256)
    position = models.CharField('职位', max_length=256)
    amount = models.PositiveIntegerField('面试题数量', default=0)
    lowest_monthly_salary = models.CharField('最低月薪', max_length=256)
    highest_monthly_salary = models.CharField('最高月薪', max_length=256)
    question_img = models.ImageField('面试题图片', upload_to='interview_questions/img/%Y/%m/%d', storage=ImageStorage())

    def __unicode__(self):
        return self.company

    class Meta:
        db_table = 'InterviewQuestions'
        verbose_name = "企业面试题"
        verbose_name_plural = "企业面试题"
