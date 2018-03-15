#!encoding:utf-8
from django.contrib import admin

from applications.live_streaming.models import Live
from lib.polyv.live_api import getstatus_live


@admin.register(Live)
class LiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "channelId", "channelPasswd", "status", "autoPlay")
    search_fields = ('name', "channelId",)
    list_filter = ('status', "autoPlay",)
    list_editable = ['status', "name", "channelPasswd"]
    readonly_fields = ("channelId", "data",)
    actions = ["delete_selected", "get_live_status_selected"]
    list_per_page = 20

    # 批量删除所选直播
    def delete_selected(self, request, queryset):
        del_count = 0
        for one in queryset:
            delete_result = one.delete()
            if delete_result:
                del_count += 1
        self.message_user(request, "成功删除 %s 个直播." % del_count, 'success')

    # 批量获取并更新所选频道直播状态
    def get_live_status_selected(self, request, queryset):
        channelId_list = queryset.values_list("channelId", flat=True)
        channelIds = ",".join(map(str, channelId_list))
        get_result = getstatus_live(channelIds)
        code = get_result.get("code")
        data = get_result.get("data", [])
        message = get_result.get("message")
        message_bit = "批量获取频道直播状态 "
        msg_level = "success"
        if code == 200:
            [Live.objects.filter(channelId=one.get("channelId")).update(status=one.get("status")) for one in data]
            message_bit += "成功"
        else:
            message_bit += message
            msg_level = "error"
        self.message_user(request, message_bit, msg_level)

    delete_selected.short_description = " ".join(["删除所选的", Live._meta.verbose_name])
    get_live_status_selected.short_description = " ".join(["获取所选的", Live._meta.verbose_name, "状态"])

    # def pathwels(self, obj):
    #     return '<img src="%s" height="24" width="24" />' % (obj.pathwel.url)
    #
    # pathwels.allow_tags = True
    # pathwels.short_description = "直播图片"

    def suit_row_attributes(self, obj, request):
        css_class = {
            "live": 'success',
        }.get(obj.status)
        if css_class:
            return {'class': css_class}
