#!encoding:utf-8
from django.shortcuts import render
from django.views.generic import View

from applications.tracks_learning.models import Project
from applications.tracks_learning.models import UnlockVideo
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import *


@class_view_decorator(user_login_required)
class FinishProjectList(View):
	"""用户完成项目-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "employment/finishprojectlist/list/index.html"
		return render(request, template_name, {})


@class_view_decorator(user_login_required)
class FinishProjectListInfo(View):
	"""用户完成项目-信息"""

	def __init__(self):
		super(FinishProjectListInfo, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": [],
			"paginator": {}
		}

	def get(self, request, *args, **kwargs):
		try:
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			name = request.GET.get("name", "")  # 项目名称
			page = request.GET.get("page", 1)  # 页码
			per_page = request.GET.get("per_page", 12)  # 每页显示条目数

			# 用户完成的所有考核ID列表
			unlockvideos = UnlockVideo.objects.filter(custom_user__id=custom_user_id)
			video_id_list = unlockvideos.values_list("video", flat=True)

			param = {
				"video__id__in": video_id_list,
				"name__icontains": name,
			}
			filter_param = get_kwargs(param)

			# 用户完成的所有项目考核
			projects = Project.objects.filter(**filter_param)

			# 提供分页数据
			if not page: page = 1
			if not per_page: page = 12
			page_obj = Paginator(projects, per_page)
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
				projects_list = page_obj.page(page).object_list
			except:
				projects_list = list()

			data_list = list()
			for one in projects_list:
				one_dict = dict()
				one_dict["id"] = one.id
				one_dict["name"] = one.name
				one_dict["desc"] = one.desc
				try:
					one_dict["update_time"] = unlockvideos.get(video=one.video).update_time.strftime("%Y-%m-%d")
				except:
					traceback.print_exc()
					one_dict["update_time"] = ""
				data_list.append(one_dict)
			self.result_dict["data"] = data_list
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))
