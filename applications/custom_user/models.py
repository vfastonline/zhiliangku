#!encoding:utf-8
from __future__ import unicode_literals

import logging
import os
import traceback

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from lib.storage import ImageStorage


def upload_to(instance, fielname):
	return os.path.join("custom_user_avatar", str(instance.id), fielname)


class CustomUser(models.Model):
	"""用户基础信息 """
	ROLE = (
		(0, '学生'),
		(1, '老师'),
		(2, 'HR'),
		(3, '其他'),
	)
	GENDER_CHOICES = (
		('M', u'男'),
		('F', u'女'),
	)

	nickname = models.CharField('昵称', max_length=255, blank=True, null=True)
	sex = models.CharField("性别", max_length=2, choices=GENDER_CHOICES, blank=True)
	role = models.IntegerField('角色', choices=ROLE, null=True, default=3)
	avatar = models.ImageField('头像', upload_to=upload_to, storage=ImageStorage(), blank=True, null=True, max_length=256,
							   default="custom_user_avatar/defaultUserIcon.png")
	institutions = models.CharField('院校', max_length=255, blank=True, null=True)
	position = models.CharField('职位', max_length=255, blank=True, null=True)
	contact_number = models.CharField('联系电话', max_length=255, blank=True, null=True, default="")
	signature = models.TextField('个性签名', max_length=255, default="", null=True, blank=True)
	integral = models.PositiveIntegerField("积分", default=10)  # 隐藏
	receiver = models.CharField('收货人', max_length=255, blank=True, null=True, default="")  # 隐藏
	address = models.CharField('收货地址', max_length=255, blank=True, null=True, default="")  # 隐藏
	create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)

	def __unicode__(self):
		return ",".join([self.nickname, str(self.id), str(self.get_role_display())])

	class Meta:
		db_table = 'CustomUser'
		verbose_name = "基础信息"
		verbose_name_plural = "基础信息"
		ordering = ["-create_time"]


@receiver(post_save, sender=CustomUser)  # 信号的名字，发送者
def add_customuser_event(sender, instance, **kwargs):  # 回调函数，收到信号后的操作
	"""注册新的用户时，默认增加一个简历信息
	:param sender:
	:param instance:
	:param kwargs:
	:return:
	"""
	from applications.personal_center.models import Resume
	from applications.notification.models import UserNotificationsCount
	try:
		Resume.objects.get_or_create(custom_user=instance)  # 默认增加一个简历
		UserNotificationsCount.objects.get_or_create(custom_user=instance)  # 增加未读消息信息
	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())


class CustomUserAuths(models.Model):
	"""用户授权信息"""
	IDENTITYTYPE = (
		("phone", "phone"),
		("email", "email"),
		("weixin", "weixin"),
		("qq", "qq"),
	)
	custom_user_id = models.ForeignKey(CustomUser, verbose_name="用户")
	identity_type = models.CharField('登录类型', choices=IDENTITYTYPE, max_length=10, help_text="手机号、邮箱、用户名或第三方应用名称微信、微博等。")
	identifier = models.CharField('唯一标识', max_length=255, help_text="手机号、邮箱、用户名或第三方应用的唯一标识。")
	credential = models.CharField('密码凭证', max_length=255, help_text="站内的保存密码，站外的不保存或保存token。")
	status = models.BooleanField("是否激活", default=True)
	create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)

	def __unicode__(self):
		return self.identity_type

	class Meta:
		db_table = 'CustomUserAuths'
		verbose_name = "授权信息"
		verbose_name_plural = "授权信息"
		ordering = ["-create_time", "custom_user_id"]


class CustomUserProject(models.Model):
	"""用户参与项目 """

	custom_user = models.ForeignKey(CustomUser, verbose_name="用户", limit_choices_to={'role': 0},
									help_text='只允许选择角色是”学生“的用户。')
	project = models.ForeignKey("tracks_learning.Project", verbose_name="参与项目", blank=True, null=True)
	create_time = models.DateTimeField(verbose_name='参与时间', default=timezone.now)

	def __unicode__(self):
		return self.custom_user.nickname

	class Meta:
		db_table = 'CustomUserProject'
		verbose_name = "参与项目"
		verbose_name_plural = "参与项目"
		ordering = ["-create_time"]


class CustomUserCourse(models.Model):
	"""用户收藏课程 """

	custom_user = models.ForeignKey(CustomUser, verbose_name="用户", limit_choices_to={'role': 0},
									help_text='只允许选择角色是”学生“的用户。')
	course = models.ForeignKey("tracks_learning.Course", verbose_name="课程", blank=True, null=True)
	create_time = models.DateTimeField(verbose_name='收藏时间', default=timezone.now)

	def __unicode__(self):
		return self.custom_user.nickname

	class Meta:
		db_table = 'CustomUserCourse'
		verbose_name = "收藏课程"
		verbose_name_plural = "收藏课程"
		ordering = ["-create_time"]


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
