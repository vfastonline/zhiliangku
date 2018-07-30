#!encoding:utf-8
from django.conf.urls import url

from backstage.exam_statistics.views import *
from backstage.exam_statistics.page_views import *

urlpatterns = [
	# 页面
	url('^statistics/$', ExamStatisticsPage.as_view()),  # 考试统计
	url('^grade/entry/$', ExamGradeEntryPage.as_view()),  # 成绩录入
	url('^detail/$', ExamDetailPage.as_view()),  # 考试详情
	url('^report/$', ExamReportPage.as_view()),  # 考试报表

	# 数据-接口
	url('^count/by/nature$', ExamsCountByNatureView.as_view()),  # 考试性质个数汇总
	url('^exams$', ExamsView.as_view()),  # 考试，查询，添加，修改
	url('^exams/(?P<pk>[0-9]+)$', ExamDetailView.as_view()),  # 考试详情
	url('^entry/grade$', ExamEntryGradeView.as_view()),  # 获取学生信息，录入成绩
	url('^report$', ExamReportView.as_view()),  # 考核报表

]
