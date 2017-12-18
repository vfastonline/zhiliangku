#!/usr/bin/env python
# !encoding:utf-8
from django.views.generic import View
from django.http import HttpResponse
import json
import traceback


class PolyvCallBack(View):
    def get(self, request, *args, **kwargs):
        result_dict = dict()
        try:
            request_type = request.GET.get("type")  # 回调通知类型
            vid = request.GET.get("vid")  # 视频在保利威视唯一ID
            request_format = request.GET.get("format")  #
            state = request.GET.get("state")  #
            # sign 系统签名，
            # sign是由系统用"upload"这个字符串和vid、secretkey这两个参数的值按顺序组成的字符串做MD5计算得到
            # （如，vid的值为e2e84a738302f20a4f6eb202976f5c63_e，secretkey的值为7UagtQOq2A,将字符串uploade2e84a738302f20a4f6eb202976f5c63_e7UagtQOq2A进行MD5计算，得到b245e3e65aa45b60dc02337b5cd914a7)
            sign = request.GET.get("sign")  #
            df = request.GET.get("df")  #

            print "type==", request_type
            print "vid==", vid
            print "format==", request_format
            print "state==", state
            print "sign==", sign
            print "df==", df
            if request_type == "upload":  # 已上传
                pass
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
