from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'index-du.html')


class Paths(TemplateView):
    template_name = 'pathlist.html'


class Courses(TemplateView):
    template_name = 'courseSelect.html'
