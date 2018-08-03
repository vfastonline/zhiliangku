#!encoding:utf-8

from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.custom_user.models import CustomUser
from lib.permissionMixin import class_view_decorator, teacher_login_required
from lib.util import *


@class_view_decorator(teacher_login_required)
class GetCustomUserClass(APIView):
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
			customusers = CustomUser.objects.filter(id=custom_user_id)
			if customusers.exists():
				class_s = customusers.first().class_s.all()
				if class_s.exists():
					for one in class_s:
						detail = dict()
						detail["id"] = one.id
						detail["name"] = one.name
						detail["technology"] = one.technology.name if one.technology else ""
						self.result_dict["data"].append(detail)
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			render = JSONRenderer().render(self.result_dict)
			return Response(render)
