#!encoding:utf-8
from django import forms
from django_select2.forms import Select2Widget

from applications.notification.models import *


class NotificationForm(forms.ModelForm):
	class Meta:
		model = Notification
		fields = "__all__"
		widgets = {
			'custom_user': Select2Widget
		}


class UserNotificationsCountForm(forms.ModelForm):
	class Meta:
		model = UserNotificationsCount
		fields = "__all__"
		widgets = {
			'custom_user': Select2Widget
		}
