#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models
from applications.tracks_learning.models import Section


class Question(models.Model):
    RIGHTANSWER = (
        ("1", "A"),
        ("2", "B"),
        ("3", "C"),
        ("4", "D"),
    )
    section = models.ForeignKey(Section, verbose_name='所属章节', related_name='Questions')
    title = models.CharField('问题内容', max_length=255)
    right_answer = models.CharField('正确答案', max_length=1, choices=RIGHTANSWER)
    detail = models.CharField('习题详解', max_length=255)
    sequence = models.PositiveIntegerField('习题顺序', default=0)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'Question'
        verbose_name = "习题"
        verbose_name_plural = "习题"
        ordering = ["section", 'sequence']
        index_together = ["section"]


class Answer(models.Model):
    RIGHTANSWER = (
        ("1", "A"),
        ("2", "B"),
        ("3", "C"),
        ("4", "D"),
    )
    question = models.ForeignKey(Question, verbose_name='所属习题', related_name='Answers')
    option = models.CharField('选项', max_length=1, choices=RIGHTANSWER)
    content = models.CharField('内容', max_length=255)

    def __unicode__(self):
        return self.content

    class Meta:
        db_table = 'Answer'
        verbose_name = "答案"
        verbose_name_plural = "答案"
        ordering = ["question", 'option']
        unique_together = (("question", "option"),)
