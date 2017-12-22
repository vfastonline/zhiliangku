#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.community.models import *
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


# @class_view_decorator(user_login_required)
class AddFaq(View):
    """提问"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 1, "msg": ""}
        try:
            # 提问参数
            param_dict = json.loads(request.body)
            video_id = int(param_dict.get('video_id', 0))  # 必填，视频ID
            custom_user_id = int(param_dict.get('custom_user_id'))  # 必填，标题
            title = param_dict.get('title')  # 必填，标题
            description = param_dict.get('description')  # 必填，标题
            path = param_dict.get('path')  # 问题方向
            reward = param_dict.get('reward')  # 悬赏

            required_dict = {"视频ID": video_id, "用户ID": custom_user_id, "问题标题": title, "问题描述": description}
            required_param = 1
            for param_name, param_value in required_dict.items():
                if not param_value:
                    result_dict["err"] = 1
                    result_dict["msg"] = "".join(["缺少 ", param_name])
                    required_param = 0
                    break

            # 提问参数全部合法
            if required_param:
                videos = Video.objects.filter(id=video_id)
                customusers = CustomUser.objects.filter(id=custom_user_id)

                if videos.exists() and customusers.exists():
                    create_dict = {
                        "video": videos.first(),
                        "user": customusers.first(),
                        "title": title,
                        "description": description,
                        "path": path,
                        "reward": reward,
                    }
                    faq_obj = Faq.objects.create(**create_dict)
                    if not faq_obj:
                        result_dict["msg"] = "提问失败"
                    else:
                        result_dict["err"] = 0
                        result_dict["msg"] = "成功提问"
                else:
                    result_dict["msg"] = "没有对应视频或提问者信息"
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


# @class_view_decorator(user_login_required)
class AddAnswerFaq(View):
    """回答提问"""

    def post(self, request, *args, **kwargs):
        result_dict = {"err": 1, "msg": ""}
        try:
            # 回答参数
            param_dict = json.loads(request.body)
            faq_id = int(param_dict.get('faq_id', 0))  # 必填，问题ID
            custom_user_id = int(param_dict.get('custom_user_id', 0))  # 必填，回答用户ID
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
