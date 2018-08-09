#!encoding:utf-8
"""zhiliangku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views import static as new_static
from django.views.generic import TemplateView

from lib.polyv.api_callback import PolyvCallBack
from zhiliangku import settings
from zhiliangku import views

handler500 = "zhiliangku.views.redirect_500_error"
handler404 = "zhiliangku.views.redirect_404_error"
handler403 = "zhiliangku.views.redirect_403_error"
handler400 = "zhiliangku.views.redirect_400_error"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.index, name="home"),
    url(r'^login/$', TemplateView.as_view(template_name="login/index.html"), name="login"),
    url('^slides/', include('applications.slideshow.urls')),  # 轮播

    # 项目-课程-视频、考核
    url('^tracks/', include(('applications.tracks_learning.urls', "tracks_learning"), namespace="tracks")),

    url('^lives/', include('applications.live_streaming.urls')),  # 直播
    url('^company/', include('applications.company_jobs.urls')),
    url('^customuser/', include('applications.custom_user.urls')),  # 用户
    url('^community/', include('applications.community.urls')),  # 社区
    url('^exercise/', include('applications.exercise.urls')),  # 习题
    url('^polyv/callback', PolyvCallBack.as_view()),  # 保利威视回调
    url('^personal_center/', include('applications.personal_center.urls')),  # 个人中心
    url('^integral/', include('applications.integral.urls')),  # 积分
    url(r'^record/', include('applications.record.urls')),  # 学生观看视频记录
    url(r'^r/', include('applications.face.urls')),
    url(r'^assess/', include('applications.assessment.urls')),  # 考核
    url(r'^employment/', include('applications.employment.urls')),  # 就业
    url(r'^medal/', include('applications.medal.urls')),  # 勋章
    url(r'^notification/', include('applications.notification.urls')),  # 消息通知

    url(r'^wechat/', include('applications.wechat_promotion.urls')),  # 微信推广
    url(r'^worldcup/', include('applications.world_cup.urls')),  # 世界杯-答题-猜球-赢积分

    url(r'^select2/', include('django_select2.urls')),
    url(r'^upload', views.upload, name='upload'),
    url(r'^wechat/audios/(?P<path>.*)$', new_static.serve,
        {'document_root': "/usr/local/openresty/nginx/html/templates/wechat/promotion/audios"}),
    url(r'^wechat/fonts/(?P<path>.*)$', new_static.serve,
        {'document_root': "/usr/local/openresty/nginx/html/templates/wechat/promotion/fonts"}),
    url(r'^wechat/images/(?P<path>.*)$', new_static.serve,
        {'document_root': "/usr/local/openresty/nginx/html/templates/wechat/promotion/images"}),
    url(r'^wechat/javascripts/(?P<path>.*)$', new_static.serve,
        {'document_root': "/usr/local/openresty/nginx/html/templates/wechat/promotion/javascripts"}),
    url(r'^wechat/stylesheets/(?P<path>.*)$', new_static.serve,
        {'document_root': "/usr/local/openresty/nginx/html/templates/wechat/promotion/stylesheets"}),
    url(r'^images/(?P<path>.*)$', new_static.serve,
        {'document_root': "/usr/local/openresty/nginx/html/templates/images"}),

]

# 教室端后台
backstageurl = [
    url(r'^backstage/', include('backstage.home.urls')),  # 首页
    url(r'^exam/', include('backstage.exam_statistics.urls')),  # 考核统计
    url(r'^student/', include('backstage.student_list.urls')),  # 学员列表

]

urlpatterns += backstageurl
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
