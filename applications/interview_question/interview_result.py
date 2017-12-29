#!encoding:utf-8
import json
import logging
import traceback

from django.db.models import *
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from applications.interview_question.models import *
from lib.permissionMixin import class_view_decorator, user_login_required


@class_view_decorator(user_login_required)
class EnterpriseRsult(View):
    """面试结果--页面"""

    def get(self, request, *args, **kwargs):
        template_name = "interview_questions/enterprise/result/index.html"
        return render(request, template_name, {})


# @class_view_decorator(user_login_required)
class EnterpriseRsultInfo(View):
    """面试结果--数据"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": dict()}
        try:
            custom_user_id = int(self.request.GET.get('custom_user_id', 0))  # 用户ID
            enterpriseinfo_id = int(self.request.GET.get("enterpriseinfo_id", 0))  # 企业ID
            result_data = dict()
            enterpriseinfos = EnterpriseInfo.objects.filter(id=enterpriseinfo_id)

            if enterpriseinfos.exists():
                enterpriseinfo = enterpriseinfos.first()
                result_data["company"] = enterpriseinfo.company  # 出题方
                result_data["position"] = enterpriseinfo.position  # 招聘职位

                # 不同类型答题正确率, 分组查询
                qtype_list = enterpriseinfo.ExaminationQuestions.values('qtype').annotate(Count('qtype'))
                qtype_list = list(qtype_list)

                # 题型字典
                qtype_dict = dict(ExaminationQuestion.QTYPE)

                # 各题型增加中文类型
                for one in qtype_list:
                    one["qtype_name"] = qtype_dict.get(one.get("qtype"))  # 考题类型
                    print one

                # 用户在本次评测中的所有答题记录
                answerrecord_param = {
                    "custom_user_id": custom_user_id,
                    "question__in": enterpriseinfo.ExaminationQuestions.all(),
                    "result":True
                }
                answerrecords = AnswerRecord.objects.filter(**answerrecord_param).values('question__qtype')
                print answerrecords

                result_dict["data"] = result_data
            else:
                result_dict["msg"] = "企业面试题不存在"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
