#!encoding:utf-8
from django.conf.urls import url
from applications.record.class_conunt import *
from applications.record.class_record import *
from applications.record.add_watch_video import *
from applications.record.today_edu_data import *
from applications.record.class_data_pic import *


urlpatterns = [

	url('^handle/watch/record$', HandleWatchRecord.as_view()),#增加视频的观看记录
	url('^handle/class/record$', ClassRecord.as_view()),   #班级学习统计
	url('^handle/class/count$', ClassCountRecord.as_view()),#视频统计详情页
	url('^handle/edu/data$', TodayEduData.as_view()),  #今日教务数据
	url('^handle/data/graph$', ClassDataGraph.as_view()),  #今日学习数据柱状图

]
