#!encoding:utf-8
from django.conf.urls import url

from backstage.home.views import *

urlpatterns = [
	url('^index/$', BackStageHomePage.as_view()),  # 教室端后台首页
	url('^set/task/info$', SetTaskInfo.as_view()),  # 设置今日任务-获取下拉信息
]
