#!encoding:utf-8
from __future__ import unicode_literals

import logging
import traceback

from django.db import models
from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone

from applications.custom_user.models import CustomUser


class Notification(models.Model):
	"""消息通知
	- `custom_user`: 消息所有人的用户
	- `title`: 消息标题
	- `content`: 消息内容
	- `create_time`: 消息创建时间
	- `have_read`: 消息是否已读
	"""

	custom_user = models.ForeignKey(CustomUser, verbose_name="用户", related_name='NotificationCustomUser', db_index=True)
	title = models.CharField('标题', max_length=255, default="", db_index=True)
	content = models.TextField('内容', max_length=255, default="")
	create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
	have_read = models.BooleanField("已读", default=False)

	def __unicode__(self):
		return '<Notification %s: %s>' % (self.custom_user.id, self.title)

	class Meta:
		db_table = 'Notification'
		verbose_name = "消息通知"
		verbose_name_plural = "消息通知"
		ordering = ["-create_time"]


class UserNotificationsCount(models.Model):
	"""用户的未读消息数目
	- `custom_user`: 消息所有人的用户
	- `have_read`: 消息未读个数
	"""

	custom_user = models.ForeignKey(CustomUser, verbose_name="用户", db_index=True)
	unread_count = models.IntegerField("未读消息数", default=0)

	def __unicode__(self):
		return '<UserNotificationsCount %s: %s>' % (self.custom_user.id, self.unread_count)

	class Meta:
		db_table = 'UserNotificationsCount'
		verbose_name = "用户未读消息"
		verbose_name_plural = "用户未读消息"


class NotificationController(object):
	"""消息通知计数器
	为了让计数器正常工作，必须实时更新它，这包括：
	当有新的未读消息过来的时候，为计数器 +1
	当消息被异常删除时，如果关联的消息为未读，为计数器 -1
	当阅读完一个新消息的时候，为计数器 -1
	"""

	def __init__(self, custom_user):
		self.custom_user = custom_user

	def update_unread_count(self, count):
		"""使用Update语句来更新我们的计数器
		:param count: 未读数
		:return:
		"""
		try:
			update_param = {
				"unread_count": F('unread_count') + count
			}
			usernotificationscount = UserNotificationsCount.objects.filter(custom_user=self.custom_user)
			if usernotificationscount.exists():
				usernotificationscount.update(**update_param)
			else:
				UserNotificationsCount.objects.get_or_create(custom_user=self.custom_user)
				usernotificationscount.update(**update_param)
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())

	def mark_as_read(self, notification_id, whole=False):
		""" 标记为已读
		:param notification_id:消息ID
		:param whole:全部
		:return:
		"""
		if whole:
			filer_param = {
				"custom_user": self.custom_user,
				"have_read": False
			}
			affected_rows = Notification.objects.filter(**filer_param).update(have_read=True)
		else:
			affected_rows = Notification.objects.filter(pk=notification_id, have_read=False).update(have_read=True)
		# affected_rows将会返回update语句修改的条目数
		if affected_rows:
			self.update_unread_count(-affected_rows)


@receiver(post_save, sender=Notification)
def increment_notifications_counter(sender, instance, created, **kwargs):
	"""当有新的未读消息过来的时候，为计数器 +1
	:param sender:
	:param instance:
	:param created:
	:param kwargs:
	:return:
	"""
	try:
		# 只有当这个instance是新创建，而且have_read是默认的false才更新
		if not (created and not instance.have_read):
			return
		# 调用 update_unread_count 方法来更新计数器 +1
		NotificationController(instance.custom_user).update_unread_count(1)
	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())


@receiver(post_delete, sender=Notification)
def decrease_notifications_counter(sender, instance, **kwargs):
	"""当删除的消息还没有被读过时，计数器 -1
	:param sender:
	:param instance:
	:param kwargs:
	:return:
	"""
	try:
		if not instance.have_read:
			NotificationController(instance.custom_user).update_unread_count(-1)
	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())
