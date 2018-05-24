#!encoding:utf-8
import logging
import traceback

from django.contrib import admin

from applications.tracks_learning.model_form import *
from zhiliangku.settings import tinymce_js


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
	list_display = ('id', "name", "color", "desc", "video")
	search_fields = ('name',)
	form = TechnologyForm


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('id', "name", "technology", "color", "desc", "is_lock", "home_show", "pathwel", "video")
	search_fields = ('name',)

	def technology(self, obj):
		name = ""
		try:
			if obj.technology:
				name = obj.technologys.name
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return name

	technology.short_description = u"技术分类"

	class Media:
		js = tinymce_js


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ('id', "project", 'name', "lecturer", "desc", "sequence", "update_time")
	search_fields = ('name', "project__name")

	class Media:
		js = tinymce_js


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
	list_display = ('id', "project", 'course', 'title', 'sequence', "desc")
	search_fields = ("course__project__name", "course__name", 'title',)
	form = SectionForm

	def project(self, obj):
		name = ""
		try:
			if obj.course:
				name = obj.course.project.name
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return name

	project.short_description = "项目"


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	list_display = ('id', "project", "course", "section", 'name', "type", "address", "subtitle", 'sequence', "duration")
	search_fields = ("section__course__project__name", "section__course__name", "section__title", 'name')
	list_filter = ('type',)

	def project(self, obj):
		name = ""
		try:
			if obj.section:
				name = obj.section.course.project.name
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return name

	def course(self, obj):
		name = ""
		try:
			if obj.section:
				name = obj.section.course.name
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return name

	project.short_description = "项目"
	course.short_description = "课程"

	class Media:
		js = ['js/webPlugins.js'] + tinymce_js


@admin.register(UnlockVideo)
class UnlockVideoAdmin(admin.ModelAdmin):
	list_display = ('id', "video", "custom_user")
	search_fields = ("video__name", 'custom_user')


@admin.register(Nodus)
class NodusAdmin(admin.ModelAdmin):
	list_display = ('id', "video", "title", 'notes', "moment")
	search_fields = ("video__name", 'title')
	form = NodusForm

	class Media:
		js = tinymce_js


@admin.register(CommonQuestion)
class CommonQuestionAdmin(admin.ModelAdmin):
	list_display = ('id', "video", "question", 'answer')
	search_fields = ("video__name", 'question')
	form = CommonQuestionForm

	class Media:
		js = tinymce_js


@admin.register(StudentNotes)
class StudentNotesAdmin(admin.ModelAdmin):
	list_display = ('id', "video", "custom_user", "title", 'notes', "create_time")
	search_fields = ("video__name", 'title')
	form = StudentNotesForm

	class Media:
		js = tinymce_js
