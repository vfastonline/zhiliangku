# coding=utf-8

import logging
import traceback

from django.db.models.signals import post_migrate
from django.dispatch import receiver

from applications.wechat_promotion.models import WechatRemark


@receiver(post_migrate)
def init_db_info(sender, **kwargs):
	"""初始化角色字典信息
	:param sender:
	:param kwargs:
	:return:
	"""
	try:
		# name，系统识别名称, 1代表第一页，A代表
		# 添加新的评语后，执行数据库迁移命令
		init_info = [
			{"name": "1A", "remark": "测试评语"},
			{"name": "1B", "remark": "测试评语"},
			{"name": "1C", "remark": "测试评语"},

			{"name": "2A", "remark": ""},
			{"name": "2B", "remark": ""},
			{"name": "2C", "remark": ""},

			{"name": "3A", "remark": ""},
			{"name": "3B", "remark": ""},
			{"name": "3C", "remark": ""},

			{"name": "4A", "remark": ""},
			{"name": "4B", "remark": ""},
			{"name": "4C", "remark": ""},

			{"name": "5A", "remark": ""},
			{"name": "5B", "remark": ""},
			{"name": "5C", "remark": ""},
		]
		[WechatRemark.objects.get_or_create(**info_dict) for info_dict in init_info]
	except:
		logging.getLogger().error(traceback.print_exc())
