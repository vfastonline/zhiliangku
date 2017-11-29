from django.contrib import admin

from applications.live_streaming.models import Live


class LiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pathwel', 'desc')
    search_fields = ('name',)


admin.site.register(Live, LiveAdmin)
