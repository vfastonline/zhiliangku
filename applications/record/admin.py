from django.contrib import admin
from applications.record.models import WatchRecord


@admin.register(WatchRecord)
class WatchRecordAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', "video", 'course', 'video_process',
        'duration', 'status', 'create_time'
    )
    search_fields = ('user', 'video', 'course',)
