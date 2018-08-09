#!encoding:utf-8
from rest_framework import serializers

from backstage.home.models import *


# 学习任务汇总
class LearnTaskSummarySerializer(serializers.ModelSerializer):
	class Meta:
		model = LearnTaskSummary
		fields = ('average', 'improve', "complete", 'undone', 'excess_complete')


class LearnTaskSummaryRangeDateSerializer(serializers.ModelSerializer):
	"""老师端-首页-任务进度数据统计表-折线图"""
	update_time = serializers.DateTimeField(format="%m/%d", required=False)

	class Meta:
		model = LearnTaskSummary
		fields = ("complete", 'undone', 'excess_complete', "update_time")
