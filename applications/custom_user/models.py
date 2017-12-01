#!encoding:utf-8
from __future__ import unicode_literals

from django.db import models

from lib.storage import ImageStorage


def upload_to(instance, fielname):
    return "/".join(["custom_user", str(instance.nickname), fielname])


class CustomUser(models.Model):
    """用户基础信息 """
    ROLE = (
        (0, '学生'),
        (1, '老师'),
        (2, 'HR'),
        (3, '其他'),
    )
    nickname = models.CharField('昵称', max_length=255, unique=True)
    role = models.IntegerField('角色', choices=ROLE, null=True, default=3)
    avatar = models.ImageField('头像', upload_to=upload_to, storage=ImageStorage(), blank=True, null=True)

    def __unicode__(self):
        return self.nickname

    class Meta:
        db_table = 'CustomUser'
        verbose_name = "用户基础信息"
        verbose_name_plural = "用户基础信息"


class CustomUserAuths(models.Model):
    """用户授权信息"""
    IDENTITYTYPE = (
        ("username", "username"),
        ("phone", "phone"),
        ("email", "email"),
        ("weixin", "weixin"),
        ("weibo", "weibo"),
        ("qq", "qq"),
    )
    custom_user_id = models.ForeignKey(CustomUser, verbose_name="用户")
    identity_type = models.CharField('登录类型', choices=IDENTITYTYPE, max_length=10)  # （手机号 邮箱 用户名）或第三方应用名称（微信 微博等）
    identifier = models.CharField('标识', max_length=255)  # （手机号 邮箱 用户名或第三方应用的唯一标识）
    credential = models.CharField('密码凭证', max_length=255)  # （站内的保存密码，站外的不保存或保存token）

    def __unicode__(self):
        return self.identity_type

    class Meta:
        db_table = 'CustomUserAuths'
        verbose_name = "用户授权信息"
        verbose_name_plural = "用户授权信息"
