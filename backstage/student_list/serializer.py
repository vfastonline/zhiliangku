

#序列化


from rest_framework import serializers


from applications.custom_user.models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields="__all__"
