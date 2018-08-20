#!encoding:utf-8

from django.db.models import Sum
from rest_framework import status
from rest_framework.views import APIView

from applications.record.models import *
from backstage.exam_statistics.models import *
from backstage.home.models import *
from lib.api_response_handler import *
from lib.permissionMixin import class_view_decorator, teacher_login_required
from online_status.models import *


@class_view_decorator(teacher_login_required)
class StudentList(APIView):
	"""
	查询学员列表信息
	"""

	def get(self, request, *args, **kwargs):
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		data = list()
		paginator = dict()
		try:
			class_id = self.request.GET.get("class_id")
			# class_id=2
			name = self.request.GET.get("name", "")  # 姓名
			# name= "学员33"
			page = self.request.GET.get("page", 1)  # 页码
			per_page = self.request.GET.get("per_page", 10)  # 每页显示条目数

			param = dict(nickname__icontains=name)
			param = get_kwargs(param)
			user_list = CustomUser.objects.filter(**param, class_s__id=class_id)

			# 提供分页数据
			if not page: page = 1
			if not per_page: page = 10
			page_obj = Paginator(user_list, per_page)
			total_count = page_obj.count  # 记录总数
			num_pages = page_obj.num_pages  # 总页数
			page_range = list(page_obj.page_range)  # 页码列表
			paginator = {
				"total_count": total_count,
				"num_pages": num_pages,
				"page_range": page_range,
				"page": page,
				"per_page": per_page
			}

			try:
				user_list = page_obj.page(page).object_list
			except:
				user_list = list()

			data_list = []
			for user in user_list:
				watchrecords = WatchRecord.objects.filter(user=user).order_by('-create_time')
				# 最后登录时间
				last_login = OnlineStatus.objects.filter(user__id=user.id).order_by("-last_login").values(
					"last_login").first()
				last_login = last_login["last_login"]
				if watchrecords.exists():
					# 聚合查询学生观看总时长，秒转时分秒
					total_duration_seconds = watchrecords.aggregate(sum=Sum("total_duration")).get("sum", "")
					if total_duration_seconds:
						m, s = divmod(total_duration_seconds, 60)
						h, m = divmod(m, 60)
						total_duration_seconds = "%02d:%02d:%02d" % (h, m, s)

					watchrecord = watchrecords.first()
					progress = round((watchrecord.video_process) / (watchrecord.duration), 3)

					# 视频相关信息
					learn_node = watchrecord.course.project.name + watchrecord.course.name + watchrecord.video.section.title  + watchrecord.video.name
					result_video = {
						"nickname": watchrecord.user.nickname,  # 姓名
						"learn_node": learn_node,  # 项目
						"progress": progress,  # 进度
						"sum_progress": 0,  # 总进度
						"total_duration_seconds": total_duration_seconds,  # 累计观看时间
						"last_login": last_login  # 最新登录时间
					}
					data_list.append(result_video)
				else:
					result = {
						"nickname": user.nickname,  # 姓名
						"learn_node": None,  # 学习节点
						"last_login": last_login  # 最新登录时间
					}
					data_list.append(result)
			data = data_list
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_500_INTERNAL_SERVER_ERROR
			msg = traceback.format_exc()
		finally:
			return JsonResponse(data=data, err=err, msg=msg, paginator=paginator)