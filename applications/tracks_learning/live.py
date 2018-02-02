#!encoding:utf-8
import json
import logging
import traceback

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from applications.tracks_learning.models import *
from lib.util import str_to_int


class LiveDetail(View):
    """直播详情页面"""

    def get(self, request, *args, **kwargs):
        template_name = "tracks/live/detail/index.html"
        return render(request, template_name, {})


class LiveDetailInfo(View):
    """直播详情信息"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": {}}
        try:
            # 获取查询参数
            video_id = str_to_int(request.GET.get('video_id', 0))

            video_dict = dict()
            if video_id:
                videos = Video.objects.filter(id=video_id, type="3")
                if videos.exists():
                    video_obj = videos.first()
                    video_dict["id"] = video_obj.id
                    video_dict["course_name"] = video_obj.section.course.name
                    video_dict["section_title"] = video_obj.section.title
                    video_dict["section_desc"] = video_obj.section.desc
                    video_dict["type"] = video_obj.type
                    video_dict["type_name"] = video_obj.get_type_display()
                    video_dict["name"] = video_obj.name
                    video_dict["desc"] = video_obj.desc
                    video_dict["duration"] = video_obj.duration
                    video_dict["notes"] = video_obj.notes

                    # 直播信息
                    if video_obj.live:
                        video_dict["live_channelId"] = video_obj.live.channelId
                        video_dict["live_id"] = video_obj.live.id
                        video_dict["live_status"] = video_obj.live.status
                        video_dict["live_status_name"] = video_obj.live.get_status_display()
                        live_start_time = video_obj.live_start_time.strftime(
                            "%Y-%m-%d %H:%M") if video_obj.live_start_time else ""
                        live_end_time = video_obj.live_end_time.strftime("%H:%M") if video_obj.live_end_time else ""
                        video_dict["live_start_time"] = live_start_time
                        video_dict["live_end_time"] = live_end_time
            result_dict["data"] = video_dict
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
