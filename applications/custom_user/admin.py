#!encoding:utf-8
from django.contrib import admin

from applications.custom_user.model_form import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nickname', "sex", 'role', "position", "receiver", "address", "signature", "integral", "create_time")
    search_fields = ('nickname',)
    list_filter = ('role', "sex")


@admin.register(CustomUserAuths)
class CustomUserAuthsAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_user_id', 'identity_type', 'identifier', "credential", "status", "create_time")
    search_fields = ('custom_user_id__nickname', "identity_type",)
    list_filter = ('status',)
    form = CustomUserAuthsForm


@admin.register(CustomUserPath)
class CustomUserPathAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_user', "path", "create_time")
    readonly_fields = ('create_time',)
    search_fields = ('custom_user__nickname', "path__name")
    form = CustomUserPathForm


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
