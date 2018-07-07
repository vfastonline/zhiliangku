from django.contrib import admin

from backstage.home.models import *


@admin.register(LearnTask)
class LearnTaskAdmin(admin.ModelAdmin):
	list_display = ('id', "video", "custom_user", "create_time", "update_time",)
	search_fields = ('video__name',)


@admin.register(LearnTaskSummary)
class LearnTaskSummaryAdmin(admin.ModelAdmin):
	list_display = (
		'id', "task", "schedule", "average", "improve", "complete", "undone", "excess_complete", "update_time")
	search_fields = ('task__video__name',)


@admin.register(UserLearnTaskSummary)
class UserLearnTaskSummaryAdmin(admin.ModelAdmin):
	list_display = (
		'id', "custom_user", "task", "schedule")
	search_fields = ('task__video__name',)
