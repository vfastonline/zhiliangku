from django.contrib import admin
from applications.community.models import *


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = (
        'id', "video", 'title', "description", "reward", "user", "create_time", "browse_amount", "status")
    search_fields = ("video__name", 'user', "title")
    list_filter = ("reward", "status",)
    readonly_fields = ("browse_amount",)
    filter_horizontal = ('follow_user',)

    def suit_row_attributes(self, obj, request):
        css_class = {
            "1": 'success',
        }.get(obj.status)
        if css_class:
            return {'class': css_class}


@admin.register(FaqAnswer)
class FaqAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', "faq", "user", 'answer', "create_time", "approve", "oppose", "optimal")
    search_fields = ("faq__title", 'user')
    list_filter = ('optimal',)

    def suit_row_attributes(self, obj, request):
        css_class = {
            True: 'success',
        }.get(obj.optimal)
        if css_class:
            return {'class': css_class}


@admin.register(FaqAnswerReply)
class FaqAnswerReplyAdmin(admin.ModelAdmin):
    list_display = ('id', "faqanswer", 'reply', "user", "create_time")
    search_fields = ('user',)
