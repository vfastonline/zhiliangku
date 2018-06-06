#!encoding:utf-8
from django.conf.urls import url

from applications.wechat_promotion.views import *

urlpatterns = [
	url('^promotion$', WechatPromotion.as_view()),  # 微信推广页面
	url('^thumbsup$', WechatThumbsUp.as_view()),  # 微信推广点赞

	url(r'^audios/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': "/usr/local/openresty/nginx/html/templates/wechat/promotion/audios"}),
	url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': "/usr/local/openresty/nginx/html/templates/wechat/promotion/fonts"}),
	url(r'^images/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': "/usr/local/openresty/nginx/html/templates/wechat/promotion/images"}),
	url(r'^javascripts/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': "/usr/local/openresty/nginx/html/templates/wechat/promotion/javascripts"}),
	url(r'^stylesheets/(?P<path>.*)$', 'django.views.static.serve',
		{'document_root': "/usr/local/openresty/nginx/html/templates/wechat/promotion/stylesheets"}),

]
