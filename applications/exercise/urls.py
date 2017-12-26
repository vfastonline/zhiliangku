#!encoding:utf-8
from django.conf.urls import url
from applications.exercise import views

urlpatterns = [
    url('^list/$', views.QuestionList.as_view()),
    url('^list/info$', views.QuestionListInfo.as_view()),
    url('^right/answer/info$', views.QuestionRightAnswerInfo.as_view()),
]
