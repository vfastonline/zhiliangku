#!encoding:utf-8
from django.conf.urls import url

from applications.interview_question.views import *
from applications.interview_question.enterprise_info import *
from applications.interview_question.examination_question import *
from applications.interview_question.interview_result import *

urlpatterns = [
    url(r'^index/list$', IndexEnterpriseInfoList.as_view()),

    # 企业信息
    url(r'^enterpriseinfo/list/$', EnterpriseInfoList.as_view()),
    url(r'^enterpriseinfo/list/info$', EnterpriseInfoListInfo.as_view()),

    # 企业面试题详情
    url(r'^enterpriseinfo/detail/$', EnterpriseInfoDetail.as_view()),
    url(r'^enterpriseinfo/detail/info$', EnterpriseInfoDetailInfo.as_view()),

    # 企业下所有面试题
    url(r'^examinationquestion/list/$', ExaminationQuestionListInfo.as_view()),
    url(r'^examinationquestion/list/info$', ExaminationQuestionListInfo.as_view()),

    # 校验面试题，记录答题记录
    url(r'^examinationquestion/answer/info$', ExaminationQuestionAnswerInfo.as_view()),

    # 面试结果
    url(r'^enterprise/result/$', EnterpriseRsult.as_view()),
    url(r'^enterprise/result/info$', EnterpriseRsultInfo.as_view()),
]
