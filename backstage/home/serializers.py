#!encoding:utf-8
from rest_framework import serializers

from backstage.home.models import *


# 学习任务汇总
class LearnTaskSummarySerializer(serializers.ModelSerializer):
	class Meta:
		model = LearnTaskSummary
		fields = ('average', 'improve', "complete", 'undone', 'excess_complete')
