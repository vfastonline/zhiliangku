# coding=utf-8

import logging
import traceback

from django.db.models.signals import post_migrate
from django.dispatch import receiver

from applications.world_cup.models import Country


@receiver(post_migrate)
def init_db_info(sender, **kwargs):
	"""初始化国家字典信息，国家名称，国旗图片
	:param sender:
	:param kwargs:
	:return:
	"""
	try:
		# 添加新的国家信息后，执行数据库迁移命令
		init_info = [
			{"name": "俄罗斯", "flag": "/flag/eluosi.png"},
			{"name": "德国", "flag": "/flag/deguo.png"},
			{"name": "法国", "flag": "/flag/faguo.png"},
			{"name": "西班牙", "flag": "/flag/xibanya.png"},
			{"name": "葡萄牙", "flag": "/flag/putaoya.png"},
			{"name": "比利时", "flag": "/flag/bilishi.png"},
			{"name": "英格兰", "flag": "/flag/yinggelan.png"},
			{"name": "冰岛", "flag": "/flag/bingdao.png"},
			{"name": "克罗地亚", "flag": "/flag/keluodiya.png"},
			{"name": "瑞士", "flag": "/flag/ruishi.png"},
			{"name": "瑞典", "flag": "/flag/ruidian.png"},
			{"name": "丹麦", "flag": "/flag/damai.png"},
			{"name": "塞尔维亚", "flag": "/flag/saierweiya.png"},
			{"name": "波兰", "flag": "/flag/bolan.png"},
			{"name": "韩国", "flag": "/flag/hanguo.png"},
			{"name": "日本", "flag": "/flag/riben.png"},
			{"name": "伊朗", "flag": "/flag/yilang.png"},
			{"name": "沙特阿拉伯", "flag": "/flag/shatealabo.png"},
			{"name": "澳大利亚", "flag": "/flag/aodaliya.png"},
			{"name": "巴西", "flag": "/flag/baxi.png"},
			{"name": "阿根廷", "flag": "/flag/agenting.png"},
			{"name": "乌拉圭", "flag": "/flag/wulagui.png"},
			{"name": "哥伦比亚", "flag": "/flag/gelunbiya.png"},
			{"name": "秘鲁", "flag": "/flag/milu.png"},
			{"name": "埃及", "flag": "/flag/aiji.png"},
			{"name": "突尼斯", "flag": "/flag/tunisi.png"},
			{"name": "尼日利亚", "flag": "/flag/niriliya.png"},
			{"name": "摩洛哥", "flag": "/flag/moluoge.png"},
			{"name": "塞内加尔", "flag": "/flag/saineijiaer.png"},
			{"name": "哥斯达黎加", "flag": "/flag/gesidalijia.png"},
			{"name": "墨西哥", "flag": "/flag/moxige.png"},
			{"name": "巴拿马", "flag": "/flag/banama.png"},
		]
		[Country.objects.get_or_create(**info_dict) for info_dict in init_info]
	except:
		logging.getLogger().error(traceback.print_exc())
