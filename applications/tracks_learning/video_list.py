#!encoding:utf-8
import hashlib
import json
import logging
import time
import traceback

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from applications.tracks_learning.models import *
from conf.conf_core import *
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int
from applications.record.models import WatchRecord


class UploadVideoPolyvParam(View):
    """上传视频到保利威视接口参数，3分钟获取一次"""

    def get(self, request, *args, **kwargs):
        ts = str(int(round(time.time() * 1000)))
        result_dict = dict()

        hash_str = hashlib.new("md5", "".join([ts, WRITETOKEN])).hexdigest()
        sign = hashlib.new("md5", "".join([SECRETKEY, ts])).hexdigest()
        result_dict["writeToken"] = WRITETOKEN
        result_dict["userid"] = USERID
        result_dict["ts"] = ts
        result_dict["hash"] = hash_str
        result_dict["sign"] = sign
        result_dict["readToken"] = READTOKEN
        return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


class VideoList(View):
    """视频列表"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": list()}
        try:
            # 获取查询参数
            section_id = str_to_int(request.GET.get('section_id', 0))
            custom_user_id = str_to_int(request.GET.get('custom_user_id', 0))  # 用户ID

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
                    video_dict["is_learned"] = 0
                    video_dict["vid"] = one_video.vid if one_video.vid else ""
                    duration_str = ""
                    if one_video.duration:
                        m, s = divmod(one_video.duration, 60)
                        duration_str = "%d分%d秒" % (m, s)

                    video_dict["duration"] = duration_str

                    # 补全直播信息
                    if one_video.live:
                        video_dict["live_id"] = one_video.live.id
                        video_dict["live_channelId"] = one_video.live.channelId
                        video_dict["vid"] = one_video.live.channelId
                        video_dict["live_status"] = one_video.live.status
                        video_dict["live_status_name"] = one_video.live.get_status_display()
                        video_dict["live_start_time"] = one_video.live_start_time.strftime("%Y-%m-%d %H:%M") \
                            if one_video.live_start_time else ""
                        video_dict["live_end_time"] = one_video.live_end_time.strftime("%H:%M") \
                            if one_video.live_end_time else ""
                    # 补全是否学习状态
                    if one_video.type in ["1", "2"]:  # 点播、直播回放
                        watchrecords = WatchRecord.objects.filter(video=one_video, user_id=custom_user_id)
                        if watchrecords.exists():
                            video_dict["is_learned"] = 99
                        if watchrecords.filter(status=1).exists():
                            video_dict["is_learned"] = 1

                    if one_video.type == "4":  # 习题
                        pass

                    data_list.append(video_dict)
            result_dict["data"] = data_list
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class VideoDetail(View):
    """视频详情页面"""

    def get(self, request, *args, **kwargs):
        template_name = "tracks/video/detail/index.html"
        return render(request, template_name, {})


@class_view_decorator(user_login_required)
class LiveDetail(View):
    """直播详情页面"""

    def get(self, request, *args, **kwargs):
        template_name = "tracks/live/detail/index.html"
        return render(request, template_name, {})


@class_view_decorator(user_login_required)
class VideoDetailInfo(View):
    """视频详情信息"""

    def get(self, request, *args, **kwargs):
        result_dict = {"err": 0, "msg": "success", "data": {}}
        try:
            # 获取查询参数
            video_id = str_to_int(request.GET.get('video_id', 0))

            video_dict = dict()
            if video_id:
                videos = Video.objects.filter(id=video_id)
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
                    if video_obj.type == "3":
                        if video_obj.live:
                            video_dict["live_channelId"] = video_obj.live.channelId
                            video_dict["live_id"] = video_obj.live.id
                            video_dict["live_status"] = video_obj.live.status
                            video_dict["live_status_name"] = video_obj.live.get_status_display()
                            video_dict["live_start_time"] = video_obj.live_start_time.strftime("%Y-%m-%d %H:%M") \
                                if video_obj.live_start_time else ""
                            video_dict["live_end_time"] = video_obj.live_end_time.strftime("%H:%M") \
                                if video_obj.live_end_time else ""
                    # 点播信息
                    if video_obj.type in ["1", "2"]:
                        video_dict["vid"] = video_obj.vid
                        # video_dict["video_data"] = dict()
                        # video_data_dict = json.loads(video_obj.data)
                        # data_code = video_data_dict.get("code")
                        # data_data_list = video_data_dict.get("data", [])
                        # if data_code == 200:
                        #     if data_data_list:
                        #         video_dict["video_data"] = data_data_list[0]
                        # else:
                        #     # 再次查询一下视频信息
                        #     video_msg_dict = get_video_msg(video_obj.vid)
                        #     video_msg_code = video_msg_dict.get("code")
                        #     video_msg_data_list = video_msg_dict.get("data", [])
                        #     if video_msg_code == 200:
                        #         if video_msg_data_list:
                        #             video_dict["video_data"] = video_msg_data_list[0]
            result_dict["data"] = video_dict
        except:
            traceback.print_exc()
            logging.getLogger().error(traceback.format_exc())
            result_dict["err"] = 1
            result_dict["msg"] = traceback.format_exc()
        finally:
            return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
