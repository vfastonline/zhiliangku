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
            sign = 'format=json&ptime={ptime}&vid={vid}{secretkey}'.format(ptime=timestamp,
                                                                           vid=vid,
                                                                           secretkey=SECRETKEY)
            sign = hashlib.md5(sign).hexdigest().upper()
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
        print result
        return result
