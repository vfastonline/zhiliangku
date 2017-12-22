from django.contrib import admin
from applications.community.models import *


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('id', "video", 'title', "description", "path", "reward", "user", "create_time", "browse_number")
    search_fields = ("video__name", 'user', "title")
    list_filter = ('path', "reward")
    eadonly_fields = ("browse_number",)


@admin.register(FaqAnswer)
class FaqAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', "faq", "user", 'answer', "create_time")
    search_fields = ("faq__title", 'user')
