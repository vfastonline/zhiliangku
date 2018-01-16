#!encoding:utf-8
from django.conf.urls import url

from applications.record import views

urlpatterns = [
    url('^handle/watchrecord$', views.HandleWatchRecord.as_view()),

]
