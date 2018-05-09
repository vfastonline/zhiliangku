#!encoding:utf-8
from django import forms
from django_select2.forms import Select2Widget

from applications.custom_user.models import *


class CustomUserProjectForm(forms.ModelForm):
    class Meta:
        model = CustomUserProject
        fields = "__all__"
        widgets = {
            'custom_user': Select2Widget
        }


class CustomUserAuthsForm(forms.ModelForm):
    class Meta:
        model = CustomUserProject
        fields = "__all__"
        widgets = {
            'custom_user_id': Select2Widget
        }


class CustomUserCourseForm(forms.ModelForm):
    class Meta:
        model = CustomUserProject
        fields = "__all__"
        widgets = {
            'custom_user': Select2Widget
        }
