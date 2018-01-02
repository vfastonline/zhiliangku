from django.conf.urls import url

from applications.personal_center import views

urlpatterns = [
    url('^page/$', views.PersonalCenter.as_view()),

    # url('^personal_settings/$', views.CustomUserLogin.as_view()),
]
