from django.contrib import admin
from applications.projects.models import *

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "name", "desc", "pathwel")
    search_fields = ('title',)
