from django.contrib import admin

from applications.interview_question.models import InterviewQuestions


class InterviewQuestionsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'company', 'position', 'amount', 'lowest_monthly_salary', 'highest_monthly_salary', 'question_img')
    search_fields = ('company', 'position')


admin.site.register(InterviewQuestions, InterviewQuestionsAdmin)
