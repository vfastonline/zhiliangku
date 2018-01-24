#!encoding:utf-8
from django.contrib import admin

from applications.tracks_learning.model_form import *
from zhiliangku.settings import tinymce_js


@admin.register(Path)
class PathAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "lowest_salary", "highest_salary", "path_img", 'desc')
    search_fields = ('name',)
    list_filter = ('home_show',)


@admin.register(PathStage)
class PathStageAdmin(admin.ModelAdmin):
    list_display = ('id', "path", 'name', "sequence")
    search_fields = ("path__name", 'name',)
    form = PathStageForm


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', "path_stage", 'name', "sequence", "courses_name")
    search_fields = ("path_stage__name", 'name',)
    filter_horizontal = ('courses',)
    form = CourseCategoryForm

    def courses_name(self, obj):
        return ",".join(obj.courses.all().values_list("name", flat=True))

    courses_name.short_description = "包含课程"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "recommend", 'lecturer', 'course_img', "prerequisites", "learn")
    search_fields = ('name',)
    list_filter = ('recommend',)
    filter_horizontal = ('tech',)
    form = CourseForm

    def suit_row_attributes(self, obj, request):
        css_class = {
            True: 'success',
        }.get(obj.recommend)
        if css_class:
            return {'class': css_class}


@admin.register(CoursePath)
class CoursePathAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    filter_horizontal = ('tech',)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'desc')
    search_fields = ('name',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'title', 'sequence', "desc")
    search_fields = ("course__name", 'title',)
    form = SectionForm


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'id', "section", 'name',
        "type", 'sequence', "duration",
        "live", "live_start_time", "vid",
    )
    search_fields = ("section__title", 'name', "live__name", "vid")
    list_filter = ('type',)
    readonly_fields = ("vid", "data",)
    form = VideoForm

    fieldsets = [
        ("视频一般信息", {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['section', "type", "name", "sequence", "duration", "desc"]
        }),
        ('直播信息', {
            'classes': ('suit-tab', 'suit-tab-live',),
            'fields': ['live', "live_start_time", "live_end_time"]}),
        ('讲师笔记', {
            'classes': ('suit-tab', 'suit-tab-notes',),
            'fields': ['notes']}),
        ('保利威视', {
            'classes': ('suit-tab', 'suit-tab-polyv',),
            'fields': ['vid', 'data']}),
    ]
    suit_form_tabs = (('general', '一般'), ('live', '直播'), ('notes', '讲师笔记'), ('polyv', '保利威视回调'))

    def suit_row_attributes(self, obj, request):
        css_class = {
            "3": 'success',
            "4": 'info',
        }.get(obj.type)
        if css_class:
            return {'class': css_class}

    class Media:
        js = ['js/webPlugins.js'] + tinymce_js


@admin.register(CommonQuestion)
class CommonQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', "video", "question", 'answer')
    search_fields = ("video__name", 'question')
    form = CommonQuestionForm

    class Media:
        js = tinymce_js
