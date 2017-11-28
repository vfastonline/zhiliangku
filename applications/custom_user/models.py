#!encoding:utf-8
from __future__ import unicode_literals

import os

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db import models

from lib.storage import ImageStorage
from zhiliangku.settings import MEDIA_ROOT


class ProfileBase(type):
    def __new__(cls, name, bases, attrs):
        module = attrs.pop('__module__')
        parents = [b for b in bases if isinstance(b, ProfileBase)]
        if parents:
            fields = []
            for obj_name, obj in attrs.items():
                if isinstance(obj, models.Field): fields.append(obj_name)
                User.add_to_class(obj_name, obj)
            UserAdmin.fieldsets = list(UserAdmin.fieldsets)
            UserAdmin.fieldsets.append((name, {'fields': fields}))
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)


class Profile(object):
    __metaclass__ = ProfileBase


def upload_to(instance, fielname):
    return "/".join(["user", instance.username, fielname])


class MyProfile(Profile):
    ROLE = (
        (0, '学生'),
        (1, '老师'),
        (2, 'HR'),
        (3, '其他'),
    )
    role = models.IntegerField('用户角色', choices=ROLE, null=True, default=3)
    nickname = models.CharField('用户昵称', max_length=50, null=True, blank=True)
    user_img = models.ImageField('用户头像', upload_to=upload_to, storage=ImageStorage(), blank=True, null=True)

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = "补充信息"
        verbose_name_plural = "补充信息"
