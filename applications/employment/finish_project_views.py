#!encoding:utf-8
from django.shortcuts import render
from django.views.generic import View

from lib.util import *
from lib.permissionMixin import class_view_decorator, user_login_required


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
			pass
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))
