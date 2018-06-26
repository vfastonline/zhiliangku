#!encoding:utf-8
from django.contrib import admin

from applications.custom_user.model_form import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
	list_display = ('id', 'nickname', "sex", 'role', "position", "integral", "create_time")
	search_fields = ('nickname',)
	list_filter = ('role', "sex")
	readonly_fields = ("receiver", "address", "create_time")


@admin.register(CustomUserAuths)
class CustomUserAuthsAdmin(admin.ModelAdmin):
	list_display = ('id', 'custom_user_id', 'identity_type', 'identifier', "credential", "status", "create_time")
	search_fields = ('custom_user_id__nickname', "identity_type",)
	list_filter = ('status',)
	form = CustomUserAuthsForm


@admin.register(CustomUserProject)
class CustomUserProjectAdmin(admin.ModelAdmin):
	list_display = ('id', 'custom_user', "project", "create_time")
	readonly_fields = ('create_time',)
	search_fields = ('custom_user__nickname', "path__name")
	form = CustomUserProjectForm


@admin.register(CustomUserCourse)
class CustomUserCourseAdmin(admin.ModelAdmin):
	list_display = ('id', 'custom_user', "course", 'create_time',)
	readonly_fields = ('create_time',)
	search_fields = ('custom_user__nickname', "course__name")
	form = CustomUserCourseForm


@admin.register(VerifyCode)
class VerifyCodeAdmin(admin.ModelAdmin):
	list_display = ('id', 'phone', 'code', 'create_time', "expire_time", "is_use")
	search_fields = ('phone',)
	list_filter = ('is_use',)
