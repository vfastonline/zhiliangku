import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone

from applications.custom_user.models import CustomUser
from lib.base_redis import redis_db


class OnlineStatus(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	last_login = models.DateTimeField(default=timezone.now)

	class Meta:
		db_table = 'OnlineStatus'
		verbose_name = 'Online Status'
		verbose_name_plural = 'Online Status'
		ordering = ['-last_login']

	def __str__(self):
		return '%s last login at UTC %s' % (self.user.nickname, self.last_login.strftime('%Y-%m-%d %H:%M'))

	def get_last_active(self):
		"""获取最后登录时间
		:return:
		"""
		cache_key = '%s_last_login' % self.user.id
		# 如果缓存过期，从数据库获取last_login，并存到缓存
		cache_last_login = redis_db.get(cache_key)
		if not cache_last_login:
			redis_db.setex(cache_key, self.last_login, settings.USER_ONLINE_TIMEOUT)
			cache_last_login = self.last_login
		return cache_last_login

	def is_online(self):
		"""是否在线
		:return: True/Flase
		"""
		now = timezone.now()
		if self.get_last_active() < now - datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT):
			return False
		return True
