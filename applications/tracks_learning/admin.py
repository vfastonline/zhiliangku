from django.contrib import admin

from applications.tracks_learning.models import *


class PathAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc', 'path_img')
    search_fields = ('name',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lecturer', 'course_img')
    search_fields = ('name',)
    filter_horizontal = ('tech',)


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'desc')
    search_fields = ('name',)


admin.site.register(Path, PathAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Technology, TechnologyAdmin)
