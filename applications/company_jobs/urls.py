#!encoding:utf-8
from django.conf.urls import url

from applications.company_jobs.views import *

urlpatterns = [
    url(r'^add$', company_add),
]
