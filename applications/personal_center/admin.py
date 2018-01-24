from django.contrib import admin

from applications.personal_center.model_form import *
from zhiliangku.settings import tinymce_js


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'custom_user',
        "name",
        "sex",
        "birthday",
        "years_of_service",
        "education",
        "status",
        "company",
        "position",
        "advantage",
        "career_objective",
    )
    search_fields = ("name", 'years_of_service', "education")
    form = ResumeForm

    class Media:
        js = tinymce_js


@admin.register(CareerObjective)
class CareerObjectiveAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'custom_user',
        'way',
        "position",
        "city",
        "expect_salary",
        "industry",
    )
    search_fields = ('position',)
    form = CareerObjectiveForm


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'custom_user',
        "company",
        "position",
        "start_time",
        "end_time",
        "content",
    )
    search_fields = ('company',)
    form = WorkExperienceForm

    class Media:
        js = tinymce_js


@admin.register(ProjectExperience)
class ProjectExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'custom_user',
        "name",
        "role",
        "url",
        "start_time",
        "end_time",
        "description",
        "performance",
    )
    search_fields = ('project_name',)
    form = ProjectExperienceForm

    class Media:
        js = tinymce_js


@admin.register(EducationExperience)
class EducationExperienceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'custom_user',
        "school",
        "discipline",
        "education",
        "start_time",
        "end_time",
        "experience",
    )
    search_fields = ('school',)
    form = EducationExperienceForm

    class Media:
        js = tinymce_js
