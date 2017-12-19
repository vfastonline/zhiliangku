#!/usr/bin/env python
# !encoding:utf-8
import hashlib
import logging
import time
import traceback

import requests

from conf.conf_core import *


def get_video_msg(vid=''):
    """获取单个视频信息
    :param vid: 保利威视视频唯一ID
    :return:
    """
    result = dict()
    timestamp = (int(round(time.time() * 1000)))
    try:
        if vid:
            sign = 'ptime={ptime}&vid={vid}{secretkey}'.format(ptime=timestamp, vid=vid, secretkey=SECRETKEY)
            sign = hashlib.sha1(sign).hexdigest().upper()
            data = {
                'vid': vid,
                'userid': USERID,
                'ptime': timestamp,
                'sign': sign,
            }
            get_video_msg_url = GET_VIDEO_MSG.format(userid=USERID)
            r = requests.post(get_video_msg_url, data)
            result = r.json()
    except:
        traceback.print_exc()
        logging.getLogger().error(traceback.format_exc())
    finally:
        return result


"""获取单个视频信息接口返回值
{
    code: 400,
    status: "error",
    message: "ptime is too old.",
    data: ""
}
{
    u'status': u'success',
    u'message': u'success',
    u'code': 200,
    u'data': [
        {
            u'vid': u'a582a3b65023ed66fc5a863cba9a985d_a',
            u'default_video': u'http: //plvod01.videocc.net/a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_2.flv',
            u'hls': [
                u'http: //hls.videocc.net/a582a3b650/a/a582a3b65023ed66fc5a863cba9a985d_1.m3u8',
                u'http: //hls.videocc.net/a582a3b650/a/a582a3b65023ed66fc5a863cba9a985d_2.m3u8',
                u'http: //hls.videocc.net/a582a3b650/a/a582a3b65023ed66fc5a863cba9a985d_3.m3u8'
            ],
            u'duration': u'00: 00: 16',
            u'mp4': u'http: //mpv.videocc.net/a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_1.mp4',
            u'tag': u'',
            u'images': [
                u'a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_0.jpg',
                u'a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_1.jpg',
                u'a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_2.jpg',
                u'a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_3.jpg',
                u'a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_4.jpg',
                u'a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_5.jpg'
            ],
            u'mp4_1': u'http: //mpv.videocc.net/a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_1.mp4',
            u'images_b': [
                u'a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_0_b.jpg',
                u'a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_1_b.jpg',
                u'a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_2_b.jpg',
                u'a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_3_b.jpg',
                u'a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_4_b.jpg',
                u'a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_5_b.jpg'
            ],
            u'ptime': u'2017-12-1913: 16: 38',
            u'title': u'IMG_0073',
            u'cataid': u'1',
            u'mp4_3': u'http: //mpv.videocc.net/a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_3.mp4',
            u'mp4_2': u'http: //mpv.videocc.net/a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_2.mp4',
            u'filesize': [
                0,
                0,
                0
            ],
            u'original_definition': u'480x480',
            u'status': u'20',
            u'df': 3,
            u'sourcefile': u'',
            u'playerheight': u'600',
            u'imageUrls': [
                u'http: //img.videocc.net/uimage/a/a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_0.jpg',
                u'http: //img.videocc.net/uimage/a/a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_1.jpg',
                u'http: //img.videocc.net/uimage/a/a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_2.jpg',
                u'http: //img.videocc.net/uimage/a/a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_3.jpg',
                u'http: //img.videocc.net/uimage/a/a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_4.jpg',
                u'http: //img.videocc.net/uimage/a/a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_5.jpg'
            ],
            u'first_image': u'http: //img.videocc.net/uimage/a/a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_0.jpg',
            u'playerwidth': u'600',
            u'times': u'0',
            u'flv1': u'http: //plvod01.videocc.net/a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_1.flv',
            u'flv2': u'http: //plvod01.videocc.net/a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_2.flv',
            u'seed': 0,
            u'context': u'',
            u'flv3': u'http: //plvod01.videocc.net/a582a3b650/d/a582a3b65023ed66fc5a863cba9a985d_3.flv',
            u'source_filesize': 3468442,
            u'md5checksum': u'cbd58c04a3ec8557e4c72bb901c6a255',
            u'swf_link': u'http: //player.polyv.net/videos/a582a3b65023ed66fc5a863cba9a985d_a.swf'
        }
    ]
}

字段	说明
error	错误提示
swf_link	返回flash连接
tag	视频标签
mp4	MP4源文件
playerwidth	视频宽度
title	标题
duration	时长
filesize	编码后各个清晰度视频的文件大小，类型为array
first_image	视频首图
times	播放次数
context	视频描述
original_definition	最佳分辨率
images	视频截图
playerheight	视频高度
ptime	视频上传日期
context	内容
ptime	上传时间
vid	视频id
previewVid	预览视频id
cataid	分类id， 如1为根目录
default_video	用户默认播放视频
df	视频码率数
flv1	流畅码率flv格式视频地址
flv2	高清码率flv格式视频地址
flv3	超清码率flv格式视频地址
mp4_1	流畅码率mp4格式视频地址
mp4_2	高清码率mp4格式视频地址
mp4_3	超清码率mp4格式视频地址
hlsIndex	索引文件，记录每个清晰度的m3u8的链接
hls_1	流畅清晰度的m3u8
hls_2	高清清晰度的m3u8
hls_3	超清清晰度的m3u8
images_b	视频截图大图地址
seed	加密视频为1，非加密为0
status	视频状态error	错误提示
swf_link	返回flash连接
tag	视频标签
mp4	MP4源文件
playerwidth	视频宽度
title	标题
duration	时长
filesize	编码后各个清晰度视频的文件大小，类型为array
first_image	视频首图
times	播放次数
context	视频描述
original_definition	最佳分辨率
images	视频截图
playerheight	视频高度
ptime	视频上传日期
context	内容
ptime	上传时间
vid	视频id
previewVid	预览视频id
cataid	分类id， 如1为根目录
default_video	用户默认播放视频
df	视频码率数
flv1	流畅码率flv格式视频地址
flv2	高清码率flv格式视频地址
flv3	超清码率flv格式视频地址
mp4_1	流畅码率mp4格式视频地址
mp4_2	高清码率mp4格式视频地址
mp4_3	超清码率mp4格式视频地址
hlsIndex	索引文件，记录每个清晰度的m3u8的链接
hls_1	流畅清晰度的m3u8
hls_2	高清清晰度的m3u8
hls_3	超清清晰度的m3u8
images_b	视频截图大图地址
seed	加密视频为1，非加密为0
status	视频状态


视频状态码	含义
60/61	已发布
10	等待编码
20	正在编码
50	等待审核
51	审核不通过
-1	已删除
"""
