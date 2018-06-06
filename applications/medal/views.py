#!encoding:utf-8

from django.views.generic import View

from applications.medal.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import *
from lib.util import str_to_int


@class_view_decorator(user_login_required)
class GetCustomUserMedal(View):
	"""获取用户勋章"""

	def __init__(self):
		super(GetCustomUserMedal, self).__init__()
		self.result_dict = {"err": 0, "msg": "success", "data": [], "total": 0}

	def get(self, request, *args, **kwargs):
		try:
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			data_list = list()

			customusermedals = CustomUserMedal.objects.filter(custom_user__id=custom_user_id)
			for one in customusermedals:
				detail = dict()
				detail["id"] = one.id
				detail["name"] = one.medal.name if one.medal else ""
				detail["name"] = one.medal.name
				detail["pathwel"] = one.medal.pathwel.url if one.medal.pathwel else ""
				detail["create_time"] = one.create_time.strftime("%Y-%m-%d")
				data_list.append(detail)
			self.result_dict["data"] = data_list
			self.result_dict["total"] = customusermedals.count()
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))
