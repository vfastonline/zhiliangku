from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'index-du.html')


class Paths(TemplateView):
    template_name = 'front/tracks/paths/index.html'


class PathDetail(TemplateView):
    template_name = 'front/tracks/path/detail/index.html'


class Courses(TemplateView):
    template_name = 'front/tracks/courses/index.html'


class CourseDetail(TemplateView):
    template_name = 'front/tracks/course/detail/index.html'
