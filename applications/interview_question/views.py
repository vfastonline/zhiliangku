#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.interview_question.models import EnterpriseInfo


class IndexEnterpriseInfoList(View):
    """首页-企业信息"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": []}
        try:
            enterprise_info_objs = EnterpriseInfo.objects.all()[:4]
            result_dict["data"] = [
                {
                    "id": one.id,
                    "company": one.company,
                    "position": one.position,
                    "amount": one.amount,
                    "lowest_monthly_salary": one.lowest_monthly_salary,
                    "highest_monthly_salary": one.highest_monthly_salary,
                    "question_img": one.question_img.url,
                }
                for one in enterprise_info_objs
            ]
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
