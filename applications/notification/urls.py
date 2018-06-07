#!encoding:utf-8
from django.conf.urls import url

from applications.notification.views import *

urlpatterns = [
	url('^list/$', MyNotification.as_view()),  # 用户消息-页面
	url('^list/info$', MyNotificationInfo.as_view()),  # 用户消息
	url('^delete$', DeleteMyNotification.as_view()),  # 删除-用户消息
	url('^markasread$', MarkAsReadMyNotification.as_view()),  # 标记已读-用户消息
	url('^unread/count$', MyNotificationUnreadCount.as_view()),  # 未读消息总数
]
