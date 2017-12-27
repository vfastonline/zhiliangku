#!encoding:utf-8
from django.conf.urls import url

from applications.interview_question.views import *
from applications.interview_question.enterprise_info import *

urlpatterns = [
    url(r'^index/list$', IndexEnterpriseInfoList.as_view()),
    url(r'^enterpriseinfo/list/$', EnterpriseInfoList.as_view()),
    url(r'^enterpriseinfo/list/info$', EnterpriseInfoListInfo.as_view()),
]
