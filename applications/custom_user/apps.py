# encoding: utf8
from __future__ import unicode_literals

from django.apps import AppConfig


class CustomUserConfig(AppConfig):
    name = 'applications.custom_user'
    verbose_name = "用户管理"
