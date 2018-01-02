#!encoding:utf-8
from django.conf.urls import url

from applications.personal_center import views
from applications.personal_center import personal_settings

urlpatterns = [
    url('^page/$', views.PersonalCenter.as_view()),
    url('^basic/info$', views.PersonalCenterBasicInfo.as_view()),

    # 个人设置
    url('^personal_settings/update/basicinfo$', personal_settings.UpdateBasicInfo.as_view()),
]
