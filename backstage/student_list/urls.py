#!encoding:utf-8
from django.conf.urls import url

# from backstage.student_list.views import *
from backstage.student_list.learn_video import *
from backstage.student_list.learn_time import *
from backstage.student_list.student_info import *
from backstage.student_list.date_range_info import *
from backstage.student_list.learn_status import *
from backstage.student_list.student_list import *


urlpatterns = [
	# 学员列表
	url('^student/list$', StudentList.as_view()),  # 学员列表信息
	url('^student/info$', StudentInfo.as_view()),  # 学员基本信息+当前学习节点
	url('^date/range/info', DateRangeInfo.as_view()),  # 时间段信息

	#时间、视频分布信息
	url('^learn/time$', LearnTime.as_view()),  # 时间分布信息
	url('^learn/video$', LearnVideo.as_view()),  # 视频分布信息

	url('^learn/status$', LearnStatus.as_view()),  # 学习状态

]
