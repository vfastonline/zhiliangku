#!encoding:utf-8
from django.conf.urls import url

from applications.live_streaming.views import *

urlpatterns = [
    url(r'^list$', LiveList.as_view()),
]
