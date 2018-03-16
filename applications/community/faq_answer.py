#!encoding:utf-8
import json
import logging
import traceback

from django.db.models import F
from django.http import HttpResponse
from django.views.generic import View

from applications.community.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int


@class_view_decorator(user_login_required)
class AppraisalFaqAnswer(View):
    """问题回复，反对/支持"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": {}}
        try:
            param_dict = json.loads(request.body)
            faq_answer_id = str_to_int(param_dict.get('faq_answer_id', 0))  # 必填，问题回复ID
            appraisal = param_dict.get('appraisal')  # 必填，赞同：approve， 反对：oppose

            if faq_answer_id and appraisal:
                faqanswers = FaqAnswer.objects.filter(id=faq_answer_id)
                if faqanswers.exists():
                    faqanswer = faqanswers.first()
                    if appraisal == "approve":
                        faqanswer.approve = F('approve') + 1  # 支持
                    elif appraisal == "oppose":
                        faqanswer.oppose = F('oppose') + 1  # 反对
                    faqanswer.save()
                    faqanswer.refresh_from_db()
                    FaqAnswerFeedback.objects.create(faqanswer=faqanswer, user=faqanswer.user, feedback=appraisal)
                    result_dict["data"]["approve"] = faqanswer.approve
                    result_dict["data"]["oppose"] = faqanswer.oppose
            else:
                result_dict["err"] = 1
                result_dict["msg"] = "缺少问题回复ID或评价类型"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class AcceptFaqAnswer(View):
    """采纳这个答案"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "成功采纳这个答案"}
        try:
            param_dict = json.loads(request.body)
            custom_user_id = str_to_int(request.GET.get('custom_user_id', 0))  # 用户ID
            faq_id = str_to_int(param_dict.get('faq_id', 0))  # 必填，问题ID
            faq_answer_id = str_to_int(param_dict.get('faq_answer_id', 0))  # 必填，问题回复ID

            faqs = Faq.objects.filter(id=faq_id)
            if not faqs.exists():
                result_dict["err"] = 1
                result_dict["msg"] = "问题不存！"
                return

            # 判断用户是否是提问者
            if not faqs.filter(user__id=custom_user_id):
                result_dict["err"] = 1
                result_dict["msg"] = "不是提问者，不能采纳这个答案！"
                return

            if FaqAnswer.objects.filter(faq__id=faq_id, optimal=True).exists():
                result_dict["err"] = 1
                result_dict["msg"] = "问题已经存在最佳答案！"
                return

            if faq_answer_id:
                faqanswers = FaqAnswer.objects.filter(id=faq_answer_id)
                if faqanswers.exists() and faqs.exists():
                    faqanswer = faqanswers.first()
                    faq = faqs.first()
                    reward = int(faq.reward)

                    # 回答是否对应问题
                    if faqanswer.faq.id != faq_id:
                        result_dict["err"] = 1
                        result_dict["msg"] = "回复不对应提问！"
                        return

                    customuser = CustomUser.objects.filter(id=custom_user_id, integral__gte=reward)
                    if not customuser.exists():
                        result_dict["err"] = 1
                        result_dict["msg"] = "积分不足！"
                        return

                    # 提问用户扣除悬赏积分
                    customuser.update(integral=F('integral') - reward)

                    # 回复者增加悬赏积分
                    CustomUser.objects.filter(id=faqanswer.user.id).update(integral=F('integral') + reward)

                    # 回复修改为最佳答案
                    faqanswers.update(optimal=True)

                    # 问题修改为已解决
                    faqs.update(status="1")

            else:
                result_dict["err"] = 1
                result_dict["msg"] = "缺少问题回复ID"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class AddFaqAnswer(View):
    """回答提问"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 1, "msg": ""}
        try:
            # 回答参数
            param_dict = json.loads(request.body)
            faq_id = str_to_int(param_dict.get('faq_id', 0))  # 必填，问题ID
            custom_user_id = str_to_int(param_dict.get('custom_user_id', 0))  # 必填，回答用户ID
            answer = param_dict.get('answer', "")  # 回答内容

            required_dict = {"问题ID": faq_id, "回答用户ID": custom_user_id, "回答内容": answer}
            required_param = 1
            for param_name, param_value in required_dict.items():
                if not param_value:
                    result_dict["err"] = 1
                    result_dict["msg"] = "".join(["缺少 ", param_name])
                    required_param = 0
                    break

            # 回答参数全部合法
            if required_param:
                faqs = Faq.objects.filter(id=faq_id)
                customusers = CustomUser.objects.filter(id=custom_user_id)
                if faqs.exists() and customusers.exists():
                    create_dict = {
                        "faq": faqs.first(),
                        "user": customusers.first(),
                        "answer": answer,
                    }
                    faqanswer_obj = FaqAnswer.objects.create(**create_dict)
                    if not faqanswer_obj:
                        result_dict["msg"] = "回答失败"
                    else:
                        result_dict["err"] = 0
                        result_dict["msg"] = "成功回答"
                else:
                    result_dict["msg"] = "没有对应问题或回答用户信息"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
