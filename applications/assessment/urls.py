#!encoding:utf-8
from django.conf.urls import url

from applications.assessment.views import *

urlpatterns = [
	url('^info/$', AssessmentPage.as_view()),  # 考核页面
	url('^construct$', ConstructDocker.as_view()),  # 构建docker容器
	url('^result/$', AssessmentResult.as_view()),  # 考核结果页面
	url('^result/info$', AssessmentResultInfo.as_view()),  # 考核结果信息
	url('^add/times$', AssessmentResultInfo.as_view()),  # 增加用户考核记录
]
