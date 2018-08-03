#!encoding:utf-8
from rest_framework import serializers

from applications.tracks_learning.models import *


# 学生笔记
class StudentNotesSerializer(serializers.ModelSerializer):
	custom_user_nickname = serializers.CharField(source='custom_user.nickname', required=False)
	create_time = serializers.DateTimeField(format="%Y-%m-%d %X", required=False)

	class Meta:
		model = StudentNotes
		fields = ('id', 'video', "custom_user", 'custom_user_nickname', 'title', 'notes', 'create_time')
