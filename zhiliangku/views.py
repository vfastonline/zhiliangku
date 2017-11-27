from django.http import HttpResponse
from django.shortcuts import render

import logging

def index(request):
    logging.getLogger().info('hello')
#    return HttpResponse('ok')
    return render(request, 'index.html')
