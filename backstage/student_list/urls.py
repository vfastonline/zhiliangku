#!encoding:utf-8
from django.conf.urls import url

from backstage.student_list.views import *

urlpatterns = [
	# 学员列表
	url('^student/list$', StudentList.as_view()),  # 学员列表信息
	url('^student/info$', StudentInfo.as_view()),  # 学员基本信息+当前学习节点
	url('^daterangeinfo', DateRangeInfo.as_view()),  # 时间段信息

	#时间、视频分布信息
	url('^learningtime$', LearningTime.as_view()),  # 时间分布信息
	url('^learningvideo$', LearningVideo.as_view()),  # 视频分布信息



]
