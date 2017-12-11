from django.conf.urls import url
import views

urlpatterns = [
    url('^login$', views.CustomUserLogin.as_view()),
    url('^register$', views.CustomUserRegister.as_view()),
]
