from django.contrib import admin
from backstage.exam_statistics.models import *


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', "dates", 'class_s', "style", "nature", "number")
	search_fields = ('name',)
	list_filter = ('style', "nature")
	readonly_fields = ("create_time",)


@admin.register(ExamNatureCount)
class ExamNatureCountAdmin(admin.ModelAdmin):
	list_display = ('id', 'class_s', "nature", 'nature_id', "count",)
	search_fields = ('class_s',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
	list_display = ('id', 'exam', 'custom_user', "fraction", 'remark',)
	search_fields = ('exam', 'custom_user')
