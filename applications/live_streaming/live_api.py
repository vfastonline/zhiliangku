#!/usr/bin/env python
#!encoding:utf-8
import time
import hashlib
import requests
import json

timestamp = (int(round(time.time() * 1000)))
appid = 'eu1e5pr3zy'
userid = 'a582a3b650'
appsecret = '55f9bfe376594829958203ff7ab3b99c'


def create_live(name, courseid='zhiliangku', autoplay=1,playercolor='#00ffff',channelpasswd='111111'):
    '''
    创建直播频道
    @param  name                直播频道名称
    @param  courseid            课程名称
    @param  channelpasswd       直播频道密码
    @param  autoplay            自动播放
    @param  playercolor         界面颜色
    return 
        {u'status': u'success', u'message': u'', u'code': 200, u'data': {u'coverHref': u'', u'waitHref': u'', u'warmUpFlv': u'', u'stream': u'a582a3b65020171128131439507', u'passwdRestrict': False, u'channelId': 141520, u'advertType': u'NONE', u'playerColor': u'#00ffff', u'logoHref': u'', u'isOnlyAudio': u'N', u'description': u'', u'm3u8Url2': u'', u'm3u8Url3': u'', u'm3u8Url1': u'', u'advertFlvUrl': u'', u'logoImage': u'', u'advertHref': u'', u'advertImage': u'', u'advertFlvVid': u'', u'autoPlay': True, u'waitImage': u'', u'cutoffImage': u'', u'userId': u'a582a3b650', u'logoPosition': u'', u'advertWidth': None, u'advertDuration': None, u'logoOpacity': 1.0, u'm3u8Url': u'http://pullh.videocc.net/recordfe/a582a3b65020171128131439507/playlist.m3u8?wsSecret=5fa6b8e64ca5a4ef5398c1271971569c&wsTime=1511846079', u'publisher': None, u'isLowLatency': u'N', u'name': u'adsfs', u'url': u'rtmp://push2.videocc.net/recordfe/a582a3b65020171128131439507', u'coverImage': u'', u'currentTimeMillis': 1511846079521, u'cutoffHref': u'', u'channelLogoImage': None, u'advertHeight': None, u'passwdEncrypted': u''}}
        {u'status': u'error', u'message': u'invalid signature.', u'code': 403, u'data': u''}
        
    '''
    if name is None:
        return 'param name is required!'
    sign = '%sappId%sautoPlay%schannelPasswd%scourseId%sname%splayerColor%stimestamp%suserId%s%s' % (
            appsecret,appid,autoplay,channelpasswd,courseid,name,playercolor,timestamp,userid,appsecret)
    sign = hashlib.md5(sign).hexdigest().upper()
    data = {
            'appId':appid,
            'autoPlay':autoplay,
            'name':name,
            'courseId':courseid,
            'playerColor':playercolor,
            'timestamp':timestamp,
            'userId': userid,
            'channelPasswd':channelpasswd,
            'sign':sign
            }
    url = "http://api.polyv.net/live/v2/channels"
    r = requests.post(url, data)
    ret = json.loads(r.text)
    return ret


def delete_live(channelID):
    '''
    删除直播频道
    @param channelID            频道ID
    return
        {u'status': u'success', u'result': True}
        {u'status': u'failure', u'result': u'failed operation.'}
    '''
    sign = '%sappId%stimestamp%suserId%s%s'  %  (appsecret, appid,timestamp,userid,appsecret)
    sign = hashlib.md5(sign).hexdigest().upper()
    url = "http://api.live.polyv.net/v1/channels/%s?appId=%s&timestamp=%s&userId=%s&sign=%s" % (channelID,appid,timestamp,userid,sign)
    r=requests.delete(url)
    ret = json.loads(r.text)
    return ret


def setlivepasswd(channelId,passwd):
    '''
    修改直播频道播放密码
    @param channelID   频道ID
    @param passwd      新设置的频道密码
    return 
        {u'status': u'success', u'message': u'', u'code': 200, u'data': True}
        {u'status': u'error', u'message': u'invalid signature.', u'code': 403, u'data': u''}
        
    '''
    sign = '%sappId%spasswd%stimestamp%s%s' % (appsecret,appid,passwd,timestamp,appsecret)
    sign = hashlib.md5(sign).hexdigest().upper()
    url = "http://api.live.polyv.net/v2/channels/%s/passwdSetting?appId=%s&timestamp=%s&passwd=%s&sign=%s" % (userid,appid,timestamp,passwd,sign)
    r = requests.post(url)
    ret = json.loads(r.text)
    return ret


def getstatus_live(channelIds):
    '''
    批量获取直播状态接口
    @params channelIds 用逗号隔开的频道ID，如：10000,100001 最多20个
    return 
        {u'status': u'success', u'message': u'', u'code': 200, u'data': [{u'status': u'end', u'channelId': 141514}, {u'status': u'end', u'channelId': 141520}]}
        {u'status': u'error', u'message': u'appId is required.', u'code': 400, u'data': u''}
    '''
    sign = appsecret+"appId"+appid+"channelIds"+ channelIds + "timestamp" + str(timestamp) + appsecret
    sign = hashlib.md5(sign).hexdigest().upper()
    data = {
            'appId': appid,
            'timestamp': timestamp,
            'channelIds': channelIds,
            'sign': sign
            }
    url ="http://api.live.polyv.net/v2/channels/live-status";
    r = requests.post(url, data)
    ret = json.loads(r.text)
    return ret

