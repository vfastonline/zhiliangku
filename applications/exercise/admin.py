from django.contrib import admin

from applications.exercise.model_form import *
from zhiliangku.settings import tinymce_js


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('id', "video", 'title', "right_answer", "detail")
	search_fields = ('video__name', "title")
	form = QuestionForm

	class Media:
		js = tinymce_js


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
	list_display = ('id', "question", 'option', "content")
	search_fields = ('question__title',)
	form = AnswerForm

	class Media:
		js = tinymce_js


@admin.register(UserExercise)
class UserExerciseAdmin(admin.ModelAdmin):
	list_display = ('id', "custom_user", 'video', "times", "is_pass")
	search_fields = ('custom_user__nickname', "video__name",)
