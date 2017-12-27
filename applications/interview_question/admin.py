from django.contrib import admin

from applications.interview_question.models import *
from zhiliangku.settings import tinymce_js


@admin.register(EnterpriseInfo)
class EnterpriseInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'company', "email", 'position', 'amount',
        'lowest_monthly_salary', 'highest_monthly_salary', "duration", "path", 'question_img', "detail", "notes"
    )
    search_fields = ('company', 'position',)

    class Media:
        js = tinymce_js


@admin.register(CompletedInterviewQuestion)
class CompletedInterviewQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'interview_question', "customuser")
    search_fields = ('interview_question', 'customuser',)


@admin.register(ExaminationQuestion)
class ExaminationQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'enterprise', "qtype", "title", "right_answer", "score")
    search_fields = ('enterprise', 'title',)


@admin.register(ExaminationAnswer)
class ExaminationAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', "option", "content")
    search_fields = ('question',)


@admin.register(AnswerRecord)
class AnswerRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', "custom_user", "result", "create_time")
    search_fields = ('question',)
    list_filter = ('result',)
