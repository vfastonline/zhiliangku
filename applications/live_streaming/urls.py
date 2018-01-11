#!encoding:utf-8
from django.conf.urls import url

from applications.live_streaming.views import *

urlpatterns = [
    url(r'^index/list$', IndexLiveList.as_view()),
]
