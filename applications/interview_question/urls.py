#!encoding:utf-8
from django.conf.urls import url

from applications.interview_question.views import *

urlpatterns = [
    url(r'^index/list$', IndexInterviewQuestionList.as_view()),
]
