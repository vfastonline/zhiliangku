#!encoding:utf-8
from __future__ import unicode_literals

import logging
import traceback

from django.db import models
from django.utils import timezone

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
    nickname = models.CharField('昵称', max_length=255, blank=True, null=True)
    role = models.IntegerField('角色', choices=ROLE, null=True, default=3)
    avatar = models.ImageField('头像', upload_to=upload_to, storage=ImageStorage(), blank=True, null=True, max_length=256)
    position = models.CharField('职位', max_length=255, blank=True, null=True)

    def __unicode__(self):
        return ",".join([self.nickname, str(self.id), str(self.get_role_display())])

    class Meta:
        db_table = 'CustomUser'
        verbose_name = "基础信息"
        verbose_name_plural = "基础信息"


class CustomUserAuths(models.Model):
    """用户授权信息"""
    IDENTITYTYPE = (
        ("phone", "phone"),
        ("email", "email"),
        ("weixin", "weixin"),
        ("weibo", "weibo"),
        ("qq", "qq"),
    )
    custom_user_id = models.ForeignKey(CustomUser, verbose_name="用户")
    identity_type = models.CharField('登录类型', choices=IDENTITYTYPE, max_length=10, help_text="手机号、邮箱、用户名或第三方应用名称微信、微博等。")
    identifier = models.CharField('唯一标识', max_length=255, help_text="手机号、邮箱、用户名或第三方应用的唯一标识。")
    credential = models.CharField('密码凭证', max_length=255, help_text="站内的保存密码，站外的不保存或保存token。")
    status = models.BooleanField("是否激活", default=True)

    def __unicode__(self):
        return self.identity_type

    class Meta:
        db_table = 'CustomUserAuths'
        verbose_name = "授权信息"
        verbose_name_plural = "授权信息"


class CustomUserPath(models.Model):
    """用户参与路径 """

    custom_user = models.OneToOneField(CustomUser, verbose_name="用户", unique=True, limit_choices_to={'role': 0},
                                       help_text='只允许选择角色是”学生“的用户。')
    path = models.ManyToManyField("tracks_learning.Path", verbose_name="职业路径", blank=True)

    def __unicode__(self):
        return self.custom_user.nickname

    class Meta:
        db_table = 'CustomUserPath'
        verbose_name = "参与路径"
        verbose_name_plural = "参与路径"


class VerifyCode(models.Model):
    """验证码"""
    phone = models.CharField("手机号", max_length=11)
    code = models.CharField("验证码", max_length=4)
    create_time = models.DateTimeField(verbose_name='生成时间', default=timezone.now)
    expire_time = models.DateTimeField("失效时间", max_length=4)
    is_use = models.BooleanField("已使用", default=False)

    def __unicode__(self):
        return self.phone + ":" + self.code

    def check_is_valid(self):
        """校验验证码是否有效
        :return:
        """
        try:
            # 已经使用过
            if self.is_use:
                return 1

        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())

    class Meta:
        db_table = 'VerifyCode'
        verbose_name = "验证码"
        verbose_name_plural = "验证码"
