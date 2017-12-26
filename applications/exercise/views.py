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
            page = int(self.request.GET.get("page", 1))  # 页码
            per_page = int(self.request.GET.get("per_page", 1))  # 每页显示条目数

            data_list = list()
            questions = Question.objects.filter(section__id=section_id).order_by("sequence")
            if questions.exists():
                # 提供分页数据
                page_objs = Paginator(questions, per_page)
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
                    questions = page_objs.page(page).object_list
                except:
                    questions = list()

                for question in questions:
                    question_dict = dict()
                    question_dict["id"] = question.id
                    question_dict["section_id"] = question.section.id
                    question_dict["title"] = question.title
                    answers = Answer.objects.filter(question=question).order_by("option")
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


# @class_view_decorator(user_login_required)
class QuestionRightAnswerInfo(View):
    """返回习题正确答案"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": dict()}
        try:
            # 获取查询参数
            question_id = int(request.GET.get('question_id', 0))  # 视频ID

            questions = Question.objects.filter(id=question_id)
            if questions.exists():
                question_obj = questions.first()
                right_answer_dict = {
                    "right_answer_option": question_obj.right_answer,
                    "right_answer_option_name": question_obj.get_right_answer_display()
                }
                result_dict["data"] = right_answer_dict
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
