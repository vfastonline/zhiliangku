#!encoding:utf-8
from django.views.generic import View

from backstage.home.models import *
from lib.permissionMixin import class_view_decorator, teacher_login_required
from lib.util import *
from applications.custom_user.models import CustomUser


@class_view_decorator(teacher_login_required)
class GetCustomUserClass(View):
	"""获取当前登录老师管理班级信息"""

	def __init__(self):
		super(GetCustomUserClass, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": [],
		}

	def get(self, request, *args, **kwargs):
		try:
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户(老师)ID
			CustomUser_class = CustomUser.objects
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))
