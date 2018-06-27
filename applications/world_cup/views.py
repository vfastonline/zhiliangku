#!encoding:utf-8
import datetime
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import View

from applications.world_cup.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import *


# @class_view_decorator(user_login_required)
class WorldCupTopic(View):
	"""世界杯-答题-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "worldcup/topic/index.html"
		return render(request, template_name, {})


# @class_view_decorator(user_login_required)
class WorldCupTournament(View):
	"""世界杯-猜球-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "worldcup/tournament/index.html"
		return render(request, template_name, {})


# @class_view_decorator(user_login_required)
class WorldCupTopicInfo(View):
	"""世界杯-题目-随机5道题"""

	def __init__(self):
		super(WorldCupTopicInfo, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": list(),
		}

	def get(self, request, *args, **kwargs):
		try:
			topics = random.sample(Topic.objects.all(), 5)
			for one in topics:
				one_dict = dict()
				one_dict["id"] = one.id
				one_dict["title"] = one.title
				one_dict["A"] = one.A
				one_dict["B"] = one.B
				one_dict["right"] = one.right
				self.result_dict["data"].append(one_dict)
		except:
			self.result_dict["err"] = 1
			self.result_dict["msg"] = "获取题目异常"
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


# @class_view_decorator(user_login_required)
class WorldCupScore(View):
	"""世界杯-题目-得分"""

	def __init__(self):
		super(WorldCupScore, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"integral": 0,
		}

	def post(self, request, *args, **kwargs):
		try:
			param_dict = json.loads(request.body)
			custom_user_id = 112#str_to_int(kwargs.get('uid', 0))  # 用户ID
			integral = str_to_int(param_dict.get('integral', 0))  # 积分
			customuser = CustomUser.objects.filter(id=custom_user_id)
			if customuser.exists():
				customuser.update(integral=F('integral') + integral)
				self.result_dict["integral"] = customuser.first().integral
		except:
			self.result_dict["err"] = 1
			self.result_dict["msg"] = "获得积分异常"
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


# @class_view_decorator(user_login_required)
class GetTournamentInfo(View):
	"""世界杯-获取未开赛今日赛事"""

	def __init__(self):
		super(GetTournamentInfo, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": list(),
		}

	def get(self, request, *args, **kwargs):
		try:
			filter_param = {
				"start_time__gt": datetime.datetime.now()
			}
			tournaments = Tournament.objects.filter(**filter_param)[:3]
			for one in tournaments:
				one_dict = dict()
				one_dict["id"] = one.id
				one_dict["country_a_id"] = one.country_a.id
				one_dict["country_a_name"] = one.country_a.name
				one_dict["country_a_flag"] = one.country_a.flag.url if one.country_a.flag else ""
				one_dict["country_b_id"] = one.country_b.id
				one_dict["country_b_name"] = one.country_b.name
				one_dict["country_b_flag"] = one.country_b.flag.url if one.country_b.flag else ""
				one_dict["start_time"] = one.start_time.strftime("%Y-%m-%d %X")
				self.result_dict["data"].append(one_dict)
		except:
			self.result_dict["err"] = 1
			self.result_dict["msg"] = "获取赛事异常"
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


# @class_view_decorator(user_login_required)
class WorldCupBet(View):
	"""押注"""

	def __init__(self):
		super(WorldCupBet, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"integral": 0,
		}

	def post(self, request, *args, **kwargs):
		try:
			param_dict = json.loads(request.body)
			custom_user_id = 112#str_to_int(kwargs.get('uid', 0))  # 用户ID
			bet_info = param_dict.get('bet_info', [])  # [{"integral": 10, "tournament_id": 1, "country": "A"}]

			customuser = CustomUser.objects.get(id=custom_user_id)
			for one in bet_info:
				integral = str_to_int(one.get('integral', 0))  # 积分
				tournament_id = str_to_int(one.get('tournament_id', 0))  # 赛事ID
				country = one.get('country', "")  # A:国家A胜  B:国家B胜  C:平

				tournament = Tournament.objects.get(id=tournament_id)
				create_param = {
					"user": customuser,
					"tournament": tournament,
					"country": country,
					"integral": integral,
				}
				betrecord = BetRecord.objects.create(**create_param)
				if betrecord:
					CustomUser.objects.filter(id=custom_user_id).update(integral=F('integral') - integral)

			# 获取用户积分
			self.result_dict["integral"] = CustomUser.objects.get(id=custom_user_id).integral

		except:
			self.result_dict["err"] = 1
			self.result_dict["msg"] = "押注异常"
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


# @class_view_decorator(user_login_required)
class GetAnalysisInfo(View):
	"""世界杯-获取-教你猜球信息"""

	def __init__(self):
		super(GetAnalysisInfo, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": list(),
		}

	def get(self, request, *args, **kwargs):
		try:
			today = datetime.date.today()
			for one in Analysis.objects.filter(create_time=today):
				chart_url = one.chart.url if one.chart else ""
				self.result_dict["data"].append(chart_url)
		except:
			self.result_dict["err"] = 1
			self.result_dict["msg"] = "无猜球规则"
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


# @class_view_decorator(user_login_required)
class GetUserIntegral(View):
	"""世界杯-获取-用户积分"""

	def __init__(self):
		super(GetUserIntegral, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": 0,
		}

	def get(self, request, *args, **kwargs):
		try:
			custom_user_id =112 #str_to_int(kwargs.get('uid', 0))  # 用户ID
			self.result_dict["data"] = CustomUser.objects.get(id=custom_user_id).integral
		except:
			self.result_dict["err"] = 1
			self.result_dict["msg"] = "无用户信息"
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


# @class_view_decorator(user_login_required)
class GetUserBetResult(View):
	"""世界杯-获取-用户押注结果"""

	def __init__(self):
		super(GetUserBetResult, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": list(),
		}

	def get(self, request, *args, **kwargs):
		try:
			custom_user_id = 112#str_to_int(kwargs.get('uid', 0))  # 用户ID

			now = time.time()
			midnight = now - (now % 86400) + time.timezone
			pre_midnight = midnight - 86400
			now_midnight = midnight - 1
			time_format = "%Y-%m-%d %H:%M:%S"
			start_time = datetime.datetime.strptime(time.strftime(time_format, time.localtime(pre_midnight)),
													time_format)
			end_time = datetime.datetime.strptime(time.strftime(time_format, time.localtime(now_midnight)), time_format)
			# 获取昨天有结果赛事
			filter_param = {
				"is_summary": True,
				"summary_time__gt": start_time,
				"summary_time__lt": end_time,
			}
			tournaments = Tournament.objects.filter(**filter_param)  # 昨天已经出比赛结果并且已经汇总的赛事
			for tournament in tournaments:
				one_dict = dict()
				if tournament.a_victory:  # A国家胜
					match_results = "A"
				elif tournament.b_victory:  # B国家胜
					match_results = "B"
				elif tournament.common:  # 平
					match_results = "C"
				else:  # 没有录入结果的不汇总
					continue

				filter_param = {
					"user__id": custom_user_id,
					"tournament": tournament,
					"country": match_results
				}
				betrecords = BetRecord.objects.filter(**filter_param).values("user").annotate(integral=Sum("integral"))
				integral = 0
				if betrecords.exists():
					betrecord = betrecords.first()
					integral = betrecord.get("integral", 0) * 2
				one_dict["id"] = tournament.id
				one_dict["country_a_name"] = tournament.country_a.name
				one_dict["country_a_flag"] = tournament.country_a.flag.url if tournament.country_a.flag else ""
				one_dict["country_b_name"] = tournament.country_b.name
				one_dict["country_b_flag"] = tournament.country_b.flag.url if tournament.country_b.flag else ""
				one_dict["integral"] = integral
				one_dict["match_results"] = match_results

				self.result_dict["data"].append(one_dict)

		except:
			self.result_dict["err"] = 1
			self.result_dict["msg"] = "无猜球规则"
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


# @class_view_decorator(user_login_required)
class GetBetRecordCount(View):
	"""世界杯-获取-投注记录总数"""

	def __init__(self):
		super(GetBetRecordCount, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": 999,
		}

	def get(self, request, *args, **kwargs):
		try:
			self.result_dict["data"] = BetRecordCount.objects.first().count
		except:
			self.result_dict["err"] = 1
			self.result_dict["msg"] = "无投注记录"
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))
