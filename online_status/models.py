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
		verbose_name = '在线状态'
		verbose_name_plural = '在线状态'
		ordering = ['-last_login']

	def __str__(self):
		return '%s last login at UTC %s' % (self.user.nickname, self.last_login.strftime('%Y-%m-%d %H:%M'))

	@staticmethod
	def get_last_active(user_id, today=True):
		"""获取今天最后登录时间
		:param user_id: 学生角色的用户ID
		:param today: 是否查询当天最后登录时间
		:return：用户最后登录时间
		"""

		cache_key = '%s_last_login' % user_id
		# 如果缓存过期，从数据库获取last_login，并存到缓存
		cache_last_login = redis_db.get(cache_key)
		if not cache_last_login:
			filter_dict = dict(user__id=user_id)
			if today:
				today = datetime.datetime.today()
				start_date = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)
				end_date = datetime.datetime(today.year, today.month, today.day, 23, 59, 59)
				filter_dict.update({"last_login__range": (start_date, end_date)})
			online_status = OnlineStatus.objects.filter(**filter_dict).order_by("-last_login")
			if online_status.exists():
				cache_last_login = online_status.first().last_login
				redis_db.setex(cache_key, cache_last_login, settings.USER_ONLINE_TIMEOUT)

		return cache_last_login

	def is_online(self, user_id):
		"""是否在线
		:param user_id: 学生角色的用户ID
		:return: True/False
		"""
		now = timezone.now()
		try:
			if self.get_last_active(user_id) < now - datetime.timedelta(seconds=settings.USER_ONLINE_TIMEOUT):
				return False
			return True
		except:
			return False
