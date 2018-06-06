#!encoding:utf-8
from django import forms
from django_select2.forms import Select2Widget

from applications.medal.models import *


class CustomUserMedalForm(forms.ModelForm):
	class Meta:
		model = CustomUserMedal
		fields = "__all__"
		widgets = {
			'custom_user': Select2Widget
		}


class MedalForm(forms.ModelForm):
	class Meta:
		model = Medal
		fields = "__all__"
