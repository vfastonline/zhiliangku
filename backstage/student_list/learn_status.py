# !encoding:utf-8

from rest_framework import status
from rest_framework.views import APIView

from backstage.exam_statistics.models import *
from backstage.home.models import *
from lib.api_response_handler import *
from lib.permissionMixin import class_view_decorator, teacher_login_required


@class_view_decorator(teacher_login_required)
class LearnStatus(APIView):
	"""
	学习状态
	"""

	def get(self, request, *args, **kwargs):
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		data = list()
		try:
			user_id = self.request.GET.get("user_id")
			# user_id = 6
			today_date = get_day_of_day(0)  # 今日日期
			if user_id:
				param = dict(custom_user__id=user_id, task__create_time=today_date)
				user_task_summary = UserLearnTaskSummary.objects.filter(**param).first()
				task_summary = user_task_summary.schedule
				data = {
					"task_summary": task_summary  # 今日任务完成率
				}

		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_500_INTERNAL_SERVER_ERROR
			msg = traceback.format_exc()

		finally:
			return JsonResponse(data=data, err=err, msg=msg)
