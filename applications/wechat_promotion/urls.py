#!encoding:utf-8
from django.conf.urls import url

from applications.wechat_promotion.views import *
from applications.wechat_promotion.get_signature import *

urlpatterns = [
	url('^promotion/jl$', WechatPromotionJl.as_view()),  # 推广-页面
	url('^promotion$', WechatPromotion.as_view()),  # 推广-页面
	url('^promotion/info$', WechatPromotionInfo.as_view()),  # 推广-学员-信息

	url('^backgrounds$', GetBackgrounds.as_view()),  # 背景图
	url('^background/music$', GetBackgroundMusic.as_view()),  # 背景音乐

	url('^thumbsup$', WechatThumbsUp.as_view()),  # 点赞
	url('^share$', WechatShare.as_view()),  # 分享
	url('^thumbsuptotal$', WechatThumbsUptotal.as_view()),  # 点赞总数

	# 获取jssdk签名
	url('^get/signature$', GetSignature.as_view()),  # 获取signature
]
