#!encoding:utf-8
from rest_framework import serializers

from applications.community.models import *


# 我要提问、问答统计（缓
# 搜索问题
class FaqSerializer(serializers.ModelSerializer):
    # custom_user_nickname = serializers.CharField(source='custom_user.nickname', required=False)
    # create_time = serializers.DateTimeField(format="%Y-%m-%d %X", required=False)

    class Meta:
        model = FaqAnswer
        fields = ('faq', 'user', "answer", 'create_time', 'approve', 'oppose', 'optimal')

