#!encoding:utf-8
from django.contrib import admin

from applications.custom_user.models import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'role', "position", 'avatar',)
    search_fields = ('nickname',)
    list_filter = ('role',)


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
