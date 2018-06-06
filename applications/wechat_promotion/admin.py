from django.contrib import admin
from applications.wechat_promotion.models import WechatBrowse


@admin.register(WechatBrowse)
class WechatBrowseAdmin(admin.ModelAdmin):
	list_display = ('id', "page_views", "thumbs_up", "create_time")
