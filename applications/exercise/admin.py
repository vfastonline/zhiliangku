from django.contrib import admin

from applications.exercise.models import *
from zhiliangku.settings import tinymce_js


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', "video", 'title', "right_answer", "detail")
    search_fields = ('video', "title")

    class Media:
        js = tinymce_js


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', "question", 'option', "content")
    search_fields = ('question',)

    class Media:
        js = tinymce_js
