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

			# 第一页评语
			{
				"name": "1A",
				"remark": "<span class='blue'>怀疑过人生，但我更坚信未来</span>",
				"english": "<span class='blue'>DOUBT LIFE, BUT I FIRMLY BELIEVE THE FUTURE</span>"
			},
			{
				"name": "1B",
				"remark": "<span class='blue'>我不是最强，但我很强</span>",
				"english": "<span class='blue'>I AM NOT BEST，BUT I AM VERY STRONG</span>"
			},
			{
				"name": "1C",
				"remark": "<span class='blue'>我在努力创造价值，等我</span>",
				"english": "<span class='blue'>I AM TRYING TO CREATE VALUE, WAIT FOR ME</span>"
			},

			# 第二页评语
			{
				"name": "2A",
				"remark": "<span class='red'>130</span><span class='blue'>个小时的学习</span><br><span class='blue'>相当于走了</span><span class='red'>112931</span><span class='blue'>步</span><br><span class='blue'>攀登了整个</span><span class='red'>珠穆朗玛峰</span>",
			},
			{
				"name": "2B",
				"remark": "<span class='red'>120</span><span class='blue'>个小时的学习</span><br><span class='blue'>相当于走了</span><span class='red'>104244</span><span class='blue'>步</span><br><span class='blue'>攀登了大半个</span><span class='red'>珠穆朗玛峰</span>",
			},
			{
				"name": "2C",
				"remark": "<span class='red'>110</span><span class='blue'>个小时的学习</span><br><span class='blue'>相当于走了</span><span class='red'>95557</span><span class='blue'>步</span><br><span class='blue'>攀登了半个</span><span class='red'>珠穆朗玛峰</span>",
			},

			# 第三页评语
			{
				"name": "3A",
				"remark": "<span class='red'>33</span>个视频<br><span class='red'>40多</span>个大知识点<br><span class='red'>800</span>多分钟<br>恭喜已到<span class='red'>铂金I段位</span>",
			},
			{
				"name": "3B",
				"remark": "<span class='red'>32</span>个视频<br><span class='red'>40</span>个大知识点<br><span class='red'>780</span>多分钟<br>恭喜已到<span class='red'>铂金II段位</span>",
			},
			{
				"name": "3C",
				"remark": "<span class='red'>31</span>个视频<br><span class='red'>37多</span>个大知识点<br><span class='red'>750</span>多分钟<br>恭喜已到<span class='red'>铂金III段位</span>",
			},

			# 第四页评语
			{
				"name": "4A",
				"remark": "你本阶段<span class='red'>100%</span>的勤劳<br>已为你<span class='red'>薪资过万</span>的工作<br>积累了<span class='red'>33%</span>的经验值"
			},
			{
				"name": "4B",
				"remark": "你本阶段<span class='red'>95%</span>的勤劳<br>已为你<span class='red'>薪资过万</span>的工作<br>积累了<span class='red'>30%</span>的经验值"
			},
			{
				"name": "4C",
				"remark": "你本阶段<span class='red'>90%</span>的勤劳<br>已为你<span class='red'>薪资过万</span>的工作<br>积累了<span class='red'>27%</span>的经验值"
			},

			# 第五页评语
			{
				"name": "5A",
				"remark": "第一次认真，只为把人生过得更精彩",
				"english": "<span class='blue'>THE FIRST TIME SERIOUS<span><br><span class='blue'>JUST TO MAKE LIFE MORE EXCITING</span>"
			},
			{
				"name": "5B",
				"remark": "现在的努力只为我生命中最重要的人",
				"english": "<span class='blue'>THE CURRENT EFFORT IS ONLY<span><br><span class='blue'>THE MOST IMPORTANT PERSON IN MY LIFE</span>"
			},
			{
				"name": "5C",
				"remark": "硬度取决于技术，高度取决于资本",
				"english": "<span class='blue'>HARDNESS DEPENDS ON TECHNOLOGY<span><br><span class='blue'>HIGHLY DEPENDENT ON CAPITAL</span>"
			},
		]
		[WechatRemark.objects.get_or_create(**info_dict) for info_dict in init_info]
	except:
		logging.getLogger().error(traceback.print_exc())
