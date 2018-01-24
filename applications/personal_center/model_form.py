#!encoding:utf-8
from django import forms
from django_select2.forms import Select2Widget

from applications.personal_center.models import *


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = "__all__"
        widgets = {
            'custom_user': Select2Widget
        }


class CareerObjectiveForm(forms.ModelForm):
    class Meta:
        model = CareerObjective
        fields = "__all__"
        widgets = {
            'custom_user': Select2Widget
        }


class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = "__all__"
        widgets = {
            'custom_user': Select2Widget
        }


class ProjectExperienceForm(forms.ModelForm):
    class Meta:
        model = ProjectExperience
        fields = "__all__"
        widgets = {
            'custom_user': Select2Widget
        }


class EducationExperienceForm(forms.ModelForm):
    class Meta:
        model = EducationExperience
        fields = "__all__"
        widgets = {
            'custom_user': Select2Widget
        }
