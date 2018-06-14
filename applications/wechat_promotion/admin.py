from django.contrib import admin
from applications.wechat_promotion.models import *


@admin.register(WechatBrowse)
class WechatBrowseAdmin(admin.ModelAdmin):
	list_display = ('id', "name", "pinyin", "remark", "page_views", "thumbs_up", "share", "create_time")
	search_fields = ('name', 'pinyin')
	readonly_fields = ("create_time")


@admin.register(WechatBackground)
class WechatBackgroundAdmin(admin.ModelAdmin):
	list_display = ('id', "sequence", "image")


@admin.register(WechatRemark)
class WechatRemarkAdmin(admin.ModelAdmin):
	list_display = ('id', "name", "remark", "english")


@admin.register(WechatMusic)
class WechatMusicAdmin(admin.ModelAdmin):
	list_display = ('id', "name", "address", "images")
	search_fields = ('name',)
