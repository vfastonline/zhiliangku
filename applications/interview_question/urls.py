#!encoding:utf-8
from django.conf.urls import url

from applications.interview_question.views import *
from applications.interview_question.enterprise_info import *

urlpatterns = [
    url(r'^index/list$', IndexEnterpriseInfoList.as_view()),

    # 企业面试题
    url(r'^enterpriseinfo/list/$', EnterpriseInfoList.as_view()),
    url(r'^enterpriseinfo/list/info$', EnterpriseInfoListInfo.as_view()),

    # 企业面试题详情
    url(r'^enterpriseinfo/detail/$', EnterpriseInfoDetail.as_view()),
    url(r'^enterpriseinfo/detail/info$', EnterpriseInfoDetailInfo.as_view()),
]
