import logging

from django.shortcuts import render


def index(request):
    logging.getLogger().info('hello')
    return render(request, 'index.html')
