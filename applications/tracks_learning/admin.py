#!encoding:utf-8
from django.contrib import admin

from applications.tracks_learning.models import *


@admin.register(Path)
class PathAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "lowest_salary", "highest_salary", "path_img", 'desc')
    search_fields = ('name',)
    list_filter = ('home_show',)


@admin.register(PathStage)
class PathStageAdmin(admin.ModelAdmin):
    list_display = ('id', "path", 'name', "sequence")
    search_fields = ("path__name", 'name',)


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', "path_stage", 'name', "sequence", "courses_name")
    search_fields = ("path_stage__name", 'name',)
    filter_horizontal = ('courses',)

    def courses_name(self, obj):
        return ",".join(obj.courses.all().values_list("name", flat=True))

    courses_name.short_description = "包含课程"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lecturer', 'course_img', "prerequisites", "learn")
    search_fields = ('name',)
    filter_horizontal = ('tech',)


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


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'id', "section", 'name',
        "type", 'sequence', "duration",
        "live", "live_start_time", "live_end_time", "desc"
    )
    search_fields = ("section__title", 'name', "live__name")
    list_filter = ('type',)

    class Media:
        js = ['js/webPlugins.js']
