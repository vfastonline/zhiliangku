#!encoding:utf-8
from __future__ import unicode_literals

from backstage.exam_statistics.models import *


@receiver(post_migrate, sender=ExamNatureCount)
def init_db_info(sender, **kwargs):
	"""初始化各考试性质总数
	:param sender:
	:param kwargs:
	:return:
	"""
	print "111"
	try:
		# 添加新的考核属性后，执行数据库迁移命令
		init_info = [
			{"nature": "日考核", "nature_id": "1"},
			{"nature": "阶段考核", "nature_id": "2"},
			{"nature": "课程考核", "nature_id": "3"},
			{"nature": "项目考核", "nature_id": "4"},
			{"nature": "结业考核", "nature_id": "5"},
		]
		[ExamNatureCount.objects.get_or_create(**info_dict) for info_dict in init_info]
	except:
		logging.getLogger().error(traceback.print_exc())
