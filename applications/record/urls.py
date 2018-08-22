#!encoding:utf-8
from django.conf.urls import url
from applications.record.class_conunt import *
from applications.record.class_record import *
from applications.record import views

urlpatterns = [
	url('^handle/watchrecord$', views.HandleWatchRecord.as_view()),
	url('^handle/classrecord', ClassRecord.as_view()),
	url('^handle/classcount', ClassCountRecord.as_view()),


]
