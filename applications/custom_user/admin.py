#!encoding:utf-8
from django.contrib import admin

from applications.custom_user.models import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', "sex", 'role', "position", 'avatar', "receiver", "address", "signature",)
    search_fields = ('nickname',)
    list_filter = ('role', "sex")


@admin.register(CustomUserAuths)
class CustomUserAuthsAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_user_id', 'identity_type', 'identifier', "credential", "status")
    search_fields = ('custom_user_id__nickname', "identity_type",)
    list_filter = ('status',)


@admin.register(CustomUserPath)
class CustomUserPathAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_user', "paths")
    search_fields = ('custom_user__nickname',)
    filter_horizontal = ('path',)

    def paths(self, obj):
        return ",".join(obj.path.all().values_list("name", flat=True))

    paths.short_description = "参与职业路径"


@admin.register(CustomUserCourse)
class CustomUserCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_user', "courses")
    search_fields = ('custom_user__nickname',)
    filter_horizontal = ('course',)

    def courses(self, obj):
        return ",".join(obj.course.all().values_list("name", flat=True))

    courses.short_description = "收藏课程"


@admin.register(VerifyCode)
class VerifyCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'code', 'create_time', "expire_time", "is_use")
    search_fields = ('phone',)
    list_filter = ('is_use',)
