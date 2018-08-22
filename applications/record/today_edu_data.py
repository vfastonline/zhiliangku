#!encoding:utf-8
from django.db.models import F
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.views import APIView

from applications.exercise.models import UserExercise
from applications.record.models import WatchRecord
from applications.tracks_learning.models import *
from lib.api_response_handler import JsonResponse
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int



@class_view_decorator(user_login_required)
class TodayEduData(APIView):
	"""今日教务数据"""

	def get(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success"}
		try:
			pass
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = 1
			msg = traceback.format_exc()
		finally:
			return JsonResponse(data=data, err=err, msg=msg)