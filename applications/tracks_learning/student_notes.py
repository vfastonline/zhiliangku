#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.tracks_learning.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int


@class_view_decorator(user_login_required)
class StudentNotesList(View):
	"""学生笔记列表"""

	def get(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success", "data": list()}
		try:
			video_id = str_to_int(request.GET.get('video_id', 0))  # 视频ID
			custom_user_id = str_to_int(request.GET.get('custom_user_id', 0))  # 用户ID

			data_list = list()
			if video_id:
				student_notes = StudentNotes.objects.filter(video__id=video_id, custom_user__id=custom_user_id)
				if student_notes.exists():
					for note in student_notes:
						note_dict = dict()
						note_dict["id"] = note.id
						note_dict["title"] = note.title
						note_dict["notes"] = note.notes
						note_dict["custom_user"] = note.custom_user.nickname if note.custom_user else ""
						note_dict["create_time"] = note.create_time.strftime("%Y-%m-%d %X")

						data_list.append(note_dict)
			result_dict["data"] = data_list
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class AddStudentNotes(View):
	"""增加--学生笔记列表"""

	def post(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success", "data": {}}
		try:
			# 获取查询参数
			param_dict = json.loads(request.body)
			video_id = str_to_int(param_dict.get('video_id', 0))
			custom_user_id = str_to_int(param_dict.get('custom_user_id', 0))
			title = param_dict.get('title', "")
			notes = param_dict.get('notes', "")

			if title and notes:
				custom_user = CustomUser.objects.filter(id=custom_user_id)
				video = Video.objects.filter(id=video_id)
				if video.exists() and custom_user.exists():
					create_dict = {
						"video": video.first(),
						"custom_user": custom_user.first(),
						"title": title,
						"notes": notes,
					}
					student_notes = StudentNotes.objects.create(**create_dict)
					if student_notes:
						result_dict["data"] = {
							"id": student_notes.id,
							"notes": student_notes.notes,
							"title": student_notes.title,
							"custom_user": student_notes.custom_user.nickname if student_notes.custom_user else "",
							"create_time": student_notes.create_time.strftime("%y-%m-%d %X"),
						}
				else:
					result_dict["msg"] = u"缺少视频信息或用户信息"
					result_dict["err"] = 1
			else:
				result_dict["msg"] = u"缺少笔记标题或内容"
				result_dict["err"] = 1
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class DeleteStudentNotes(View):
	"""删除--学生笔记列表"""

	def post(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success"}
		try:
			# 获取查询参数
			param_dict = json.loads(request.body)
			video_id = str_to_int(param_dict.get('video_id', 0))
			custom_user_id = str_to_int(param_dict.get('custom_user_id', 0))
			notes_id = str_to_int(param_dict.get('notes_id', 0))

			filter_parm = {
				"video__id": video_id,
				"custom_user__id": custom_user_id,
				"id": notes_id,
			}
			deleted, _rows_count = StudentNotes.objects.filter(**filter_parm).delete()
			if not deleted:
				result_dict["msg"] = u"未找到要删除的笔记信息"

		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
