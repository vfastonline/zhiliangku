#!encoding:utf-8
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import View

from applications.custom_user.models import CustomUser
from applications.tracks_learning.models import Project
from applications.tracks_learning.models import UnlockVideo
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import *


@class_view_decorator(user_login_required)
class LeaderboardList(View):
	"""排行榜-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "employment/leaderboard/list/index.html"
		return render(request, template_name, {})


@class_view_decorator(user_login_required)
class LeaderboardListInfo(View):
	"""排行榜-信息"""

	def __init__(self):
		super(LeaderboardListInfo, self).__init__()
		# 用户ID，昵称，头像，所属院校，所属班级
		self.user_info_list = ["id", "nickname", "avatar", "institutions"]
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": list(),
			"custom_user": dict(),
			"paginator": dict()
		}

	def get(self, request, *args, **kwargs):
		try:
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			page = request.GET.get("page", 1)  # 页码
			per_page = request.GET.get("per_page", 12)  # 每页显示条目数

			self.project_video_id_list = Project.objects.all().values_list("video", flat=True)  # 所有项目的考核视频ID列表

			# 完成项目考核用户排名
			unlockvideos = UnlockVideo.objects.filter(video__id__in=self.project_video_id_list) \
				.values('custom_user') \
				.annotate(num=Count('custom_user')) \
				.order_by("-num")

			# 提供分页数据
			if not page: page = 1
			if not per_page: page = 12
			page_obj = Paginator(unlockvideos, per_page)
			total_count = page_obj.count  # 记录总数
			num_pages = page_obj.num_pages  # 总页数
			page_range = list(page_obj.page_range)  # 页码列表
			paginator_dict = {
				"total_count": total_count,
				"num_pages": num_pages,
				"page_range": page_range,
				"page": page,
				"per_page": per_page
			}
			self.result_dict["paginator"] = paginator_dict
			try:
				unlockvideo_list = page_obj.page(page).object_list
			except:
				unlockvideo_list = list()

			# 当前用户的排名
			custom_user_unlocks = unlockvideos.filter(custom_user__id=custom_user_id)
			if custom_user_unlocks.exists():
				custom_user_unlock = custom_user_unlocks.first()
				rank = list(unlockvideos).index(custom_user_unlock) + 1  # 当前用户完成项目考核排名
				customusers = CustomUser.objects.filter(id=custom_user_id).values(*self.user_info_list)
				if customusers.exists():
					customuser_dict = customusers.first()
					avatar = customuser_dict.get("avatar")
					customuser_dict.update({"avatar": os.path.join("/media", avatar)})
					customuser_dict.update({"rank": rank})
					technologys = self.get_technologys(custom_user_id)
					customuser_dict.update({"technologys": technologys})
					self.result_dict["custom_user"] = customuser_dict

			# 每个用户排名
			for one in unlockvideo_list:
				rank = list(unlockvideos).index(one) + 1
				one_user_dict = dict.fromkeys(self.user_info_list, "")
				one_user_dict.update({"rank": rank})
				user_id = one.get("custom_user")
				customusers = CustomUser.objects.filter(id=user_id).values(*self.user_info_list)
				if customusers.exists():
					customuser_dict = customusers.first()
					avatar = customuser_dict.get("avatar")
					customuser_dict.update({"avatar": os.path.join("/media", avatar)})
					one_user_dict.update(customuser_dict)

				# 获取项目对应技术方向
				technologys = self.get_technologys(user_id)
				one_user_dict.update({"technologys": technologys})

				self.result_dict["data"].append(one_user_dict)

		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))

	def get_technologys(self, user_id):
		"""获取通过考核的技术方向
		:param user_id: 用户ID
		:return:技术方向列表
		"""
		technologys = list()
		try:
			filter_dict = {
				"video__id__in": self.project_video_id_list,
				"custom_user__id": user_id

			}
			unlockvideos = UnlockVideo.objects.filter(**filter_dict).values_list("video", flat=True)
			projects = Project.objects.filter(video__id__in=unlockvideos)

			for one_project in projects:
				technologys.append(one_project.technology.name)
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return technologys
