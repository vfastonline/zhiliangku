# coding=utf-8
import traceback

import datetime
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Sum, F

from applications.world_cup.models import *


class Command(BaseCommand):
	help = "Every day at 10:30am, user points are aggregated according to the outcome of each World Cup match"

	def handle(self, *args, **options):
		"""每天上午10:30，根据每场世界杯比赛的结果汇总用户积分
		:return:
		"""
		try:
			# 获取已经开赛同时没有汇总过的赛事
			filter_param = {
				"start_time__lte": datetime.datetime.now(),
				"is_summary": False
			}
			tournaments = Tournament.objects.filter(**filter_param)
			is_summary_ids = list()

			# 汇总
			user_integral = dict()  # {user_id:integral}
			for tournament in tournaments:
				# 查看本场赛事比赛结果
				if tournament.a_victory:  # A国家胜
					match_results = "A"
				elif tournament.b_victory:  # B国家胜
					match_results = "B"
				elif tournament.common:  # 平
					match_results = "C"
				else:  # 没有录入结果的不汇总
					continue
				is_summary_ids.append(tournament.id)
				filter_param = {
					"tournament": tournament,
					"country": match_results
				}
				# 分组查询各个用户正确押注总积分
				# betrecords：<QuerySet [{'sum_integral': 32, 'user': 3L}]>
				betrecords = BetRecord.objects.filter(**filter_param).values("user").annotate(integral=Sum("integral"))
				for betrecord in betrecords:
					user_id = betrecord["user"]
					integral = betrecord["integral"]
					if user_integral.has_key(user_id):  # 已经有用户积分信息
						user_integral[user_id] += integral * 2
					else:
						user_integral[user_id] = integral * 2

			# 修改用户积分
			[CustomUser.objects.filter(id=key).update(integral=F('integral') + val) for key, val in
			 user_integral.items()]

			# 管理员设置比赛结果并已汇总的赛事，修改为已汇总
			Tournament.objects.filter(id__in=is_summary_ids).update(is_summary=True)
		except:
			traceback.print_exc()
			raise CommandError(traceback.format_exc())
