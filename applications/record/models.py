#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models

from applications.custom_user.models import CustomUser
from applications.tracks_learning.models import Video, Course


class WatchRecord(models.Model):
    """用户观看记录表"""
    STATUS = (
        (1, '已看完'),
        (0, '未看完')
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='用户')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, verbose_name='视频')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    video_process = models.IntegerField('观看时间', default=0, help_text="秒")
    duration = models.IntegerField('时长', default=0, help_text="单位：秒")
    status = models.IntegerField('观看状态', choices=STATUS, default=0)
    create_time = models.DateTimeField(verbose_name='记录时间', auto_now=True)

    def __unicode__(self):
        return self.user.nickname + "|" + self.course.name

    class Meta:
        db_table = 'WatchRecord'
        verbose_name = "学生观看视频记录"
        verbose_name_plural = "学生观看视频记录"

# class WatchCourse(models.Model):
#     """记录用户那些课程都已经观看完成"""
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='用户ID')
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程ID')
#     createtime = models.CharField('记录时间', max_length=20, default='2015-09-08 12:00:00')
#
#     def __unicode__(self):
#         return self.user.nickname
#
#     class Meta:
#         db_table = 'WatchCourse'
#         verbose_name = "用户已完成课程"
#         verbose_name_plural = "用户已完成课程"
