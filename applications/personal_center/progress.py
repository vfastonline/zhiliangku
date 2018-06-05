#!encoding:utf-8
from django.db.models import Count
from django.views.generic import View

from applications.record.models import WatchRecord
from applications.tracks_learning.projects_list import project_summarize_course_progress
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import *


@class_view_decorator(user_login_required)
class GetLearningProgressInfo(View):
	"""个人中心-学习进度-信息"""

	def __init__(self):
		super(GetLearningProgressInfo, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": list(),
		}

	def get(self, request, *args, **kwargs):
		try:
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID

			# 对用户观看记录以项目信息分组查询
			watchrecords = WatchRecord.objects.filter(user__id=custom_user_id).values("course__project").annotate(
				Count('id'))
			time_line_dict = dict()
			for one in watchrecords:
				project_id = one.get("course__project")

				# 查询用户指定项目最近一次学习记录
				filter_param = {
					"user__id": custom_user_id,
					"course__project__id": project_id,
				}
				record = WatchRecord.objects.filter(**filter_param).order_by("-create_time").first()
				create_time = record.create_time.strftime('%Y-%m-%d %H:%M:%S')  # 最近一次项目学习记录时间

				# 项目详细信息
				detail = dict()
				detail["name"] = record.course.project.name
				detail["pathwel"] = record.course.project.pathwel.url if record.course.project.pathwel else ""

				courses = record.course.project.Courses.all()  # 项目下所有课程
				courses_count = courses.count()  # 课程数
				courses_schedule = 0
				for course in courses:
					# 汇总用户每个课程完成百分比
					summarize_param = [custom_user_id, course, list(courses)]
					summarize_dict = project_summarize_course_progress(*summarize_param)
					unlock = summarize_dict.get("unlock")

					# 课程未解锁，跳出汇总
					if not unlock:
						break
					courses_schedule += summarize_dict.get("schedule")
					learn_video_id = summarize_dict.get("learn_video_id")
					if learn_video_id:
						detail["learn_video_id"] = learn_video_id
						detail["video_process"] = summarize_dict.get("video_process")
						detail["learn_video_type"] = summarize_dict.get("learn_video_type")
						detail["learn_video_name"] = summarize_dict.get("learn_video_name")

				# 项目完成百分比
				detail["schedule"] = float(courses_schedule) / float(courses_count)
				time_line_dict[create_time] = detail

			# 对时间轴排序，观看时间倒序
			data_list = list()
			for i in sorted(time_line_dict.items(), key=lambda e: e[0], reverse=True):
				data_list.append({i[0]: i[1]})
			self.result_dict["data"] = data_list
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))
