#!encoding:utf-8
from django import forms
from django_select2.forms import Select2Widget

from applications.tracks_learning.models import *


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        widgets = {
            'lecturer': Select2Widget
        }


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = "__all__"
        widgets = {
            'course': Select2Widget
        }


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = "__all__"
        widgets = {
            'section': Select2Widget,
            'live': Select2Widget,
        }


class CommonQuestionForm(forms.ModelForm):
    class Meta:
        model = CommonQuestion
        fields = "__all__"
        widgets = {
            'video': Select2Widget,
        }


class PathStageForm(forms.ModelForm):
    class Meta:
        model = PathStage
        fields = "__all__"
        widgets = {
            'path': Select2Widget
        }


class CourseCategoryForm(forms.ModelForm):
    class Meta:
        model = CourseCategory
        fields = "__all__"
        widgets = {
            'path_stage': Select2Widget
        }
