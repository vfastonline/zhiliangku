#!encoding:utf-8
from django.conf.urls import url
from applications.world_cup.views import *

urlpatterns = [
	url('^topic$', WorldCupTopic.as_view()),  # 答题-页面
	url('^tournament$', WorldCupTopic.as_view()),  # 赛事-页面
	url('^topic/info$', WorldCupTopicInfo.as_view()),  # 答题-数据
	url('^score$', WorldCupScore.as_view()),  # 答题-得分
	url('^tournament/info$', GetTournamentInfo.as_view()),  # 未开赛的赛事
	url('^bet$', WorldCupBet.as_view()),  # 押注
]
