#!encoding:utf-8
import json
import logging
import traceback

from django.db.models import *
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from applications.interview_question.models import *
from applications.tracks_learning.models import Course
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int


@class_view_decorator(user_login_required)
class EnterpriseRsult(View):
    """面试结果--页面"""

    def get(self, request, *args, **kwargs):
        template_name = "interview_questions/enterprise/result/index.html"
        return render(request, template_name, {})


@class_view_decorator(user_login_required)
class EnterpriseRsultInfo(View):
    """面试结果--数据"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": dict()}
        try:
            result_data = dict()
            custom_user_id = str_to_int(self.request.GET.get('custom_user_id', 0))  # 用户ID
            enterpriseinfo_id = str_to_int(self.request.GET.get("enterpriseinfo_id", 0))  # 企业ID

            enterpriseinfos = EnterpriseInfo.objects.filter(id=enterpriseinfo_id)
            if enterpriseinfos.exists():
                enterpriseinfo = enterpriseinfos.first()
                result_data["company"] = enterpriseinfo.company  # 出题方
                result_data["position"] = enterpriseinfo.position  # 招聘职位

                # 本次评测中的所有答题记录
                answerrecord_param = {
                    "custom_user_id": custom_user_id,
                    "question__in": enterpriseinfo.ExaminationQuestions.all(),
                    # "result": True
                }
                answerrecord_objs = AnswerRecord.objects.filter(**answerrecord_param)
                answerrecords = answerrecord_objs.filter(result=True).values('question__qtype').annotate(
                    Count('question__qtype'))
                answer_record_dict = {}  # {考题类型：答对个数}
                for one_record in answerrecords:
                    if not answer_record_dict.has_key(one_record["question__qtype"]):
                        answer_record_dict[one_record["question__qtype"]] = one_record["question__qtype__count"]
                    else:
                        answer_record_dict[one_record["question__qtype"]] += one_record["question__qtype__count"]
                # 汇总未掌握技能点
                wrong_answerrecords = answerrecord_objs.filter(result=False)
                tech_name_list = list()
                course_list = list()
                for one_record in wrong_answerrecords:
                    all_tech = one_record.question.tech.all()
                    course_list = list(set(course_list).union(set(Course.objects.filter(tech__in=all_tech))))
                    tech_name_list = list(set(tech_name_list).union(set(all_tech.values_list("name", flat=True))))
                result_data["tech_name_list"] = tech_name_list

                # 组装推荐课程信息
                result_data["course_list"] = [
                    {
                        "id": one.id,
                        "name": one.name,
                        "tech": [one_tech.name for one_tech in one.tech.all()] if one.tech.all().exists() else list(),
                        "course_img": one.course_img.url if one.course_img else "",
                        "lecturer": one.lecturer.nickname if one.lecturer else "",
                        "avatar": one.lecturer.avatar.url if one.lecturer.avatar else "",
                    }
                    for one in course_list
                ]

                # 不同类型答题正确率, 分组查询
                qtype_list = enterpriseinfo.ExaminationQuestions.values('qtype').annotate(Count('qtype'))
                qtype_list = list(qtype_list)

                # 题型字典
                qtype_dict = dict(ExaminationQuestion.QTYPE)

                # 各题型增加中文类型,答题正确个数
                for one in qtype_list:
                    one["qtype_name"] = qtype_dict.get(one.get("qtype"))  # 考题类型
                    one["right_qtype__count"] = answer_record_dict.get(one.get("qtype"), 0)
                result_data["qtype_list"] = qtype_list

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
