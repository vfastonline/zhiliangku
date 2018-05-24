#!encoding:utf-8
import json
import logging
import os
import re
import traceback
from django.views.generic import View

from django.http import HttpResponse
from django.shortcuts import render

import settings
from lib.uploader import Uploader


def index(request):
	logging.getLogger().info('hello')
	return render(request, 'index.html')


# 链接指向的网页不存在
def redirect_404_error(request):
	return render(request, '404.html')


# 服务器内部错误
def redirect_500_error(request):
	return render(request, '500.html')


# 无权限请求
def redirect_403_error(request):
	return render(request, '403.html')


# 请求出错
def redirect_400_error(request):
	return render(request, '400.html')


def upload(request):
	"""UEditor文件上传接口
	config 配置文件
	result 返回结果
	"""
	result = {}
	action = request.GET.get('action')

	# 解析JSON格式的配置文件
	with open(os.path.join(settings.BASE_DIR, 'conf', 'config.json')) as fp:
		try:
			# 删除 `/**/` 之间的注释
			CONFIG = json.loads(re.sub(r'\/\*.*\*\/', '', fp.read()))
		except:
			CONFIG = {}

	# #print CONFIG
	# #print action
	if action == 'config':
		# 初始化时，返回配置文件给客户端
		result = CONFIG

	elif action in ('uploadimage', 'uploadfile', 'uploadvideo'):
		# 图片、文件、视频上传
		if action == 'uploadimage':
			fieldName = CONFIG.get('imageFieldName')
			config = {
				"pathFormat": CONFIG['imagePathFormat'],
				"maxSize": CONFIG['imageMaxSize'],
				"allowFiles": CONFIG['imageAllowFiles']
			}

		elif action == 'uploadvideo':
			fieldName = CONFIG.get('videoFieldName')
			config = {
				"pathFormat": CONFIG['videoPathFormat'],
				"maxSize": CONFIG['videoMaxSize'],
				"allowFiles": CONFIG['videoAllowFiles']
			}

		else:
			fieldName = CONFIG.get('fileFieldName')
			config = {
				"pathFormat": CONFIG['filePathFormat'],
				"maxSize": CONFIG['fileMaxSize'],
				"allowFiles": CONFIG['fileAllowFiles']
			}

		# #print fieldName, request.FILES.get('upfile')
		if fieldName in request.FILES:
			field = request.FILES[fieldName]
			# #print field.name, field.size,
			uploader = Uploader(field, config, os.path.join(settings.BASE_DIR))
			result = uploader.getFileInfo()
		else:
			result['state'] = 'upload interface error'

	# elif action in ('uploadscrawl'):
	#     # 涂鸦上传
	#     fieldName = CONFIG.get('scrawlFieldName')
	#     config = {
	#         "pathFormat": CONFIG.get('scrawlPathFormat'),
	#         "maxSize": CONFIG.get('scrawlMaxSize'),
	#         "allowFiles": CONFIG.get('scrawlAllowFiles'),
	#         "oriName": "scrawl.png"
	#     }
	#     if fieldName in request.form:
	#         field = request.form[fieldName]
	#         uploader = Uploader(field, config, app.static_folder, 'base64')
	#         result = uploader.getFileInfo()
	#     else:
	#         result['state'] = '上传接口出错'
	#
	# elif action in ('catchimage'):
	#     config = {
	#         "pathFormat": CONFIG['catcherPathFormat'],
	#         "maxSize": CONFIG['catcherMaxSize'],
	#         "allowFiles": CONFIG['catcherAllowFiles'],
	#         "oriName": "remote.png"
	#     }
	#     fieldName = CONFIG['catcherFieldName']
	#     if fieldName in request.form:
	#         # 这里比较奇怪，远程抓图提交的表单名称不是这个
	#         source = []
	#     elif '%s[]' % fieldName in request.form:
	#         # 而是这个
	#         source = request.form.getlist('%s[]' % fieldName)
	#     _list = []
	#     for imgurl in source:
	#         uploader = Uploader(imgurl, config, app.static_folder, 'remote')
	#         info = uploader.getFileInfo()
	#         _list.append({
	#             'state': info['state'],
	#             'url': info['url'],
	#             'original': info['original'],
	#             'source': imgurl,
	#         })
	#     result['state'] = 'SUCCESS' if len(_list) > 0 else 'ERROR'
	#     result['list'] = _list

	else:
		result['state'] = 'request URL error'
	result = json.dumps(result)
	if 'callback' in request.GET:
		callback = request.args.get('callback')
		if re.match(r'^[\w_]+$', callback):
			result = '%s(%s)' % (callback, result)
			mimetype = 'application/javascript'
		else:
			result = json.dumps({'state': 'callback args is not right'}, ensure_ascii=False)
	# #print result
	# res.mimetype = mimetype
	# res.headers['Access-Control-Allow-Origin'] = '*'
	# res.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,X_Requested_With'
	return HttpResponse(result)
