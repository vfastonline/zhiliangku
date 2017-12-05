#!encoding:utf-8
from django.contrib import admin

from applications.custom_user.models import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'role', 'avatar',)
    search_fields = ('nickname',)


@admin.register(CustomUserAuths)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_user_id', 'identity_type', 'identifier', "credential")
    search_fields = ('custom_user_id__nickname', "identity_type",)


@admin.register(CustomUserPath)
class CustomUserPathAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_user', "paths")
    search_fields = ('custom_user__nickname',)
    filter_horizontal = ('path',)

    def paths(self, obj):
        return ",".join(obj.path.all().values_list("name", flat=True))

    paths.short_description = "参与职业路径"
