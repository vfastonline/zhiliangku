#!encoding:utf-8
from django.conf.urls import url

from applications.employment.finish_project_views import *
from applications.employment.leaderboard_views import *

urlpatterns = [
	# 排行榜
	url('^leaderboard/list/$', LeaderboardList.as_view()),
	url('^leaderboard/list/info$', LeaderboardListInfo.as_view()),

	# 用户完成项目
	url('^finishprojectlist/list/$', FinishProjectList.as_view()),
	url('^finishprojectlistinfo/list/info$', FinishProjectListInfo.as_view()),
]
