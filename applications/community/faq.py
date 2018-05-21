#!encoding:utf-8
import json
import logging
import traceback

from django.core.paginator import Paginator
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from applications.community.models import *
from applications.tracks_learning.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int


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
            video_id = str_to_int(request.GET.get('video_id', 0))  # 视频ID
            status = request.GET.get('status')  # 问题状态，"0"：未解决；"1"：已解决
            custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
            participate_custom_user_id = str_to_int(request.GET.get('participate_custom_user_id', 0))  # 回答用户ID,我参与的
            follow_custom_user_id = str_to_int(request.GET.get('follow_custom_user_id', 0))  # 用户ID,我关注的
            page = self.request.GET.get("page", 1)  # 页码
            per_page = self.request.GET.get("per_page", 12)  # 每页显示条目数

            data_list = list()
            search_param = {
                "status": status,
                "video__id": video_id,
                "user__id": custom_user_id,
                "FaqAnswer__user__id": participate_custom_user_id,
                "follow_user__id": follow_custom_user_id,
            }
            filter_dict = dict()
            [filter_dict.update({query_field: param}) for query_field, param in search_param.items() if param]
            faqs = Faq.objects.filter(**filter_dict).order_by("-create_time")

            if faqs:
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
                    faq_dict["custom_user_nickname"] = faq.user.nickname
                    faq_dict["custom_user_avatar"] = faq.user.avatar.url
                    faq_dict["browse_amount"] = faq.browse_amount
                    faq_dict["create_time"] = faq.create_time.strftime("%Y-%m-%d")
                    faq_dict["faq_answer_count"] = faq.FaqAnswer.all().count()
                    faq_dict["status_name"] = faq.get_status_display()
                    faq_dict["status"] = faq.status
                    faq_dict["reward"] = faq.reward
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

                    for one_answer in faqanswer_objs:
                        answer_dict = dict()
                        answer_dict["id"] = one_answer.id
                        answer_dict["answer"] = one_answer.answer
                        answer_dict["create_time"] = one_answer.create_time.strftime("%Y-%m-%d")
                        answer_dict["custom_user_id"] = one_answer.user.id
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
                        for answer_reply in faqanswerreplys:
                            answer_reply_dict = dict()
                            answer_reply_dict["id"] = answer_reply.id
                            answer_reply_dict["reply"] = answer_reply.reply
                            answer_reply_dict["custom_user_id"] = answer_reply.user.id
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
            path_id = str_to_int(param_dict.get('path_id'))  # 问题方向
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
                paths = CoursePath.objects.filter(id=path_id)
                customusers = CustomUser.objects.filter(id=custom_user_id)

                if customusers.exists():
                    create_dict = {
                        "user": customusers.first(),
                        "title": title,
                        "description": description,
                    }
                    # 判断积分是否够
                    if customusers.filter(integral__gte=int(reward)).exists():
                        create_dict.update({"reward": reward})
                    if paths.exists():
                        create_dict.update({"path": paths.first()})
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
class FollowFaq(View):
    """关注这个问题"""

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
