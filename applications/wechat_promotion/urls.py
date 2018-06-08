#!encoding:utf-8
from django.conf.urls import url

from applications.wechat_promotion.views import *

urlpatterns = [
	url('^promotion$', WechatPromotion.as_view()),  # 微信推广页面
	url('^thumbsup$', WechatThumbsUp.as_view()),  # 微信推广点赞
	url('^thumbsuptotal$', WechatThumbsUptotal.as_view()),  # 微信推广点赞
	url('^get/accesstoken$', GetAccessToken.as_view()),  # 微信-获取accesstoken
]
