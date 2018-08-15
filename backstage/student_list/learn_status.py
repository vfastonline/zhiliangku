
#!encoding:utf-8

from rest_framework import status
from rest_framework.views import APIView

from applications.record.models import *
from backstage.exam_statistics.models import *
from backstage.home.models import *
from lib.api_response_handler import *
from lib.permissionMixin import class_view_decorator, teacher_login_required
from online_status.models import *



# @class_view_decorator(teacher_login_required)
class LearnStatus(APIView):
	"""
	学习状态
	"""

	def get(self, request, *args, **kwargs):
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		data = list()
		try:
			name = self.request.GET.get("name", "")#==========================================
			date = "2018-08-19 00:00:00"  # self.request.GET.get("date", "")
			today_date = get_day_of_day(0)
			if name:
				param = dict(nickname__icontains=name)
				param = get_kwargs(param)
				user_list = CustomUser.objects.filter(**param)
				data_list = []

				print("user_list",user_list)

				for user in user_list:#=====================
					filter_dict = dict(custom_user=user, task__create_time=today_date)
					learntasksummary = UserLearnTaskSummary.objects.filter(**filter_dict).values("schedule")

					result = {
						"learntasksummary": learntasksummary  # 任务百分比
					}
					data_list.append(result)
				data = data_list
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_500_INTERNAL_SERVER_ERROR
			msg = traceback.format_exc()

		finally:
			return JsonResponse(data=data, err=err, msg=msg)




