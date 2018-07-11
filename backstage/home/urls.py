#!encoding:utf-8
from django.conf.urls import url

from backstage.home.get_learn_schedule_by_date import *
from backstage.home.get_learn_task_schedule import *
from backstage.home.set_learn_task import SetLearnTaskInfo
from backstage.home.views import *

urlpatterns = [
	url('^index/$', BackStageHomePage.as_view()),  # 教室端后台首页
	url('^set/task/info$', SetLearnTaskInfo.as_view()),  # 设置今日任务-获取下拉信息
	url('^get/today/task/schedule$', GetTodayTaskScheduleInfo.as_view()),  # 获取今日预计达到目标进度百分比
	url('^get/yesterday/task/schedule$', GetYesterdayTaskScheduleInfo.as_view()),  # 获取昨日目标进度
	url('^get/learn/schedule/by/date$', GetLearnTaskScheduleBydate.as_view()),  # 根据日期获取学习任务完成进度
	url('^get/has/today/learn/task$', GetHasTodayLearnTaskInfo.as_view()),  # 当天是否有任务发布
]
