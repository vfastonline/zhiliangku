# encoding: utf8
import datetime
from django.conf import settings
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

from applications.custom_user.views import CryptKey
from lib.base_redis import redis_db
from lib.util import validate
from .models import OnlineStatus


class OnlineStatusMiddleware(MiddlewareMixin):

	@staticmethod
	def process_request(request, *args, **kwargs):
		token = request.COOKIES.get("token")
		if token:
			today = datetime.datetime.today()
			start_date = datetime.datetime(today.year, today.month, today.day, 0, 0, 0)
			end_date = datetime.datetime(today.year, today.month, today.day, 23, 59, 59)

			validate_result = validate(token, CryptKey)
			uid = validate_result.get("uid", 0)
			if uid:
				redis_key = '%s_last_login' % uid
				now = timezone.now()

				# 用户是第一次登录、或者是缓存过期、或者是服务器重启导致缓存消失
				if not redis_db.get(redis_key):
					# print('#### cache not found #####')
					online_status = OnlineStatus.objects.filter(user__id=uid, last_login__range=(start_date, end_date))
					if online_status.exists():
						online_status.update(last_login=now)
						redis_db.setex(redis_key, now, settings.USER_ONLINE_TIMEOUT)  # 缓存5分钟
					else:
						OnlineStatus.objects.create(user__id=uid)
						redis_db.setex(redis_key, now, settings.USER_ONLINE_TIMEOUT)  # 缓存5分钟
		return None
