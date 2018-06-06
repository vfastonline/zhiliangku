# coding=utf-8
import logging
import traceback

from django.db.models.signals import post_migrate
from django.dispatch import receiver

from applications.medal.models import *


@receiver(post_migrate)
def init_db_info(sender, **kwargs):
	"""初始化角色字典信息
	:param sender:
	:param kwargs:
	:return:
	"""
	try:
		init_info = [
			{"name": "初次完成考核", "pathwel": "/medal/1.jpg"},
			{"name": "完成项目考核", "pathwel": "/medal/2.jpg"},
			{"name": "完成总项目考核", "pathwel": "/medal/3.jpg"},
		]
		[Medal.objects.get_or_create(**info_dict) for info_dict in init_info]
	except:
		logging.getLogger().error(traceback.print_exc())
