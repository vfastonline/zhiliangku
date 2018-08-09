#!encoding:utf-8
from django.conf.urls import url

from backstage.student_list.views import *


urlpatterns = [
	# 学员列表
	url('^studentlist$', StudentList.as_view()),  # 学员列表信息
]
