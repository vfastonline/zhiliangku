#!encoding:utf-8

from django.views.generic import View

from applications.tracks_learning.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import *


@class_view_decorator(user_login_required)
class CommonQuestionList(View):
	"""视频常见问题列表"""

	def __init__(self):
		super(CommonQuestionList, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": list(),
			"paginator": dict()
		}

	def get(self, request, *args, **kwargs):
		try:
			# 获取查询参数
			video_id = str_to_int(request.GET.get('video_id', 0))
			page = self.request.GET.get("page", 1)  # 页码
			per_page = self.request.GET.get("per_page", 12)  # 每页显示条目数

			data_list = list()
			if video_id:
				common_problems = CommonQuestion.objects.filter(video__id=video_id).values()

				# 提供分页数据
				page_obj = Paginator(common_problems, per_page)
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
					common_problems_list = page_obj.page(page).object_list
				except:
					common_problems_list = list()

				data_list = list()
				for one in common_problems_list:
					one_dict = dict()
					one_dict["id"] = one.id
					one_dict["video_id"] = one.video.id
					one_dict["question"] = one.question
					one_dict["answer"] = one.answer
					data_list.append(one_dict)
			self.result_dict["data"] = data_list
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))
