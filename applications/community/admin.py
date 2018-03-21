#!encoding:utf-8
import traceback

from django.contrib import admin

from applications.community.models import *


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = (
        'id', "video", 'title', "description", "reward", "user", "create_time", "browse_amount", "status")
    search_fields = ("video__name", 'user__nickname', "title")
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
    search_fields = ("faq__title", 'user__nickname')
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
    search_fields = ('user__nickname',)


@admin.register(FaqAnswerFeedback)
class FaqAnswerReplyAdmin(admin.ModelAdmin):
    list_display = ('id', "faqanswer", 'user', "feedbacks")
    search_fields = ('user__nickname',)

    def feedbacks(self, obj):
        name = None
        try:

            if obj.feedback == "approve":
                name = True
            if obj.feedback == "oppose":
                name = False
        except:
            traceback.print_exc()
        finally:
            return name

    feedbacks.boolean = True
    feedbacks.short_description = "支持/反馈"
