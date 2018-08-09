#!encoding:utf-8

from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView

from applications.tracks_learning.serializers import *
from lib.api_response_handler import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import *


@class_view_decorator(user_login_required)
class StudentNotesDetail(APIView):
	"""修改，删除"""

	@staticmethod
	def get_object(pk):
		try:
			return StudentNotes.objects.get(pk=pk)
		except StudentNotes.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		student_note = self.get_object(pk)
		serializer = StudentNotesSerializer(student_note)
		return JsonResponse(data=serializer.data, err=status.HTTP_200_OK)

	def patch(self, request, pk, format=None):
		student_note = self.get_object(pk)
		serializer = StudentNotesSerializer(student_note, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(data=serializer.data, err=status.HTTP_201_CREATED)
		return JsonResponse(serializer.errors, err=status.HTTP_400_BAD_REQUEST, msg="fail")

	def delete(self, request, pk, format=None):
		student_note = self.get_object(pk)
		student_note.delete()
		return JsonResponse(err=status.HTTP_204_NO_CONTENT, msg="success")


@class_view_decorator(user_login_required)
class StudentNotesList(APIView):
	"""查询，新增"""

	def get(self, request, *args, **kwargs):
		data = []
		paginator = dict()
		err = status.HTTP_204_NO_CONTENT
		msg = "success"
		try:
			video_id = str_to_int(request.GET.get('video_id', 0))  # 视频ID
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			page = self.request.GET.get("page", 1)  # 页码
			per_page = self.request.GET.get("per_page", 10)  # 每页显示条目数

			self.id_ = {"video__id": video_id, "custom_user__id": custom_user_id, }
			student_notes = StudentNotes.objects.filter(**self.id_)

			# 提供分页数据
			if not page: page = 1
			if not per_page: page = 10
			page_obj = Paginator(student_notes, per_page)
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
				student_notes = page_obj.page(page).object_list
			except:
				student_notes = list()

			serializer = StudentNotesSerializer(student_notes, many=True)
			data = serializer.data
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_404_NOT_FOUND
			msg = "fail"
		finally:
			return JsonResponse(data=data, err=err, msg=msg, paginator=paginator)

	def post(self, request, *args, **kwargs):
		"""
		:param request:{ "video":1, "custom_user":1, "title": "das11", "notes": "dadas11" }
		:param args:
		:param kwargs:
		:return:
		"""
		data = dict()
		err = status.HTTP_201_CREATED
		msg = "success"
		try:
			serializer = StudentNotesSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				data = serializer.data
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				data = serializer.errors
				msg = "fail"
				err = status.HTTP_400_BAD_REQUEST
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = status.HTTP_404_NOT_FOUND
			msg = "fail"
		finally:
			return JsonResponse(data=data, err=err, msg=msg)
