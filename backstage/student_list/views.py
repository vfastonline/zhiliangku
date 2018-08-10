#!encoding:utf-8

from django.db.models import Sum
from rest_framework import status
from rest_framework.views import APIView

from applications.record.models import *
from backstage.student_list.serializer import *
from lib.api_response_handler import *


from lib.permissionMixin import class_view_decorator, teacher_login_required



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
			name = self.request.GET.get("name", "")  # 姓名
			page = self.request.GET.get("page", 1)  # 页码
			per_page = self.request.GET.get("per_page", 10)  # 每页显示条目数

			param = dict(nickname__icontains=name)
			param = get_kwargs(param)
			user_list = CustomUser.objects.filter(**param)

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
				if watchrecords.exists():
					# 秒转时分秒
					total_duration_seconds = watchrecords.annotate(sum=Sum("video_process")).values("sum")
					total_duration_seconds = (list(total_duration_seconds))[0]["sum"]
					m, s = divmod(total_duration_seconds, 60)
					h, m = divmod(m, 60)
					total_duration_seconds = ("%02d:%02d:%02d" % (h, m, s))

					watchrecord = watchrecords.first()
					create_time = watchrecord.create_time.strftime("%Y-%m-%d %H:%M:%S")
					progress = (watchrecord.video_process) / (watchrecord.duration) * 100

					result = {
						"nickname": watchrecord.user.nickname,  # 姓名
						"project": watchrecord.course.project.name,  # 项目
						"course": watchrecord.course.name,  # 课程
						"section": watchrecord.video.section.title,  # 章节
						"video": watchrecord.video.name,  # 视频
						"progress": "%d%%" % progress,  # 进度
						"sum_progress": 11,  # 总进度
						"total_duration_seconds": total_duration_seconds,  # 累计观看时间
						"create_time": create_time  # 最新登录时间
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
