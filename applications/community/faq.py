#!encoding:utf-8

from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView

from applications.community.models import *
from applications.tracks_learning.models import *
from lib.api_response_handler import *

from lib.permissionMixin import class_view_decorator, user_login_required, teacher_login_required

from lib.util import get_kwargs
from lib.util import str_to_int


# from models import *


@class_view_decorator(user_login_required)
class FaqList(View):
	"""问题-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "community/faq/list/index.html"
		return render(request, template_name, {})


@class_view_decorator(user_login_required)
class FaqListInfo(View):
	"""提问信息"""

	def get(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success", "data": list(), "paginator": {}}
		try:
			# 获取查询参数
			# 按过滤条件查询
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			video_id = str_to_int(request.GET.get('video_id', 0))  # 视频ID
			title = request.GET.get('title', 0)  # 标题
			status = request.GET.get('status')  # 问题状态，"0"：未解决；"1"：已解决
			ask = str_to_int(request.GET.get('ask', 0))  # 我的提问
			participate = str_to_int(request.GET.get('participate', 0))  # 我参与的
			follow = str_to_int(request.GET.get('follow', 0))  # 我关注的
			page = self.request.GET.get("page", 1)  # 页码
			per_page = self.request.GET.get("per_page", 12)  # 每页显示条目数

			data_list = list()
			search_param = {
				"status": status,
				"video__id": video_id,
			}
			if title:
				search_param.update({"title__icontains": title})
			if ask:
				search_param.update({"user__id": custom_user_id})
			if participate:
				search_param.update({"FaqAnswer__user__id": custom_user_id})
			if follow:
				search_param.update({"follow_user__id": custom_user_id})

			filter_dict = get_kwargs(search_param)
			faqs = Faq.objects.filter(**filter_dict).order_by("-create_time")

			# 提供分页数据
			if not page: page = 1
			if not per_page: page = 12
			page_objs = Paginator(faqs, per_page)
			total_count = page_objs.count  # 记录总数
			num_pages = page_objs.num_pages  # 总页数
			page_range = list(page_objs.page_range)  # 页码列表
			paginator_dict = {
				"total_count": total_count,
				"num_pages": num_pages,
				"page_range": page_range,
				"page": page,
				"per_page": per_page
			}
			result_dict["paginator"] = paginator_dict

			try:
				faqs = page_objs.page(page).object_list
			except:
				faqs = list()

			for faq in faqs:
				faq_dict = dict()
				faq_dict["id"] = faq.id
				faq_dict["video_id"] = faq.video.id if faq.video else ""
				faq_dict["title"] = faq.title
				faq_dict["custom_user_id"] = faq.user.id
				faq_dict["is_self"] = False
				if faq.user.id == custom_user_id:  # 是登录用户的提问，支持修改和删除
					faq_dict["is_self"] = True
				faq_dict["custom_user_nickname"] = faq.user.nickname
				faq_dict["custom_user_avatar"] = faq.user.avatar.url
				faq_dict["browse_amount"] = faq.browse_amount
				faq_dict["create_time"] = faq.create_time.strftime("%Y-%m-%d")
				faq_dict["faq_answer_count"] = faq.FaqAnswer.all().count()
				faq_dict["status_name"] = faq.get_status_display()
				faq_dict["status"] = faq.status
				faq_dict["reward"] = faq.reward
				try:
					faq.follow_user.get(id=custom_user_id)
					faq_dict["is_follow_user"] = 1
				except:
					faq_dict["is_follow_user"] = 0

				data_list.append(faq_dict)
			result_dict["data"] = data_list
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class FaqDetai(View):
	"""问题详情-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "community/faq/detail/index.html"
		return render(request, template_name, {})


@class_view_decorator(user_login_required)
class FaqDetaiInfo(View):
	"""提问信息详情"""

	def get(self, request, *args, **kwargs):
		result_dict = {
			"err": 0,
			"msg": "success",
			"data": {},
			"paginator": {}
		}
		try:
			# 获取查询参数
			faq_id = str_to_int(request.GET.get('faq_id', 0))  # 问题ID
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			page = self.request.GET.get("page", 1)  # 页码
			per_page = self.request.GET.get("per_page", 12)  # 每页显示条目数

			if faq_id:
				faqs = Faq.objects.filter(id=faq_id)
				if faqs.exists():
					faq = faqs.first()
					faq.browse_amount = F('browse_amount') + 1  # 增加浏览量
					faq.save()
					faq.refresh_from_db()

					faq_dict = dict()
					faq_dict["id"] = faq.id
					faq_dict["title"] = faq.title
					faq_dict["description"] = faq.description
					faq_dict["video_id"] = faq.video.id if faq.video else ""
					faq_dict["custom_user_id"] = faq.user.id
					faq_dict["is_self"] = False
					if faq.user.id == custom_user_id:  # 是登录用户的提问，支持修改和删除
						faq_dict["is_self"] = True
					faq_dict["custom_user_nickname"] = faq.user.nickname
					faq_dict["custom_user_avatar"] = faq.user.avatar.url
					faq_dict["browse_amount"] = faq.browse_amount
					faq_dict["create_time"] = faq.create_time.strftime("%Y-%m-%d")
					faq_dict["is_follow_user"] = 1 if faqs.filter(follow_user=custom_user_id).exists() else 0

					# 获取问题回答
					faq_answer_list = list()

					faqanswer_objs = list(set(list(faq.FaqAnswer.all())))
					if not page: page = 1
					if not per_page: page = 12
					page_obj = Paginator(faqanswer_objs, per_page)
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
						faqanswer_objs = page_obj.page(page).object_list
					except:
						faqanswer_objs = list()

					for one_answer in faqanswer_objs:  # 回答
						answer_dict = dict()
						answer_dict["id"] = one_answer.id
						answer_dict["answer"] = one_answer.answer
						answer_dict["create_time"] = one_answer.create_time.strftime("%Y-%m-%d")
						answer_dict["custom_user_id"] = one_answer.user.id
						answer_dict["is_self"] = False
						if one_answer.user.id == custom_user_id:  # 是登录用户的回答，支持修改和删除
							answer_dict["is_self"] = True
						answer_dict["custom_user_nickname"] = one_answer.user.nickname
						answer_dict["custom_user_avatar"] = one_answer.user.avatar.url
						answer_dict["approve"] = one_answer.approve
						answer_dict["oppose"] = one_answer.oppose
						answer_dict["optimal"] = one_answer.optimal
						faqanswerreplys = one_answer.FaqAnswerReply.all()
						answer_dict["answer_reply_amount"] = faqanswerreplys.count()
						faqanswerfeedbacks = FaqAnswerFeedback.objects.filter(faqanswer=one_answer,
																			  user__id=custom_user_id)
						answer_dict["feedback"] = ""
						try:
							if faqanswerfeedbacks.exists():
								feedback = faqanswerfeedbacks.first().feedback
								answer_dict["feedback"] = feedback
						except:
							traceback.print_exc()

						# 获取问题回答回复
						faq_answer_reply_list = list()
						for answer_reply in faqanswerreplys:  # 问题-回答-回复
							answer_reply_dict = dict()
							answer_reply_dict["id"] = answer_reply.id
							answer_reply_dict["reply"] = answer_reply.reply
							answer_reply_dict["custom_user_id"] = answer_reply.user.id
							answer_reply_dict["is_self"] = False
							if answer_reply.user.id == custom_user_id:  # 问题-回答-回复是登录用户，支持修改和删除
								answer_reply_dict["is_self"] = True
							answer_reply_dict["custom_user_nickname"] = answer_reply.user.nickname
							answer_reply_dict["custom_user_avatar"] = answer_reply.user.avatar.url
							answer_reply_dict["create_time"] = answer_reply.create_time.strftime("%Y-%m-%d %H:%M")
							answer_reply_dict["role"] = "发问人"
							if one_answer.user == answer_reply.user:
								answer_reply_dict["role"] = "答主"

							faq_answer_reply_list.append(answer_reply_dict)
						answer_dict["answer_reply_list"] = faq_answer_reply_list
						faq_answer_list.append(answer_dict)
					if faq_answer_list:
						faq_dict["faq_answer_list"] = faq_answer_list

					result_dict["data"] = faq_dict
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class GetFaqByTitle(View):
	"""根据问题标题查询类似问题个数"""

	def get(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success", "data": 0}
		try:
			title = request.GET.get('title')  # 问题标题
			faqs_count = Faq.objects.filter(title__icontains=title).count()
			result_dict["data"] = faqs_count
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class FollowFaq(View):
	"""关注-这个问题"""

	def post(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success"}
		try:
			param_dict = json.loads(request.body)
			faq_id = str_to_int(param_dict.get('faq_id', 0))  # 必填，问题ID
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID

			faqs = Faq.objects.filter(id=faq_id)
			customusers = CustomUser.objects.filter(id=custom_user_id)
			if faqs.exists():
				if customusers.exists():
					faqs.first().follow_user.add(customusers.first())
				else:
					result_dict["err"] = 1
					result_dict["msg"] = "缺少关注用户ID"
			else:
				result_dict["err"] = 1
				result_dict["msg"] = "缺少关注问题ID"
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class UnFollowFaq(View):
	"""取消关注-这个问题"""

	def post(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success"}
		try:
			param_dict = json.loads(request.body)
			faq_id = str_to_int(param_dict.get('faq_id', 0))  # 必填，问题ID
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID

			faqs = Faq.objects.filter(id=faq_id)
			customusers = CustomUser.objects.filter(id=custom_user_id)
			if faqs.exists():
				if customusers.exists():
					faqs.first().follow_user.remove(customusers.first())
				else:
					result_dict["err"] = 1
					result_dict["msg"] = "缺少关注用户ID"
			else:
				result_dict["err"] = 1
				result_dict["msg"] = "缺少关注问题ID"
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class AddFaq(View):
	"""提问"""

	def post(self, request, *args, **kwargs):
		result_dict = {"err": 1, "msg": ""}
		try:
			# 提问参数
			param_dict = json.loads(request.body)
			video_id = str_to_int(param_dict.get('video_id', 0))  # 视频ID
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			title = param_dict.get('title')  # 必填，标题
			description = param_dict.get('description')  # 必填，问题描述
			reward = param_dict.get('reward', 0)  # 悬赏

			required_dict = {"用户ID": custom_user_id, "问题标题": title, "问题描述": description}
			required_param = 1
			for param_name, param_value in required_dict.items():
				if not param_value:
					result_dict["err"] = 1
					result_dict["msg"] = "".join(["缺少 ", param_name])
					required_param = 0
					break

			# 提问参数全部合法
			if required_param:
				videos = Video.objects.filter(id=video_id)
				customusers = CustomUser.objexcts.filter(id=custom_user_id)

				if customusers.exists():
					create_dict = {
						"user": customusers.first(),
						"title": title,
						"description": description,
					}
					# 判断积分是否够
					if customusers.filter(integral__gte=int(reward)).exists():
						create_dict.update({"reward": reward})
					if videos.exists():
						create_dict.update({"video": videos.first()})
					faq_obj = Faq.objects.create(**create_dict)
					if not faq_obj:
						result_dict["msg"] = "提问失败"
					else:
						result_dict["err"] = 0
						result_dict["msg"] = "成功提问"
				else:
					result_dict["msg"] = "没有对应视频或提问者信息"
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class DelFaq(View):
	"""删除-提问"""

	def __init__(self):
		super(DelFaq, self).__init__()
		self.result_dict = {"err": 0, "msg": "success", "data": 0}

	def post(self, request, *args, **kwargs):
		try:
			param_dict = json.loads(request.body)
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			faq_id = str_to_int(param_dict.get('faq_id', 0))  # 问题ID

			faqs = Faq.objects.filter(user__id=custom_user_id, id=faq_id)
			if faqs.exists():
				deleted, _rows_count = faqs.delete()
				self.result_dict["data"] = deleted
			else:
				self.result_dict["msg"] = "只有提问者才能删除"
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class EditFaq(View):
	"""编辑-提问"""

	def __init__(self):
		super(EditFaq, self).__init__()
		self.result_dict = {"err": 0, "msg": "success", "data": dict()}

	def post(self, request, *args, **kwargs):
		try:
			param_dict = json.loads(request.body)
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			faq_id = str_to_int(param_dict.get('faq_id', 0))  # 问题ID
			title = param_dict.get('title', "")  # 问题标题
			description = param_dict.get('description', "")  # 问题描述

			faqs = Faq.objects.filter(user__id=custom_user_id, id=faq_id)
			if faqs.exists():
				update_param = {
					"title": title,
					"description": description,
				}
				update_count = faqs.update(**update_param)
				if update_count:
					self.result_dict["data"] = update_param
			else:
				self.result_dict["msg"] = "只有提问者才能编辑"
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


@class_view_decorator(teacher_login_required)
class CountFaq(APIView):
	"""问答统计"""

	def get(self, request, *args, **kwargs):
		err = 0
		msg = "success"
		data = dict(total_question=0, total_answer=0, acception_time=0, teacher_answer=0, unsloved=0)
		try:
			total_question = Faq.objects.count()  # 问题总数
			total_answer = FaqAnswer.objects.count()  # 回答次数
			acception_time = Faq.objects.filter(status="1").count()  # 采纳次数
			teacher_answer = FaqAnswer.objects.filter(user__role=1).count()  # 老师回答
			unsloved = Faq.objects.filter(status="0").count()  # 未解决
			data = {
				"total_question": total_question,
				"total_answer": total_answer,
				"acception_time": acception_time,
				"teacher_answer": teacher_answer,
				"unsloved": unsloved,
			}
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			err = 1
			msg = traceback.format_exc()
		finally:
			return JsonResponse(data=data, err=err, msg=msg)
