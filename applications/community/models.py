#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from applications.tracks_learning.models import *


class Faq(models.Model):
    PATH = (
        ("1", "一般问题"),
        ("2", "前端开发"),
        ("3", "后端开发"),
        ("4", "云计算&大数据"),
        ("5", "人工智能"),
        ("6", "运维"),
    )

    REWARD = (
        ("0", "不悬赏"),
        ("2", "2积分"),
        ("3", "3积分"),
        ("4", "4积分"),
        ("5", "5积分"),
    )

    video = models.ForeignKey(Video, verbose_name="视频", limit_choices_to={'type__in': [1, 2]}, related_name="VideoFaq",
                              blank=True, null=True)
    user = models.ForeignKey(CustomUser, verbose_name="提问用户", related_name="CustomUserFaq")
    title = models.CharField(max_length=200, verbose_name='标题')
    description = models.TextField(verbose_name='问题描述')
    path = models.CharField('问题方向', max_length=1, choices=PATH, default=1)
    reward = models.CharField('悬赏', max_length=1, choices=REWARD, default=0)
    create_time = models.DateTimeField(verbose_name='提问时间', auto_now=True)
    browse_number = models.PositiveIntegerField('浏览次数', default=0)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'Faq'
        verbose_name = "问题"
        verbose_name_plural = "问题"


class FaqAnswer(models.Model):
    faq = models.ForeignKey(Faq, verbose_name="问答题目", related_name="FaqAnswer")
    user = models.ForeignKey(CustomUser, verbose_name="回答用户", related_name="CustomUserFaqAnswer")
    answer = models.TextField(verbose_name='回答')
    create_time = models.DateTimeField(verbose_name='提问时间', auto_now=True)

    def __unicode__(self):
        return self.faq.title

    class Meta:
        db_table = 'FaqAnswer'
        verbose_name = "问题回答"
        verbose_name_plural = "问题回答"
