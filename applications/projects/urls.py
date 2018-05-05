#!encoding:utf-8
from django.conf.urls import url

from applications.projects.views import *

urlpatterns = [
    url(r'^list$', PrjectList.as_view()),
]
