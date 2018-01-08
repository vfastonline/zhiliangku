#!encoding:utf-8
import json
import logging
import traceback

from django.core.paginator import Paginator
from django.db.models import *
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from applications.interview_question.models import *
from lib.permissionMixin import class_view_decorator, user_login_required


@class_view_decorator(user_login_required)
class EnterpriseInfoList(View):
    """企业信息--页面"""

    def get(self, request, *args, **kwargs):
        template_name = "interview_questions/enterpriseinfo/list/index.html"
        return render(request, template_name, {})


@class_view_decorator(user_login_required)
class EnterpriseInfoListInfo(View):
    """企业信息--分页数据"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": [], "paginator": {}}
        try:
            path_id = self.request.GET.get("path_id", 0)  # 方向
            is_completed = int(self.request.GET.get("is_completed", 0))  # 已完成
            custom_user_id = self.request.GET.get('custom_user_id', 0)  # 用户ID
            page = self.request.GET.get("page", 1)  # 页码
            per_page = self.request.GET.get("per_page", 12)  # 每页显示条目数

            filter_param = dict()
            if path_id:
                filter_param["path_id"] = path_id

            enterprise_info_objs = EnterpriseInfo.objects.filter(**filter_param)
            if is_completed:
                enterprise_info_id_list = CompletedInterviewQuestion.objects.filter(
                    interview_question__in=enterprise_info_objs, customuser_id=custom_user_id,
                    complete=True).values_list(
                    "interview_question", flat=True)
                enterprise_info_objs = EnterpriseInfo.objects.filter(id__in=enterprise_info_id_list)

            if enterprise_info_objs.exists():
                page_obj = Paginator(enterprise_info_objs, per_page)
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
                    enterprise_info_objs = page_obj.page(page).object_list
                except:
                    enterprise_info_objs = list()

            data_list = list()
            for one in enterprise_info_objs:
                one_dict = dict()
                one_dict["id"] = one.id
                one_dict["company"] = one.company
                one_dict["position"] = one.position
                one_dict["amount"] = one.amount
                one_dict["lowest_monthly_salary"] = one.lowest_monthly_salary
                one_dict["highest_monthly_salary"] = one.highest_monthly_salary
                one_dict["question_img"] = one.question_img.url
                if not is_completed:
                    one_dict["is_completed"] = 0
                    completeds = CompletedInterviewQuestion.objects.filter(customuser_id=custom_user_id,
                                                                           interview_question=one, complete=True)
                    if completeds.exists():
                        one_dict["is_completed"] = 1
                else:
                    one_dict["is_completed"] = 1

                data_list.append(one_dict)

            result_dict["data"] = data_list
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class EnterpriseInfoDetail(View):
    """企业面试题详情--页面"""

    def get(self, request, *args, **kwargs):
        template_name = "interview_questions/enterpriseinfo/detail/index.html"
        return render(request, template_name, {})


@class_view_decorator(user_login_required)
class EnterpriseInfoDetailInfo(View):
    """企业面试题--详情"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": dict()}
        try:
            enterpriseinfo_id = self.request.GET.get("enterpriseinfo_id", 0)  # 企业面试题ID
            enterpriseinfos = EnterpriseInfo.objects.filter(id=enterpriseinfo_id)
            if enterpriseinfos.exists():
                enterpriseinfo = enterpriseinfos.first()
                detail = dict()
                detail["id"] = enterpriseinfo.id
                detail["position"] = enterpriseinfo.position
                detail["amount"] = enterpriseinfo.amount
                detail["duration"] = enterpriseinfo.duration
                detail["detail"] = enterpriseinfo.detail
                detail["notes"] = enterpriseinfo.notes

                # 聚合查询，面试题总分
                score_sum = enterpriseinfo.ExaminationQuestions.aggregate(Sum('score')).get("score__sum")
                if score_sum:
                    detail["score_sum"] = score_sum
                else:
                    detail["score_sum"] = 0

                # 分组查询，各题型，题目数、分值
                qtype_list = enterpriseinfo.ExaminationQuestions.values('qtype').annotate(Sum('score'), Count('qtype'))
                qtype_list = list(qtype_list)

                # 题型字典
                qtype_dict = dict(ExaminationQuestion.QTYPE)

                # 各题型增加中文类型
                [one.update({"qtype_name": qtype_dict.get(one.get("qtype"))}) for one in qtype_list]

                detail["qtype_list"] = qtype_list
                result_dict["data"] = detail
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
