#!encoding:utf-8
from django.conf.urls import url

from applications.face import views

urlpatterns = [
    url('^face$', views.face),
    url('^getface$', views.getface),

]
