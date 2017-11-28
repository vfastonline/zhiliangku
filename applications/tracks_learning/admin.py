from django.contrib import admin
from applications.tracks_learning.models import *
from zhiliangku.settings import tinymce_js


class PathAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'desc', 'path_img')
    search_fields = ('name',)

    class Media:
        js = tinymce_js


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lecturer', 'course_img')
    search_fields = ('name',)
    filter_horizontal = ('tech',)

    class Media:
        js = tinymce_js


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'desc')
    search_fields = ('name',)

    class Media:
        js = tinymce_js


admin.site.register(Path, PathAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Technology, TechnologyAdmin)
