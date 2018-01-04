#!encoding:utf-8
from django.conf.urls import url

from applications.personal_center import views
from applications.personal_center import personal_settings
from applications.personal_center import my_resume
from applications.personal_center import my_courses

urlpatterns = [
    url('^page/$', views.PersonalCenter.as_view()),
    url('^basic/info$', views.PersonalCenterBasicInfo.as_view()),

    # 个人设置
    url('^personal_settings/update/basicinfo$', personal_settings.UpdateBasicInfo.as_view()),
    url('^personal_settings/useraccount$', personal_settings.GetUserAccount.as_view()),
    # url('^personal_settings/accountbindemail$', personal_settings.AccountBindEmail.as_view()),
    url('^personal_settings/user/address$', personal_settings.UserAddress.as_view()),

    # 我的简历
    url('^resume/detail/info$', my_resume.ResumeDetailInfo.as_view()),
    url('^resume/delete$', my_resume.ResumeDelete.as_view()),
    url('^resume/update$', my_resume.ResumeUpdate.as_view()),
    url('^resume/add$', my_resume.ResumeAdd.as_view()),

    # 我的课程
    url('^course/learn_recently$', my_courses.LearnRecently.as_view()),
    url('^course/mycollect$', my_courses.MyCollect.as_view()),
    url('^course/mypath$', my_courses.MyPath.as_view()),
]
