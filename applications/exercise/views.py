#!encoding:utf-8
import json
import logging
import traceback

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from applications.exercise.models import *
from lib.permissionMixin import class_view_decorator, user_login_required


# @class_view_decorator(user_login_required)
class QuestionList(View):
    """习题-页面"""

    def get(self, request, *args, **kwargs):
        template_name = "exercise/question/list/index.html"
        return render(request, template_name, {})


# @class_view_decorator(user_login_required)
class QuestionListInfo(View):
    """习题详情"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": list(), "paginator": {}}
        try:
            # 获取查询参数
            # 按过滤条件查询
            section_id = int(request.GET.get('section_id', 0))  # 视频ID
            # status = request.GET.get('status')  # 问题状态，"0"：未解决；"1"：已解决
            # custom_user_id = int(request.GET.get('custom_user_id', 0))  # 提问用户ID
            # participate_custom_user_id = int(request.GET.get('participate_custom_user_id', 0))  # 回答用户ID,我参与的
            # follow_custom_user_id = int(request.GET.get('follow_custom_user_id', 0))  # 用户ID,我关注的
            # page = int(self.request.GET.get("page", 1))  # 页码
            # per_page = int(self.request.GET.get("per_page", 12))  # 每页显示条目数
            #
            # data_list = list()
            # search_param = {
            #     "status": status,
            #     "video__id": video_id,
            #     "user__id": custom_user_id,
            #     "FaqAnswer__user__id": participate_custom_user_id,
            #     "follow_user__id": follow_custom_user_id,
            # }
            # filter_dict = dict()
            # [filter_dict.update({query_field: param}) for query_field, param in search_param.items() if param]
            # faqs = Faq.objects.filter(**filter_dict).order_by("-create_time")
            # if faqs.exists():
            #     # 提供分页数据
            #     page_objs = Paginator(faqs, per_page)
            #     total_count = page_objs.count  # 记录总数
            #     num_pages = page_objs.num_pages  # 总页数
            #     page_range = list(page_objs.page_range)  # 页码列表
            #     paginator_dict = {
            #         "total_count": total_count,
            #         "num_pages": num_pages,
            #         "page_range": page_range,
            #         "page": page,
            #         "per_page": per_page
            #     }
            #     result_dict["paginator"] = paginator_dict
            #
            #     try:
            #         faqs = page_objs.page(page).object_list
            #     except:
            #         faqs = list()
            #
            #     for faq in faqs:
            #         faq_dict = dict()
            #         faq_dict["id"] = faq.id
            #         faq_dict["video_id"] = faq.video.id if faq.video else ""
            #         faq_dict["title"] = faq.title
            #         faq_dict["custom_user_id"] = faq.user.id
            #         faq_dict["custom_user_nickname"] = faq.user.nickname
            #         faq_dict["custom_user_avatar"] = faq.user.avatar.url
            #         faq_dict["browse_amount"] = faq.browse_amount
            #         faq_dict["create_time"] = faq.create_time.strftime("%Y-%m-%d")
            #         faq_dict["faq_answer_count"] = faq.FaqAnswer.all().count()
            #         faq_dict["status_name"] = faq.get_status_display()
            #         faq_dict["status"] = faq.status
            #         faq_dict["reward"] = faq.reward
            #         data_list.append(faq_dict)
            # result_dict["data"] = data_list
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
