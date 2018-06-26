# coding=utf-8
import logging
import traceback

from django.db.models.signals import post_migrate
from django.dispatch import receiver

from applications.medal.models import *


@receiver(post_migrate, )
def init_db_info(sender, **kwargs):
	"""初始化勋章字典信息
	:param sender:
	:param kwargs:
	:return:
	"""
	try:
		# only，系统识别名称
		# 添加新的勋章后，执行数据库迁移命令
		init_info = [
			{"name": "初次完成考核", "pathwel": "/medal/1.jpg", "only": "first_complete_assess"},
			{"name": "完成项目考核", "pathwel": "/medal/2.jpg", "only": "complete_project_assess"},
			{"name": "完成总项目考核", "pathwel": "/medal/3.jpg", "only": "complete_overall_project_assess"},
		]
		[Medal.objects.get_or_create(**info_dict) for info_dict in init_info]
	except:
		logging.getLogger().error(traceback.print_exc())
