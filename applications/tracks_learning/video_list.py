#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.views.generic import View

from applications.tracks_learning.models import *
from lib.permissionMixin import class_view_decorator, user_login_required


# @class_view_decorator(user_login_required)
class VideoList(View):
    """视频列表"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": list()}
        try:
            # 获取查询参数
            section_id = request.GET.get('section_id')

            data_list = list()
            if section_id:
                videos = Video.objects.filter(section__id=section_id).order_by("sequence")
                for one_video in videos:
                    video_dict = dict()
                    video_dict["id"] = one_video.id
                    video_dict["type"] = one_video.type
                    video_dict["type_name"] = one_video.get_type_display()
                    video_dict["name"] = one_video.name
                    video_dict["sequence"] = one_video.sequence
                    video_dict["desc"] = one_video.desc
                    video_dict["is_learned"] = 1
                    video_dict["duration"] = one_video.duration
                    if one_video.live:
                        video_dict["live_id"] = one_video.live.id
                        video_dict["live_channelId"] = one_video.live.channelId
                        video_dict["live_status"] = one_video.live.status
                        video_dict["live_status_name"] = one_video.live.get_status_display()
                        video_dict["live_start_time"] = one_video.live_start_time.strftime("%Y-%m-%d %H:%M") \
                            if one_video.live_start_time else ""
                        video_dict["live_end_time"] = one_video.live_end_time.strftime("%H:%M") \
                            if one_video.live_end_time else ""

                    data_list.append(video_dict)
            result_dict["data"] = data_list
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
