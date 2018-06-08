#!encoding:utf-8
from django.contrib import admin

from applications.notification.model_form import *


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
	list_display = ('id', 'custom_user', "title", "content", "create_time", "have_read")
	search_fields = ('custom_user', "title",)
	form = NotificationForm
	list_filter = ('have_read',)


@admin.register(UserNotificationsCount)
class UserNotificationsCountAdmin(admin.ModelAdmin):
	list_display = ('id', 'custom_user', "unread_count")
	search_fields = ('custom_user',)
	form = UserNotificationsCountForm
