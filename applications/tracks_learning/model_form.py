#!encoding:utf-8
from django import forms
from django_select2.forms import Select2Widget

from applications.tracks_learning.models import *
from django.db.models import Q
from django.core.exceptions import ValidationError


class TechnologyForm(forms.ModelForm):
	"""技术方向"""

	class Meta:
		model = Technology
		fields = "__all__"
		widgets = {
			'video': Select2Widget
		}


class SectionForm(forms.ModelForm):
	"""章节"""

	class Meta:
		model = Section
		fields = "__all__"
		widgets = {
			'course': Select2Widget
		}


class NodusForm(forms.ModelForm):
	"""视频难点"""

	class Meta:
		model = CommonQuestion
		fields = "__all__"
		widgets = {
			'video': Select2Widget,
		}


class CommonQuestionForm(forms.ModelForm):
	"""视频常见问题"""

	class Meta:
		model = CommonQuestion
		fields = "__all__"
		widgets = {
			'video': Select2Widget,
		}


class StudentNotesForm(forms.ModelForm):
	"""学生笔记"""

	class Meta:
		model = StudentNotes
		fields = "__all__"
		widgets = {
			'video': Select2Widget,
		}
