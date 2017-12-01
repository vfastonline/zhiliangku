from django.contrib import admin

from applications.tracks_learning.models import *


@admin.register(Path)
class PathAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc', 'path_img')
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lecturer', 'course_img')
    search_fields = ('name',)
    filter_horizontal = ('tech',)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'desc')
    search_fields = ('name',)
