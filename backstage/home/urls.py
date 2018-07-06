#!encoding:utf-8
from django.conf.urls import url

from backstage.home.get_learn_schedule_by_date import *
from backstage.home.get_learn_task_schedule import *
from backstage.home.set_learn_task import SetLearnTaskInfo
from backstage.home.views import *

urlpatterns = [
	url('^index/$', BackStageHomePage.as_view()),  # 教室端后台首页
	url('^set/task/info$', SetLearnTaskInfo.as_view()),  # 设置今日任务-获取下拉信息
	url('^get/today/task/schedule$', GetTodayTaskScheduleInfo.as_view()),
	url('^get/yesterday/task/schedule$', GetYesterdayTaskScheduleInfo.as_view()),
	url('^get/learn/schedule/by/date$', GetLearnTaskScheduleBydate.as_view()),
]
