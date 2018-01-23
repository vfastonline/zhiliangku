#!encoding:utf-8
from django import forms
from django_select2.forms import Select2Widget

from applications.slideshow.models import *


class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = "__all__"
        widgets = {
            'video': Select2Widget
        }
