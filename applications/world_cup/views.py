#!encoding:utf-8
from django.db.models import F
from django.shortcuts import render
from django.views.generic import View

from applications.custom_user.models import CustomUser
from applications.world_cup.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import *
import datetime


class WorldCupTopic(View):
	"""世界杯-答题-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "worldcup/topic/index.html"
		return render(request, template_name, {})


class WorldCupTournament(View):
	"""世界杯-猜球-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "worldcup/tournament/index.html"
		return render(request, template_name, {})


@class_view_decorator(user_login_required)
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


@class_view_decorator(user_login_required)
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
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
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


@class_view_decorator(user_login_required)
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


@class_view_decorator(user_login_required)
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
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			integral = str_to_int(param_dict.get('integral', 0))  # 积分
			tournament_id = str_to_int(param_dict.get('tournament', 0))  # 赛事ID
			country = param_dict.get('tournament', "")  # A:国家A胜  B:国家B胜  C:平

			customuser = CustomUser.objects.get(id=custom_user_id)
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
			self.result_dict["integral"] = customuser.integral

		except:
			self.result_dict["err"] = 1
			self.result_dict["msg"] = "押注异常"
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))
