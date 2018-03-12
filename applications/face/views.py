#!encoding:utf-8

from django.http import HttpResponse

from applications.custom_user.models import *
from applications.face.api import *
from applications.face.models import Watchface
from lib.util import dictfetchall


def face(request):
    """记录用户观看视频时表情状态"""
    try:
        if request.method == "POST":
            userid = 1
            joy = round(float(request.POST.get('joy')[0]), 3)
            engagement = round(float(request.POST.get('engagement')[0]), 3)
            sadness = round(float(request.POST.get('sadness')[0]), 3)
            anger = round(float(request.POST.get('anger')[0]), 3)
            surprise = round(float(request.POST.get('surprise')[0]), 3)
            fear = round(float(request.POST.get('fear')[0]), 3)
            valence = round(float(request.POST.get('valence')[0]), 3)
            contempt = round(float(request.POST.get('contempt')[0]), 3)
            disgust = round(float(request.POST.get('disgust')[0]), 3)
            vtime = str(request.POST.get('vtime', 0))
            vtime = int(vtime.split('.')[0])
            if not vtime:
                Watchface.objects.all().delete()
            logging.getLogger().info('%s %s  %s  %s %s %s' % (engagement, surprise, valence, contempt, disgust, vtime))

            Watchface.objects.create(userid=userid, joy=joy, engagement=engagement, sadness=sadness, anger=anger,
                                     surprise=surprise, fear=fear, valence=valence, contempt=contempt, vtime=vtime,
                                     disgust=disgust)
        return HttpResponse(json.dumps({'code': 0}))
    except:
        traceback.print_exc()
        logging.getLogger().error(traceback.format_exc())
        return HttpResponse(json.dumps({'code': 128}, ensure_ascii=False))


def getface(request):
    """获取面部信息
    :param request:
    :return:
    """
    try:
        sql = "select *, count(distinct vtime) as tmp from Watchface group by vtime;"
        result = dictfetchall(sql)
        joy, surprise, valence, engagement, sadness, disgust, anger, fear = [], [], [], [], [], [], [], []
        vtime = []
        for item in result:
            joy.append(item['joy'])
            surprise.append(item['surprise'])
            valence.append(item['valence'])
            engagement.append(item['engagement'])
            sadness.append(item['sadness'])
            disgust.append(item['disgust'])
            anger.append(item['anger'])
            fear.append(item['fear'])
            vtime.append(item['vtime'])
        return HttpResponse(
            json.dumps({'code': 0, 'joy': joy, 'surprise': surprise, 'valence': valence, 'engagement': engagement,
                        'sadness': sadness, 'disgust': disgust, 'anger': anger, 'fear': fear, 'vtime': vtime}))
    except:
        logging.getLogger().error(traceback.format_exc())
        return HttpResponse(json.dumps({'code': 128}, ensure_ascii=False))


def user_image(request):
    """
    :param request:
    :return:
    """
    try:
        if request.method == "POST":
            image = request.POST.get('image')
            ret = Detect(image)
            if ret:
                return HttpResponse(json.dumps({'code': 0, 'msg': 'ok'}))
            else:
                return HttpResponse(json.dumps({'code': 1, 'msg': 'disapper'}))
    except:
        logging.getLogger().error(traceback.format_exc())
        return HttpResponse(json.dumps({'code': 128}, ensure_ascii=False))
