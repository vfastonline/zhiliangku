#!encoding:utf-8
from django.contrib import admin

from applications.medal.model_form import *


@admin.register(Medal)
class MedalAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', "pathwel")
	search_fields = ('name',)
	form = CustomUserMedalForm


@admin.register(CustomUserMedal)
class CustomUserMedalAdmin(admin.ModelAdmin):
	list_display = ('id', 'custom_user', "medal", "create_time")
	search_fields = ('custom_user__nickname', "medal__name",)
	form = MedalForm
