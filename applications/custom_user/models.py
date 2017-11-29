#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models

from lib.storage import ImageStorage


def upload_to(instance, fielname):
    return "/".join(["user", instance.username, fielname])


class CustomUser(models.Model):
    ROLE = (
        (0, '学生'),
        (1, '老师'),
        (2, 'HR'),
        (3, '其他'),
    )
    username = models.CharField('用户名', max_length=255)
    password = models.CharField('密码', max_length=255)
    role = models.IntegerField('用户角色', choices=ROLE, null=True, default=3)
    user_img = models.ImageField('用户头像', upload_to=upload_to, storage=ImageStorage(), blank=True, null=True)

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = 'CustomUser'
        verbose_name = "用户"
        verbose_name_plural = "用户"
