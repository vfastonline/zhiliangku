#!encoding:utf-8
from django import forms
from django_select2.forms import Select2Widget

from applications.exercise.models import *


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
        widgets = {
            'video': Select2Widget
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = "__all__"
        widgets = {
            'question': Select2Widget
        }