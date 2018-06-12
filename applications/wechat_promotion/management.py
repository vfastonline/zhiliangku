# coding=utf-8

import logging
import traceback

from django.db.models.signals import post_migrate
from django.dispatch import receiver

from applications.wechat_promotion.models import WechatRemark


@receiver(post_migrate)
def init_db_info(sender, **kwargs):
	"""初始化推广页面学生学习评语字典信息
	:param sender:
	:param kwargs:
	:return:
	"""
	try:
		# name，系统识别名称, 1代表第一页，ABC代表级别
		# 添加新的评语后，执行数据库迁移命令
		init_info = [
			{"name": "1A", "remark": "怀疑过人生，但我更坚信未来"},
			{"name": "1B", "remark": "我不是最强，但我很强"},
			{"name": "1C", "remark": "我在努力创造价值，等我"},

			{"name": "2A", "remark": "130个小时的学习消耗了近4745卡路里，相当于走了112931步"},
			{"name": "2B", "remark": "120个小时的学习消耗了近4380卡路里，相当于走了104244步"},
			{"name": "2C", "remark": "110个小时的学习消耗了近4015卡路里，相当于走了95557步"},

			{"name": "3A", "remark": "33个视频，40多个大知识点，800多分钟，恭喜已到青铜I段位"},
			{"name": "3B", "remark": "32个视频，近40个大知识点，780多分钟，恭喜已到青铜II段位"},
			{"name": "3C", "remark": "31个视频，37多个大知识点，750多分钟，恭喜已到青铜III段位"},

			{"name": "4A", "remark": "你本周100%的勤劳已为你薪资过万的工作积累了33%的经验值"},
			{"name": "4B", "remark": "你本周95%的勤劳已为你薪资过万的工作积累了30%的经验值"},
			{"name": "4C", "remark": "你本周90%的勤劳已为你薪资过万的工作积累了27%的经验值"},

			{"name": "5A", "remark": "第一次认真，只为把人生过得更精彩"},
			{"name": "5B", "remark": "现在的努力只为我生命中最重要的人"},
			{"name": "5C", "remark": "硬度取决于技术，高度取决于资本"},
		]
		[WechatRemark.objects.get_or_create(**info_dict) for info_dict in init_info]
	except:
		logging.getLogger().error(traceback.print_exc())
