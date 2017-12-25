from django.contrib import admin
from applications.exercise.models import *


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', "section", 'title', "right_answer", "detail", "sequence")
    search_fields = ('section', "title")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', "question", 'option', "content")
    search_fields = ('question',)
