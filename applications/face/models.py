#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models


class Watchface(models.Model):
    """记录脸部表情"""
    userid = models.FloatField()
    joy = models.FloatField()
    engagement = models.FloatField()
    sadness = models.FloatField()
    anger = models.FloatField()
    surprise = models.FloatField()
    fear = models.FloatField()
    valence = models.FloatField()
    contempt = models.FloatField()
    vtime = models.FloatField()
    disgust = models.FloatField()

    def __unicode__(self):
        return self.userid

    class Meta:
        db_table = 'Watchface'
        verbose_name = "面部表情"
        verbose_name_plural = "面部表情"
