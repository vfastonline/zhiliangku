#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.community.models import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int


@class_view_decorator(user_login_required)
class AddFaqAnswerReply(View):
    """回复问题回答"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 1, "msg": ""}
        try:
            # 回答参数
            param_dict = json.loads(request.body)
            faq_answer_id = str_to_int(param_dict.get('faq_answer_id', 0))  # 必填，问题回答ID
            custom_user_id = str_to_int(param_dict.get('custom_user_id', 0))  # 必填，回复用户ID
            reply = param_dict.get('reply', "")  # 回复内容

            required_dict = {"问题回答ID": faq_answer_id, "回复用户ID": custom_user_id, "回复内容": reply}
            required_param = 1
            for param_name, param_value in required_dict.items():
                if not param_value:
                    result_dict["err"] = 1
                    result_dict["msg"] = "".join(["缺少 ", param_name])
                    required_param = 0
                    break

            # 回答参数全部合法
            if required_param:
                faqanswers = FaqAnswer.objects.filter(id=faq_answer_id)
                customusers = CustomUser.objects.filter(id=custom_user_id)
                if faqanswers.exists() and customusers.exists():
                    create_dict = {
                        "faqanswer": faqanswers.first(),
                        "user": customusers.first(),
                        "reply": reply,
                    }
                    faqanswerreply_obj = FaqAnswerReply.objects.create(**create_dict)
                    if not faqanswerreply_obj:
                        result_dict["msg"] = "回复失败"
                    else:
                        result_dict["err"] = 0
                        result_dict["msg"] = "成功回复"
                else:
                    result_dict["msg"] = "没有对应问题回答或回复用户信息"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
