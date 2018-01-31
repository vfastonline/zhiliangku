from django.conf.urls import url

import avatar
import views

urlpatterns = [
    url('^login$', views.CustomUserLogin.as_view()),
    url('^logout$', views.CustomUserLogout.as_view()),
    url('^weixin/login$', views.WeiXinLogin.as_view()),
    url('^qq/login$', views.QQLogin.as_view()),
    url('^register$', views.CustomUserRegister.as_view()),
    url('^send_sms$', views.SendSMSVerificationCode.as_view()),
    url('^activation/$', views.ActivationCustomUserEmail.as_view()),
    url('^activation/result/$', views.ActivationResult.as_view()),
    url('^retrieve_password_by_phone$', views.RetrievePasswordByPhone.as_view()),
    url('^retrieve_password_by_email/$', views.RetrievePasswordByEmail.as_view()),
    url('^send_email_retrieve_password$', views.SendEmailRetrievePassword.as_view()),
    url('^send_activation_mail$', views.CustomUserSendActivationMail.as_view()),
    url('^change/avatar$', avatar.CustomUserAvatar.as_view()),
]
