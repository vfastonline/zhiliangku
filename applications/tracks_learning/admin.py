#!encoding:utf-8
import logging
import traceback
from itertools import chain

from django.contrib import admin

from applications.tracks_learning.model_form import *
from zhiliangku.settings import tinymce_js


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
	list_display = ('id', "name", "desc", "video")
	search_fields = ('name',)
	form = TechnologyForm


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('id', "name", "technology", "sequence", "is_lock", "home_show", "pathwel", "video")
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
	list_display = (
		'id', "project", "course",
		"section", 'name', "type", "address",
		"subtitle", 'sequence', "duration", "vid")
	search_fields = ("section__course__project__name", "section__course__name", "section__title", 'name', "vid")
	list_filter = ('type',)
	readonly_fields = ("vid", "data",)

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

	fieldsets = [

		('视频/练习题', {
			'classes': ('suit-tab', 'suit-tab-video',),
			'fields': ['section', "type", 'name', 'address', 'subtitle', "sequence", "duration", "desc", "notes"]}),

		('考核信息', {
			'classes': ('suit-tab', 'suit-tab-assessment',),
			'fields': ['topic', "shell", "docker", "assess_time"]}),

		('保利威视', {
			'classes': ('suit-tab', 'suit-tab-polyv',),
			'fields': ['vid', 'data']}),
	]
	suit_form_tabs = (('video', '视频/练习题'), ('assessment', '考核'), ('polyv', '保利威视'))

	def suit_row_attributes(self, obj, request):
		css_class = {
			"2": 'success',
			"3": 'info',
		}.get(obj.type)
		if css_class:
			return {'class': css_class}

	class Media:
		# js = ['js/webPlugins.js'] + tinymce_js + ["layer/layer.js"]
		js = list(chain(['js/webPlugins.js'], tinymce_js, ["layer/layer.js"]))


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
