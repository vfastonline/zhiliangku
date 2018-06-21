#!encoding:utf-8
from django.db.models import *
from django.shortcuts import render
from django.views.generic import View

from applications.record.models import WatchRecord
from applications.tracks_learning.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import *


class TechnologyListInfo(View):
	"""技术类别列表"""

	def get(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success", "data": []}
		try:
			technologys = Technology.objects.all()
			data_list = list()
			for technology in technologys:
				one_dict = dict()
				one_dict["id"] = technology.id
				one_dict["name"] = technology.name
				one_dict["desc"] = technology.desc
				data_list.append(one_dict)
			result_dict["data"] = data_list
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class ProjectsList(View):
	"""项目-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "tracks/projects/list/index.html"
		return render(request, template_name, {})


class ProjectsListInfo(View):
	"""项目列表"""

	def __init__(self):
		super(ProjectsListInfo, self).__init__()
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": [],
			"paginator": {},
			"breadcrumbs": "",
			"general_assessment": {}
		}

	def get(self, request, *args, **kwargs):
		try:
			name = request.GET.get('name', "")  # 项目名称，支持模糊查询
			self.technology_id = str_to_int(request.GET.get('technology_id', 0))  # 技术方向ID
			home_show = str_to_int(request.GET.get('home_show', 0))  # 是否首页展示
			page = self.request.GET.get("page", 1)  # 页码
			per_page = self.request.GET.get("per_page", 12)  # 每页显示条目数

			# 技术方向--所有项目--总考核
			self.get_technology_assessment()

			if home_show:
				param_dict = {
					"home_show": True
				}
			else:
				param_dict = {
					"technology_id": self.technology_id,
					"name__icontains": name
				}
			filter_dict = dict()
			for key, val in param_dict.items():
				if val:
					filter_dict[key] = val

			projects = Project.objects.filter(**filter_dict)

			# 提供分页数据
			if not page: page = 1
			if not per_page: per_page = 12
			page_obj = Paginator(projects, per_page)
			total_count = page_obj.count  # 记录总数
			num_pages = page_obj.num_pages  # 总页数
			page_range = list(page_obj.page_range)  # 页码列表
			paginator_dict = {
				"total_count": total_count,
				"num_pages": num_pages,
				"page_range": page_range,
				"page": page,
				"per_page": per_page
			}

			self.result_dict["paginator"] = paginator_dict
			try:
				projects_objs = page_obj.page(page).object_list
			except:
				projects_objs = list()

			data_list = list()
			for one in projects_objs:
				one_dict = {
					"id": one.id,
					"name": one.name,
					"desc": one.desc,
					"is_lock": one.is_lock,
					"home_show": one.home_show,
					"pathwel": one.pathwel.url if one.pathwel else "",
					"technology": {"name": one.technology.name},
					"video": {
						"id": one.video.id if one.video else "",
						"docker": one.video.docker.id if one.video and one.video.docker else "",
						"docker_name": one.video.docker.name if one.video and one.video.docker else "",
					}
				}
				# 计算项目所有课程总时长
				courses = one.Courses.all()
				duration_sum = 0
				for course in courses:
					sections = course.Section.all()
					duration_sum = Video.objects.filter(section__in=sections).aggregate(Sum('duration')).get(
						"duration__sum")
				m, s = divmod(duration_sum, 60)
				h, m = divmod(m, 60)
				total_time_str = "%02d:%02d:%02d" % (h, m, s)
				one_dict["total_time"] = total_time_str

				data_list.append(one_dict)

			self.result_dict["data"] = data_list

			# 面包屑
			self.make_breadcrumbs()
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))

	def make_breadcrumbs(self):
		"""制作面包屑"""
		try:
			self.request.breadcrumbs([(u"主页", reverse('home')), (u"项目", reverse('tracks:projects'))])
			self.result_dict["breadcrumbs"] = make_bread_crumbs(self.request)
		except:
			traceback.print_exc()

	def get_technology_assessment(self):
		"""获取技术方向下总考核信息
		:return:
		"""
		try:
			if self.technology_id:
				technologys = Technology.objects.filter(id=self.technology_id)
				if technologys.exists():
					video_obj = technologys.first().video
					if video_obj:
						video_dict = {
							"id": video_obj.id,
							"docker": video_obj.docker.id if video_obj.docker else "",
							"docker_name": video_obj.docker.name if video_obj.docker else "",
						}
						self.result_dict["general_assessment"] = video_dict
		except:
			traceback.print_exc()


@class_view_decorator(user_login_required)
class ProjectsDetail(View):
	"""项目详情-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "tracks/projects/detail/index.html"
		return render(request, template_name, {})


@class_view_decorator(user_login_required)
class ProjectsDetailInfo(View):
	"""项目详情"""

	def __init__(self):
		super(ProjectsDetailInfo, self).__init__()
		self.result_dict = {"err": 0, "msg": "success", "data": [], "paginator": {}}

	def get(self, request, *args, **kwargs):
		try:
			filter_param = dict()
			project_id = str_to_int(request.GET.get('project_id', 0))
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			page = self.request.GET.get("page", 1)  # 页码
			per_page = self.request.GET.get("per_page", 12)  # 每页显示条目数

			detail = dict()
			if project_id:
				filter_param["id"] = project_id
				projects = Project.objects.filter(**filter_param)
				if projects.exists():
					projects_obj = projects.first()
					detail["id"] = projects_obj.id
					detail["name"] = projects_obj.name
					detail["desc"] = projects_obj.desc

					courses = projects_obj.Courses.all().order_by("sequence")
					# 提供分页数据
					if not page: page = 1
					if not per_page: per_page = 12
					page_obj = Paginator(courses, per_page)
					total_count = page_obj.count  # 记录总数
					num_pages = page_obj.num_pages  # 总页数
					page_range = list(page_obj.page_range)  # 页码列表
					paginator_dict = {
						"total_count": total_count,
						"num_pages": num_pages,
						"page_range": page_range,
						"page": page,
						"per_page": per_page
					}
					self.result_dict["paginator"] = paginator_dict

					try:
						course_objs = page_obj.page(page).object_list
					except:
						course_objs = list()

					# 项目下所有课程
					detail["courses"] = list()
					for course in course_objs:
						course_dict = {
							"id": course.id,
							"name": course.name,
							"desc": course.desc,
							"sequence": course.sequence,
							"lecturer": course.lecturer.nickname if course.lecturer else "",
							"avatar": course.lecturer.avatar.url if course.lecturer else "",
							"summary": {}
						}
						# 获取课程所有视频总时长
						summarize_param = [custom_user_id, course, list(courses)]
						summarize_dict = project_summarize_course_progress(*summarize_param)
						course_dict["summary"] = summarize_dict
						detail["courses"].append(course_dict)
			self.result_dict["data"] = detail

			# 面包屑
			self.make_breadcrumbs()
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))

	def make_breadcrumbs(self):
		"""制作面包屑"""
		try:
			self.request.breadcrumbs([
				(u"主页", reverse('home')),
				(u"项目", reverse('tracks:projects')),
				(u"项目课程", "#"),
			])
			self.result_dict["breadcrumbs"] = make_bread_crumbs(self.request)
		except:
			traceback.print_exc()


def project_summarize_course_progress(custom_user_id, course, courses=list(), previous_num=1):
	"""汇总项目下每个课程完成进度
	:param custom_user_id:用户ID
	:param course:当前要汇总的课程
	:param courses:项目下所有课程列表
	:param previous_num:前几个课程
	:return:课程学习进度
	"""
	result_dict = {
		"total_time": "",  # 课程总时长，时分秒
		"remaining_time": "",  # 用户剩余学习时长，时分秒
		"schedule": 0,  # 课程学习进度， 完成学习：1；未开始：0；正在学习 0< schedule <1
		"is_study": 0,  # 是否有课程学习记录
		"learn_course_id": "",  # 最近一次学习课程ID
		"learn_video_name": "",  # 最近一次学习视频名称
		"learn_video_id": "",  # 最近一次学习视频ID
		"learn_video_type": "",  # 最近一次学习视频类型
		"video_process": 0,  # 最近一次学习视频观看进度
		"unlock": False,  # 课程是否解锁
	}
	try:
		# 获取当前课程上一个课程
		previous_course = None
		previous_index = courses.index(course) - previous_num
		if previous_index >= 0:
			previous_course = courses[previous_index]

		# 判断是否解锁
		if not previous_course:  # 没有上一个课程，本课程解锁
			result_dict["unlock"] = True
		else:
			previous_course_has_assessment = False  # 上一个课程的章节中有考核
			sections = previous_course.Section.order_by("-sequence")  # 章节倒序
			for one_section in sections:
				assessment_video = one_section.Videos.filter(type="3")  # 上一个课程->章节->考核
				if assessment_video.exists():
					previous_course_has_assessment = True
					filter_param = {
						"custom_user__id": custom_user_id,
						"video": assessment_video.first()
					}
					unlockvideos = UnlockVideo.objects.filter(**filter_param)
					if unlockvideos.exists():
						result_dict["unlock"] = True
						break

			# 上一个课程所有章节中都没有考核
			if not previous_course_has_assessment:
				# 迭代查找上一个课程是否有通过考核
				return project_summarize_course_progress(custom_user_id, course, courses, previous_num + 1)

		# 聚合查询课程总时长
		sections = course.Section.all()
		duration_sum = Video.objects.filter(section__in=sections).aggregate(Sum('duration')).get("duration__sum", 0)
		m, s = divmod(str_to_int(duration_sum), 60)
		h, m = divmod(m, 60)
		result_dict["total_time"] = "%02d:%02d:%02d" % (h, m, s)

		if custom_user_id:

			# 用户观看课程记录
			watchrecords = WatchRecord.objects.filter(user_id=custom_user_id, course=course).order_by("-create_time")

			# 观看记录总秒数
			watch_total_time_sum = watchrecords.values("video_process").aggregate(Sum('video_process')).get(
				"video_process__sum")  # 秒

			# 计算剩余时长
			if duration_sum and watch_total_time_sum:
				watchrecord = watchrecords.first()
				remaining_time = duration_sum - watch_total_time_sum
				schedule = float("%.2f" % (float(watch_total_time_sum) / float(duration_sum)))
				result_dict["is_study"] = 1
				result_dict["learn_video_name"] = watchrecord.video.name  # 视频名称
				result_dict["learn_video_id"] = watchrecord.video.id  # 视频ID
				result_dict["learn_video_type"] = watchrecord.video.type  # 视频类型
				result_dict["vid"] = watchrecord.video.vid  # 视频地址
				result_dict["video_process"] = watchrecord.video_process

			else:
				remaining_time = duration_sum
				schedule = 0

				# 默认最近最近学习第一章第一个视频
				course_sections = sections.order_by("sequence")
				if course_sections:
					video_objs = course_sections.first().Videos.order_by("sequence")
					if video_objs:
						video_obj = video_objs.first()
						result_dict["learn_video_name"] = video_obj.name  # 上次学到
						result_dict["learn_video_id"] = video_obj.id  # 上次学到视频ID
						result_dict["learn_video_type"] = video_obj.type  # 上次学到视频类型
						result_dict["video_vid"] = video_obj.vid

			m, s = divmod(remaining_time, 60)
			h, m = divmod(m, 60)
			result_dict["remaining_time"] = "%02d:%02d:%02d" % (h, m, s)
			result_dict["schedule"] = schedule
	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())
		return result_dict
	return result_dict
