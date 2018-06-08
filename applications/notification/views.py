#!encoding:utf-8
from django.shortcuts import render
from django.views.generic import View

from applications.notification.models import *
from applications.tracks_learning.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import *


@class_view_decorator(user_login_required)
class MyNotification(View):
	"""我的消息-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "notification/list/index.html"
		return render(request, template_name, {})


@class_view_decorator(user_login_required)
class MyNotificationInfo(View):
	"""我的消息"""

	def __init__(self):
		super(MyNotificationInfo, self).__init__()
		self.result_dict = {"err": 0, "msg": "success", "data": [], "paginator": {}}

	def get(self, request, *args, **kwargs):
		try:
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			have_read = str_to_int(self.request.GET.get('have_read', 0))  # 是否已读，1：未读，2：已读
			page = self.request.GET.get("page", 1)  # 页码
			per_page = self.request.GET.get("per_page", 12)  # 每页显示条目数

			filter_parm = {
				"custom_user__id": custom_user_id,
			}
			if have_read == 1:
				filter_parm["have_read"] = False
			elif have_read == 2:
				filter_parm["have_read"] = True
			notifications = Notification.objects.filter(**filter_parm)

			# 提供分页数据
			if not page: page = 1
			if not per_page: per_page = 12
			page_obj = Paginator(notifications, per_page)
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
				notifications_objs = page_obj.page(page).object_list
			except:
				notifications_objs = list()

			data_list = list()
			for notification in notifications_objs:
				one_dict = dict()
				one_dict["id"] = notification.id
				one_dict["title"] = notification.title
				one_dict["content"] = notification.content
				one_dict["create_time"] = notification.create_time.strftime("%Y-%m-%d %X")
				one_dict["have_read"] = notification.have_read
				data_list.append(one_dict)
			self.result_dict["data"] = data_list
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class MyNotificationUnreadCount(View):
	"""我的未读消息总数"""

	def __init__(self):
		super(MyNotificationUnreadCount, self).__init__()
		self.result_dict = {"err": 0, "msg": "success", "total": 0}

	def get(self, request, *args, **kwargs):

		try:
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			usernotificationscounts = UserNotificationsCount.objects.filter(custom_user__id=custom_user_id)
			if usernotificationscounts.exists():
				self.result_dict["total"] = usernotificationscounts.first().unread_count
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class DeleteMyNotification(View):
	"""删除-我的消息"""

	def __init__(self):
		super(DeleteMyNotification, self).__init__()
		self.result_dict = {"err": 0, "msg": "success", "data": 0}

	def post(self, request, *args, **kwargs):

		try:
			param_dict = json.loads(request.body)
			pk_id = str_to_int(param_dict.get('pk_id', 0))  # 必填，消息ID
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			del_param = {
				"custom_user__id": custom_user_id,
				"id": pk_id
			}
			deleted, _rows_count = Notification.objects.filter(**del_param).delete()
			self.result_dict["data"] = deleted
			if not deleted:
				self.result_dict["msg"] = u"未找到消息"
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class MarkAsReadMyNotification(View):
	"""标记已读-我的消息"""

	def __init__(self):
		super(MarkAsReadMyNotification, self).__init__()
		self.result_dict = {"err": 0, "msg": "success"}

	def post(self, request, *args, **kwargs):

		try:
			param_dict = json.loads(request.body)
			pk_id = str_to_int(param_dict.get('pk_id', 0))  # 必填，消息ID
			whole = str_to_int(param_dict.get('whole', 0))  # 选填，全部标记已读
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID

			custom_user = CustomUser.objects.get(pk=custom_user_id)
			controller = NotificationController(custom_user)
			if whole:
				whole = True
			else:
				whole = False
			controller.mark_as_read(pk_id, whole)
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))
