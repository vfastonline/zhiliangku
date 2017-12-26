from django.contrib import admin
from applications.community.models import *


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = (
        'id', "video", 'title', "description", "path", "reward", "user", "create_time", "browse_amount", "status")
    search_fields = ("video__name", 'user', "title")
    list_filter = ('path', "reward", "status")
    readonly_fields = ("browse_amount",)
    filter_horizontal = ('follow_user',)


@admin.register(FaqAnswer)
class FaqAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', "faq", "user", 'answer', "create_time", "approve", "oppose", "optimal")
    search_fields = ("faq__title", 'user')
    list_filter = ('optimal',)


@admin.register(FaqAnswerReply)
class FaqAnswerReplyAdmin(admin.ModelAdmin):
    list_display = ('id', "faqanswer", 'reply', "user", "create_time")
    search_fields = ('user',)
