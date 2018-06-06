#!encoding:utf-8
from django.conf.urls import url

from applications.medal.views import GetCustomUserMedal

urlpatterns = [
	url('^list/info$', GetCustomUserMedal.as_view()),  # 用户勋章
]
