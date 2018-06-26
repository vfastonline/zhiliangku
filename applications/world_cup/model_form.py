#!encoding:utf-8
from django import forms
from django_select2.forms import Select2Widget

from applications.exercise.models import *


class TournamentForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = "__all__"
		widgets = {
			'country_a': Select2Widget,
			'country_b': Select2Widget,
		}
