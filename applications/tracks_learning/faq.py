#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.tracks_learning.models import *
from lib.permissionMixin import class_view_decorator, user_login_required


# @class_view_decorator(user_login_required)
class FaqList(View):
    """视频常见问题列表"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": list()}
        try:
            # 获取查询参数
            video_id = int(request.GET.get('video_id', 0))

            data_list = list()
            if video_id:
                faqs = Faq.objects.filter(video__id=video_id)
                if faqs.exists():
                    for faq in faqs:
                        faq_dict = dict()
                        faq_dict["id"] = faq.id
                        faq_dict["video_id"] = faq.id
                        faq_dict["video_id"] = faq.id
                        faq_dict["custom_user_id"] = faq.user.id
                        faq_dict["custom_user_nickname"] = faq.user.nickname
                        faq_dict["custom_user_avatar"] = faq.user.avatar.url
                        faq_dict["browse_number"] = faq.browse_number
                        faq_dict["create_time"] = faq.create_time.strftime("%Y-%m-%d")
                        faq_dict["faq_answer_count"] = faq.FaqAnswer.all().count()
                        if faq.reward != 0:
                            faq_dict["reward"] = faq.get_reward_display()
                        data_list.append(faq_dict)
            result_dict["data"] = data_list
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
