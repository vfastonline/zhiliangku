#!encoding:utf-8
import json
import logging
import traceback

from django.core.paginator import Paginator
from django.db.models import *
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from applications.record.models import WatchRecord
from applications.tracks_learning.models import *
from lib.util import str_to_int


class ProjectList(View):
	"""项目-页面"""

	def get(self, request, *args, **kwargs):
		request.breadcrumbs([(u"主页", '/'), (u"项目", '/tracks/projects/list/')])
		template_name = "tracks/project/list/index.html"
		return render(request, template_name, {})


class ProjectListInfo(View):
	"""项目列表"""

	def get(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success", "data": []}
		try:
			projects = Project.objects.filter()
			result_dict["data"] = [
				{
					"id": one.id,
					"name": one.name,
					"desc": one.desc,
					"color": one.color,
				}
				for one in projects
			]
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class ProjectDetail(View):
	"""项目详情-页面"""

	def get(self, request, *args, **kwargs):
		request.breadcrumbs([(u"主页", '/'), (u"项目", '/tracks/projects/list/'), (u"项目详情", '/tracks/projects/detail/')])
		template_name = "tracks/project/detail/index.html"
		return render(request, template_name, {})


class ProjectDetailInfo(View):
	"""项目详情"""

	def get(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success", "data": [], "paginator": {}}
		try:
			filter_param = dict()
			project_id = str_to_int(request.GET.get('project_id', 0))
			custom_user_id = str_to_int(request.GET.get('custom_user_id', 0))
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
					detail["color"] = projects_obj.color

					courses = projects_obj.Courses.all().order_by("sequence")
					# 提供分页数据
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
					result_dict["paginator"] = paginator_dict

					try:
						course_objs = page_obj.page(page).object_list
					except:
						course_objs = list()

					# 项目下所有课程
					detail["courses"] = list()
					for course in course_objs:
						course_dict = {
							"id": course.id,
							"pathwel": course.pathwel.url if course.pathwel else "",
							"name": course.name,
							"desc": course.desc,
							"sequence": course.sequence,
							"lecturer": course.lecturer.nickname if course.lecturer else "",
							"avatar": course.lecturer.avatar.url if course.lecturer.avatar else "",
							"summary": {}
						}
						# 获取课程所有视频总时长
						summarize_dict = project_summarize_course_progress(custom_user_id, course)
						course_dict["summary"] = summarize_dict

						# 汇总当前用户完成百分比

						detail["courses"].append(course_dict)
			result_dict["data"] = detail
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


def project_summarize_course_progress(custom_user_id, course):
	"""汇总项目下每个课程完成进度
	:param custom_user_id:用户ID
	:param course:课程
	:return:课程学习进度
	"""
	result_dict = {
		"total_time": "",  # 课程总时长，秒
		"remaining_time": "",  # 用户剩余学习时长，秒
		"schedule": 0,  # 课程学习进度
		"is_study": 0,  # 是否有课程学习记录
		"learn_video_name": "",  # 最近一次学习视频名称
		"learn_video_id": "",  # 最近一次学习视频ID
		"learn_video_type": "",  # 最近一次学习视频类型
		"video_address": "",  # 最近一次学习视频地址
		"video_process": 0,  # 最近一次学习视频观看进度
	}
	try:
		# 课程时长
		sections = course.Section.all()
		duration_sum = Video.objects.filter(section__in=sections).aggregate(Sum('duration')).get("duration__sum")
		m, s = divmod(duration_sum, 60)
		h, m = divmod(m, 60)
		total_time_str = "%02d:%02d:%02d" % (h, m, s)
		result_dict["total_time"] = total_time_str

		if custom_user_id:

			# 用户已经看了多长时间
			watchrecords = WatchRecord.objects.filter(user_id=custom_user_id, course=course).order_by("-create_time")
			watch_total_time_sum = watchrecords.values("video_process").aggregate(Sum('video_process')).get(
				"video_process__sum")  # 秒

			# 计算剩余时长
			if duration_sum and watch_total_time_sum:
				one_watchrecord = watchrecords.first()
				last_time_learn = one_watchrecord.video.name  # 上次学到
				last_time_learn_id = one_watchrecord.video.id  # 上次学到视频ID
				address = one_watchrecord.video.address  # 上次学到视频地址
				last_time_learn_type = one_watchrecord.video.type  # 上次学到视频类型
				remaining_time = duration_sum - watch_total_time_sum
				schedule = float("%.2f" % (float(watch_total_time_sum) / float(duration_sum)))
				result_dict["is_study"] = 1
				result_dict["learn_video_name"] = last_time_learn  # 视频名称
				result_dict["learn_video_id"] = last_time_learn_id  # 视频ID
				result_dict["learn_video_type"] = last_time_learn_type  # 视频类型
				result_dict["address"] = address.url if address else ""  # 视频地址
				result_dict["video_process"] = one_watchrecord.video_process

			else:
				remaining_time = duration_sum
				schedule = 0

				# 默认最近最近学习第一章第一个视频
				course_sections = course.Section.order_by("sequence")
				if course_sections:
					last_time_learn_objs = course_sections.first().Videos.order_by("sequence")
					if last_time_learn_objs:
						last_time_learn_obj = last_time_learn_objs.first()
						result_dict["learn_video_name"] = last_time_learn_obj.name  # 上次学到
						result_dict["learn_video_id"] = last_time_learn_obj.id  # 上次学到视频ID
						result_dict["learn_video_type"] = last_time_learn_obj.type  # 上次学到视频类型
						result_dict[
							"video_address"] = last_time_learn_obj.address.url if last_time_learn_obj.address else ""

			m, s = divmod(remaining_time, 60)
			h, m = divmod(m, 60)
			remaining_time_str = "%02d:%02d:%02d" % (h, m, s)
			result_dict["remaining_time"] = remaining_time_str
			result_dict["schedule"] = schedule
	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())
	finally:
		return result_dict
