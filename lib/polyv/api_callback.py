#!/usr/bin/env python
# !encoding:utf-8
import json
import traceback

from django.http import HttpResponse
from django.views.generic import View
from lib.polyv.video_api import get_video_msg

from applications.tracks_learning.models import Video
from lib.util import time_to_second


class PolyvCallBack(View):
    """保利威视回调接口"""

    def get(self, request, *args, **kwargs):
        result_dict = dict()
        try:
            request_type = request.GET.get("type")  # 回调通知类型
            vid = request.GET.get("vid")  # 视频在保利威视唯一ID
            request_format = request.GET.get("format")  # 编码后的视频格式
            state = request.GET.get("state")  # 自定义参数
            # sign 系统签名，
            # sign是由系统用"upload"这个字符串和vid、secretkey这两个参数的值按顺序组成的字符串做MD5计算得到
            # （如，vid的值为e2e84a738302f20a4f6eb202976f5c63_e，secretkey的值为7UagtQOq2A,将字符串uploade2e84a738302f20a4f6eb202976f5c63_e7UagtQOq2A进行MD5计算，得到b245e3e65aa45b60dc02337b5cd914a7)
            sign = request.GET.get("sign")  # 系统签名
            df = request.GET.get("df")  # 视频清淅度版本，1为流畅、2为高清、3为超清

            print "type==", request_type
            print "vid==", vid
            print "format==", request_format
            print "state==", state
            print "sign==", sign
            print "df==", df
            if request_type == "upload" and state:  # 已上传
                duration = 0
                video_result = get_video_msg(vid)
                data_list = video_result.get("data", [])
                if data_list:
                    video_data_dict = data_list[0]
                    duration_str = video_data_dict.get("duration", "0:0:0")
                    duration = time_to_second(duration_str)

                update_dict = {
                    "data": json.dumps(video_result, ensure_ascii=False),
                    "vid": vid,
                    "duration": duration
                }
                Video.objects.filter(id=int(state)).update(**update_dict)
            elif request_type == "invalidVideo":  # 不合规格视频（当上传的视频的信息无法被系统分析时，判断为不合规格视频）
                pass
            elif request_type == "encode":  # 已编码
                pass
            elif request_type == "encode_failed":  # 处理失败
                pass
            elif request_type == "pass":  # 通过
                pass
            elif request_type == "nopass":  # 通过
                pass
            elif request_type == "del":  # 删除
                pass
        except:
            traceback.print_exc()
        return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
