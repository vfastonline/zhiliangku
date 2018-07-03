#!encoding:utf-8

from django.shortcuts import render
from django.views.generic import View

from applications.tracks_learning.models import *
from backstage.home.models import LearnTask
from lib.permissionMixin import class_view_decorator, teacher_login_required
from lib.util import *


@class_view_decorator(teacher_login_required)
class BackStageHomePage(View):
	"""教师端-后台-首页"""

	def get(self, request, *args, **kwargs):
		template_name = "backstage/index/index.html"
		return render(request, template_name, {})


@class_view_decorator(teacher_login_required)
class SetTaskInfo(View):
	"""后台-获取任务信息"""

	def __init__(self):
		super(SetTaskInfo, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": list(),
		}

	def get(self, request, *args, **kwargs):
		try:
			info = str_to_int(request.GET.get('info', 0))  # 1：项目；2：课程；3：章节；4：视频
			pk_id = str_to_int(request.GET.get('pk_id', 0))  # 上一级主键ID

			if info == 1:
				self.result_dict["data"] = self.get_projects()
			elif info == 2:
				self.result_dict["data"] = self.get_courses(pk_id)
			elif info == 3:
				self.result_dict["data"] = self.get_sections(pk_id)
			elif info == 4:
				self.result_dict["data"] = self.get_videos(pk_id)
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))

	@staticmethod
	def get_projects():
		return list(Project.objects.values("id", "name"))

	@staticmethod
	def get_courses(pk_id):
		return list(Course.objects.filter(project__id=pk_id).values("id", "name"))

	@staticmethod
	def get_sections(pk_id):
		return list(Section.objects.filter(course__id=pk_id).values("id", "title"))

	@staticmethod
	def get_videos(pk_id):
		return list(Video.objects.filter(section__id=pk_id).values("id", "name"))

	def post(self, request, *args, **kwargs):
		try:
			param_dict = json.loads(request.body)
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			video_id = str_to_int(param_dict.get('video_id', 0))  # 视频ID

			custom_user = CustomUser.objects.get(id=custom_user_id)
			video = Video.objects.get(id=video_id)
			new_obj = LearnTask.objects.create(custom_user=custom_user, video=video)
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))
