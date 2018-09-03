#!encoding:utf-8
from django.db.models import Count
from rest_framework import status
from rest_framework.views import APIView

from applications.custom_user.models import *
from applications.tracks_learning.models import *
from backstage.home.models import *
from lib.api_response_handler import JsonResponse
from online_status.models import *
from lib.permissionMixin import class_view_decorator, teacher_login_required

@class_view_decorator(teacher_login_required)
class TodayEduData(APIView):
	"""今日教务数据"""
	def get(self, request, *args, **kwargs):
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		data = list()
		try:
			class_id = self.request.GET.get("class_id")
			# class_id = 1
			today_date = get_day_of_day(0)  # 今日日期
			start_date = self.request.GET.get("start-date")
			end_date = self.request.GET.get("end_date")
			# start_date = "2018-08-28"
			# end_date = "2018-08-31"
			if start_date and end_date:
				days = date_days(start_date, end_date)  # 总天数
			else:
				start_date = str(get_day_of_day(0))
				days = 1
			if class_id:
				class_user_id = CustomUserClass.objects.filter(id=class_id).values("customuser__id")
				user_list = []
				for user_id in class_user_id:
					user_list.append(user_id["customuser__id"])
				# 考勤
				param = dict(id__in=user_list, onlinestatus__last_login__startswith=today_date)
				login_list = CustomUser.objects.filter(**param).annotate(
					count=Count("onlinestatus__last_login")).values("count")
				no_login = len(user_list) - len(login_list)

				# 违纪
				param = dict(custom_user__id__in=user_list, current_time__startswith=today_date, schedule__lt=1)
				sum_no_learn = UserLearnTaskSummary.objects.filter(**param).aggregate(sum_learn=Count("schedule")).get(
					"sum_learn", "")

				# 选定日期的考勤、违纪
				date_range_info = []
				for i in range(days):
					date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
					new_date = (date + datetime.timedelta(days=i)).strftime("%Y-%m-%d")

					param = dict(id__in=user_list, onlinestatus__last_login__startswith=new_date)
					date_range_login = CustomUser.objects.filter(**param).annotate(
						count=Count("onlinestatus__last_login")).values("count")

					no_login_rate = round((len(user_list) - len(date_range_login)) / len(user_list), 2)

					param = dict(custom_user__id__in=user_list, current_time__startswith=new_date, schedule__lt=1)
					sum_no_learn = UserLearnTaskSummary.objects.filter(**param).aggregate(
						sum_learn=Count("schedule")).get("sum_learn", "")

					no_learn_rate = round(sum_no_learn / len(user_list), 2)
					date_range_info.append(
						{"new_date": new_date, "no_login_rate": no_login_rate, "no_learn_rate": no_learn_rate})

				data = {
					"user_list": len(user_list),  # 总人数
					"no_login": no_login,  # 缺勤人数
					"sum_no_learn": sum_no_learn,  # 违纪人数
					"date_range_info": date_range_info,  # 选定日期区间的缺勤率和违纪率
				}

		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_500_INTERNAL_SERVER_ERROR
			msg = traceback.format_exc()
		finally:
			return JsonResponse(data=data, err=err, msg=msg)
