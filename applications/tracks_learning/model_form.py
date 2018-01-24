#!encoding:utf-8
from django import forms
from django_select2.forms import Select2Widget

from applications.tracks_learning.models import *
from django.db.models import Q
from django.core.exceptions import ValidationError


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
    id = forms.CharField()

    def clean(self):
        cleaned_data = super(VideoForm, self).clean()
        video_id = cleaned_data.get('id')
        video_type = self.cleaned_data.get('type')
        live_start_time = self.cleaned_data.get('live_start_time')
        live_end_time = self.cleaned_data.get('live_end_time')
        live = self.cleaned_data.get('live')
        if video_type == "3" and live_start_time and live_end_time:  # 直播
            if live_end_time <= live_start_time:
                self.add_error('live_end_time', "直播终止时间应大于直播起始时间!")
                raise ValidationError("直播时间异常！")

            # 校验直播时间是否冲突
            filter_param = {
                "live": live,
                "live_start_time__gt": live_end_time,
                "live_end_time__lt": live_start_time,
            }
            print cleaned_data
            videos = Video.objects.filter(Q(live_start_time__lt=live_end_time) | Q(live_end_time__gt=live_start_time),
                                          live=live).exclude(id=video_id)
            print videos
            if videos.exists():
                self.add_error('live_start_time', "直播时间冲突!")
                self.add_error('live_end_time', "直播时间冲突!")
                raise ValidationError('直播时间异常！')

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
