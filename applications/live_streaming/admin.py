from django.contrib import admin
from applications.live_streaming.models import Live
from zhiliangku.settings import tinymce_js


class LiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pathwel', 'desc')
    search_fields = ('name',)

    class Media:
        js = tinymce_js


admin.site.register(Live, LiveAdmin)
