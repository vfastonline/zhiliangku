#!encoding:utf-8
from django.conf.urls import url

from applications.interview_question.views import *

urlpatterns = [
    url(r'^list$', InterviewQuestionList.as_view()),
]
