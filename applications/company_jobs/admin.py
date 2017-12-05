from django.contrib import admin
from applications.company_jobs.models import Company_jobs

# Register your models here.

@admin.register(Company_jobs)
class InterviewQuestionsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'jobname', 'salary', 'work_exp', 'education', 'skillwords')
    search_fields = ('name', 'jobname')
