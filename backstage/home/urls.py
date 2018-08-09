#!encoding:utf-8
from django.conf.urls import url

from backstage.home.get_learn_schedule_by_date import *
from backstage.home.get_learn_task_schedule import *
from backstage.home.set_learn_task import SetLearnTaskInfo
from backstage.home.views import *
from backstage.home.get_custom_user_class import *

urlpatterns = [
	# 页面
	url('^$', BackStagePage.as_view()),  # 教室端
	url('^index/$', BackStageHomePage.as_view()),  # 首页

	# 班级
	url('^get/class$', GetCustomUserClass.as_view()),  # 获取-当前登录用户管理班级

	# 发布任务
	url('^get/has/today/learn/task$', GetHasTodayLearnTaskInfo.as_view()),  # 查询-当天是否有任务发布
	url('^set/task/info$', SetLearnTaskInfo.as_view()),  # 设置-今日任务-获取项目、课程下拉信息
	url('^get/today/task/schedule$', GetTodayTaskScheduleInfo.as_view()),  # 获取-今日预计达到目标进度百分比
	url('^get/yesterday/task/schedule$', GetYesterdayTaskScheduleInfo.as_view()),  # 获取-昨日目标进度

	# 首页图表
	url('^get/learn/schedule/by/date$', GetLearnTaskScheduleByDate.as_view()),  # 饼状图-任务进度-支持按日期查询
	url('^get/learn/schedule/by/range/date$', GetLearnTaskScheduleByRangeDate.as_view()),  # 折线图-任务进度-支持按日期查询
]
