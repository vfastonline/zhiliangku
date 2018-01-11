#!/usr/bin/env python
# !encoding:utf-8
import hashlib
import logging
import time
import traceback

import requests

from conf.conf_core import *


def create_live(name, courseid='zhiliangku', autoplay=1, playercolor='#00ffff', channelpasswd='111111'):
    """创建直播频道
    :param name:频道名称
    :param courseid:课程号
    :param autoplay:是否自动播放，0/1，默认1
    :param playercolor:播放器控制栏颜色，默认：#666666
    :param channelpasswd:频道密码
    :return:{u'status': u'success', u'message': u'', u'code': 200, u'data': {u'coverHref': u'', u'waitHref': u'', u'warmUpFlv': u'', u'stream': u'a582a3b65020171128131439507', u'passwdRestrict': False, u'channelId': 141520, u'advertType': u'NONE', u'playerColor': u'#00ffff', u'logoHref': u'', u'isOnlyAudio': u'N', u'description': u'', u'm3u8Url2': u'', u'm3u8Url3': u'', u'm3u8Url1': u'', u'advertFlvUrl': u'', u'logoImage': u'', u'advertHref': u'', u'advertImage': u'', u'advertFlvVid': u'', u'autoPlay': True, u'waitImage': u'', u'cutoffImage': u'', u'userId': u'a582a3b650', u'logoPosition': u'', u'advertWidth': None, u'advertDuration': None, u'logoOpacity': 1.0, u'm3u8Url': u'http://pullh.videocc.net/recordfe/a582a3b65020171128131439507/playlist.m3u8?wsSecret=5fa6b8e64ca5a4ef5398c1271971569c&wsTime=1511846079', u'publisher': None, u'isLowLatency': u'N', u'name': u'adsfs', u'url': u'rtmp://push2.videocc.net/recordfe/a582a3b65020171128131439507', u'coverImage': u'', u'currentTimeMillis': 1511846079521, u'cutoffHref': u'', u'channelLogoImage': None, u'advertHeight': None, u'passwdEncrypted': u''}}
        {u'status': u'error', u'message': u'invalid signature.', u'code': 403, u'data': u''}
    """
    result = dict()
    timestamp = (int(round(time.time() * 1000)))
    try:
        if name:
            sign = '%sappId%sautoPlay%schannelPasswd%scourseId%sname%splayerColor%stimestamp%suserId%s%s' % (
                SECRETKEY, APPID, autoplay, channelpasswd, courseid, name, playercolor, timestamp, USERID, SECRETKEY)
            sign = hashlib.md5(sign).hexdigest().upper()
            data = {
                'appId': APPID,
                'autoPlay': autoplay,
                'name': name,
                'courseId': courseid,
                'playerColor': playercolor,
                'timestamp': timestamp,
                'userId': USERID,
                'channelPasswd': channelpasswd,
                'sign': sign
            }
            r = requests.post(CREATE_LIVE, data)
            result = r.json()
    except:
        traceback.print_exc()
        logging.getLogger().error(traceback.format_exc())
    finally:
        return result


def delete_live(channelID):
    """删除直播频道
    :param channelID: 频道ID
    :return:
        {u'status': u'success', u'result': True}
        {u'status': u'failure', u'result': u'failed operation.'}
    """
    result = dict()
    try:
        timestamp = (int(round(time.time() * 1000)))
        sign = '%sappId%stimestamp%suserId%s%s' % (SECRETKEY, APPID, timestamp, USERID, SECRETKEY)
        sign = hashlib.md5(sign).hexdigest().upper()
        url = (DELETE_LIVE + "?appId={appId}&timestamp={timestamp}&userId={userId}&sign={sign}").format(
            channelId=channelID, appId=APPID, timestamp=timestamp, userId=USERID, sign=sign)
        r = requests.delete(url)
        result = r.json()
    except:
        traceback.print_exc()
        logging.getLogger().error(traceback.format_exc())
    finally:
        return result


def setlivepasswd(channelId, passwd, is_batch=False):
    """修改直播频道播放密码
    :param channelId: 频道ID
    :param passwd: 新设置的频道密码
    :param is_batch: 是否批量设置所有直播频道密码
    :return:
        {u'status': u'success', u'message': u'', u'code': 200, u'data': True}
        {u'status': u'error', u'message': u'invalid signature.', u'code': 403, u'data': u''}
    """
    result = dict()
    try:
        timestamp = (int(round(time.time() * 1000)))
        if is_batch:  # 批量频道密码
            sign = '%sappId%spasswd%stimestamp%s%s' % (SECRETKEY, APPID, passwd, timestamp, SECRETKEY)
            sign = hashlib.md5(sign).hexdigest().upper()
            url = (PASSWD_SET_LIVE + "?appId={appId}&timestamp={timestamp}&passwd={passwd}&sign={sign}").format(
                userId=USERID, appId=APPID, timestamp=timestamp, passwd=passwd, sign=sign)
        else:
            sign = '%sappId%schannelId%spasswd%stimestamp%s%s' % (
                SECRETKEY, APPID, channelId, passwd, timestamp, SECRETKEY)
            sign = hashlib.md5(sign).hexdigest().upper()
            url = (
                PASSWD_SET_LIVE + "?appId={appId}&timestamp={timestamp}&channelId={channelId}&passwd={passwd}&sign={sign}").format(
                userId=USERID, appId=APPID, timestamp=timestamp, channelId=channelId, passwd=passwd, sign=sign)
        r = requests.post(url)
        result = r.json()
    except:
        traceback.print_exc()
        logging.getLogger().error(traceback.format_exc())
    return result


def getstatus_live(channelIds):
    """批量获取直播状态接口
    :param channelIds: 用逗号隔开的频道ID，如：10000,100001 最多20个
    :return:
        {u'status': u'success', u'message': u'', u'code': 200, u'data': [{u'status': u'end', u'channelId': 141514}, {u'status': u'end', u'channelId': 141520}]}
        {u'status': u'error', u'message': u'appId is required.', u'code': 400, u'data': u''}
    """
    result = dict()
    try:
        timestamp = (int(round(time.time() * 1000)))
        sign = SECRETKEY + "appId" + APPID + "channelIds" + channelIds + "timestamp" + str(timestamp) + SECRETKEY
        sign = hashlib.md5(sign).hexdigest().upper()
        data = {
            'appId': APPID,
            'timestamp': timestamp,
            'channelIds': channelIds,
            'sign': sign
        }
        r = requests.post(GET_LIVE_STATUS_LIVE, data)
        result = r.json()
    except:
        traceback.print_exc()
        logging.getLogger().error(traceback.format_exc())
    finally:
        return result
