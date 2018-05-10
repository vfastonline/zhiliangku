#!encoding:utf-8
from django import forms
from django_select2.forms import Select2Widget

from applications.tracks_learning.models import *
from django.db.models import Q
from django.core.exceptions import ValidationError


class SectionForm(forms.ModelForm):
	class Meta:
		model = Section
		fields = "__all__"
		widgets = {
			'course': Select2Widget
		}

class NodusForm(forms.ModelForm):
	class Meta:
		model = CommonQuestion
		fields = "__all__"
		widgets = {
			'video': Select2Widget,
		}


class CommonQuestionForm(forms.ModelForm):
	class Meta:
		model = CommonQuestion
		fields = "__all__"
		widgets = {
			'video': Select2Widget,
		}


class StudentNotesForm(forms.ModelForm):
	class Meta:
		model = StudentNotes
		fields = "__all__"
		widgets = {
			'video': Select2Widget,
		}
