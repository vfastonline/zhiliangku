#!encoding:utf-8
import json
import logging
import traceback

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from applications.interview_question.models import *
from lib.permissionMixin import class_view_decorator, user_login_required


@class_view_decorator(user_login_required)
class ExaminationQuestionList(View):
    """面试题--页面"""

    def get(self, request, *args, **kwargs):
        template_name = "interview_questions/examinationquestion/list/index.html"
        return render(request, template_name, {})


# @class_view_decorator(user_login_required)
class ExaminationQuestionListInfo(View):
    """所有面试题"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": list(), "paginator": dict()}
        try:
            # 按过滤条件查询
            enterprise_id = int(request.GET.get('enterprise_id', 0))  # 企业ID
            page = int(self.request.GET.get("page", 1))  # 页码

            data_list = list()
            questions = ExaminationQuestion.objects.filter(enterprise_id=enterprise_id)
            if questions.exists():
                # 分页处理
                page_obj = Paginator(questions, 1)
                total_count = page_obj.count  # 记录总数
                num_pages = page_obj.num_pages  # 总页数
                page_range = list(page_obj.page_range)  # 页码列表
                paginator_dict = {
                    "total_count": total_count,
                    "num_pages": num_pages,
                    "page_range": page_range,
                    "page": page,
                }
                result_dict["paginator"] = paginator_dict

                try:
                    questions = page_obj.page(page).object_list
                except:
                    questions = list()

                for question in questions:
                    question_dict = dict()
                    question_dict["id"] = question.id
                    question_dict["enterprise_id"] = question.enterprise_id
                    question_dict["title"] = question.title
                    answers = ExaminationAnswer.objects.filter(question=question).order_by("option")
                    answer_list = list()
                    for answer in answers:
                        answer_dict = dict()
                        answer_dict["id"] = answer.id
                        answer_dict["option"] = answer.option
                        answer_dict["option_name"] = answer.get_option_display()
                        answer_dict["content"] = answer.content
                        answer_list.append(answer_dict)
                    question_dict["answers"] = answer_list
                    data_list.append(question_dict)
            result_dict["data"] = data_list
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
