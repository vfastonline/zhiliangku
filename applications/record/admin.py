from django.contrib import admin
from applications.record.models import WatchRecord


@admin.register(WatchRecord)
class WatchRecordAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', "video", 'course', 'video_process',
        'duration', 'status', 'create_time'
    )
    search_fields = ('user__nickname', 'video__name', 'course__name',)
    list_filter = ('status',)

    def suit_row_attributes(self, obj, request):
        css_class = {
            1: 'success',
        }.get(obj.status)
        if css_class:
            return {'class': css_class}
