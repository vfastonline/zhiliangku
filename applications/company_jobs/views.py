#!encoding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from applications.company_jobs.models import Company_jobs
import traceback
import json
import os
from django.conf import settings


# Create your views here.
def company_add(request):
    try:
        if request.method == "POST":
            data = request.POST
            token = data.get('token')
            if token != 'xuyang':
                return HttpResponse(json.dumps({'code': 1, 'msg': 'error token'}, ensure_ascii=False))
            tmp = dict([(k, v) for k, v in data.iteritems()])
            logoimg = request.FILES['logoimg']
            if logoimg.size > 102400:
                return HttpResponse(json.dumps({'code': 1, 'msg': 'picture size limit 100kb'}, ensure_ascii=False))
            logoimg_name = logoimg.name
            destination = os.path.join(settings.MEDIA_ROOT, 'companylogo')
            if not os.path.isdir(destination):
                os.system('mkdir -p %s' % destination)
            f = open(os.path.join(destination, logoimg_name), 'wb')
            for chunk in logoimg.chunks():
                f.write(chunk)
            f.close()
            tmp['logo'] = '/media/companylogo/%s' % logoimg_name
            tmp.pop('token')
            Company_jobs.objects.create(**tmp)
        else:
            return HttpResponse('get')
    except:
        return HttpResponse(traceback.format_exc())
    finally:
        return HttpResponse(json.dumps({'code': 0, 'msg': 'request successfully'}))
