# encoding: utf8
import io
import base64
import hashlib
import json
import logging
import logging.handlers
import os
import random
import smtplib
import string
import time
import traceback
from datetime import timedelta, date
from email.header import Header
from email.mime.text import MIMEText

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect

import top.api

NULL_BLANK_TRUE = {
	'null': True,
	'blank': True
}


def get_validate(identifier, uid, role, fix_pwd):
	"""
	:param identifier: 标识，手机号、邮箱、用户名或第三方应用的唯一标识。
	:param uid: 用户唯一ID
	:param role: 用户角色
	:param fix_pwd: 偏移量
	:return:token
	"""
	t = int(time.time())
	validate_key = hashlib.md5('%s%s%s' % (identifier, t, fix_pwd)).hexdigest()
	return base64.b64encode('%s|%s|%s|%s|%s' % (identifier, t, uid, role, validate_key)).strip()


def validate(key, fix_pwd, teacher=False):
	"""
	:param key: token
	:param fix_pwd: 偏移量
	:param teacher: 校验用户角色是否是老师
	:return:
	"""
	# t = int(time.time())
	try:
		token = key
		key = base64.b64decode(key)
		x = key.split('|')
		if len(x) != 5:
			logging.getLogger().warning('token参数数量不足')
			return {'code': 1, 'msg': 'token参数不足'}
		validate_key = hashlib.md5('%s%s%s' % (x[0], x[1], fix_pwd)).hexdigest()
		if validate_key == x[4]:
			logging.getLogger().info('认证通过')
			if teacher:  # 需要校验用户角色是否是老师
				if x[3] != "1":
					return {'code': 1, 'msg': '用户角色不是老师'}
			return {'code': 0, 'identifier': x[0], 'uid': x[2], 'role': x[3], "msg": "认证通过", "token": token}
		else:
			logging.getLogger().warning('密码不正确')
			return {'code': 1, 'msg': '密码不正确'}
	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())
		return {'code': 1, 'msg': 'token 错误'}


def encry_password(password, salt='salt'):
	string = password + salt
	return hashlib.new('md5', string).hexdigest()


class ConcurrentDayRotatingFileHandler(logging.handlers.BaseRotatingHandler):
	def __init__(self, filename, encoding=None, delay=False):
		logging.handlers.BaseRotatingHandler.__init__(self, filename, 'a', encoding, delay)
		self.day = time.strftime('%Y-%m-%d', time.localtime())

	def shouldRollover(self, record):
		now_day = time.strftime('%Y-%m-%d', time.localtime())
		if self.stream is None:
			self.stream = self._open()
		if now_day == self.day:
			return False
		return True

	def doRollover(self):
		if self.stream:
			self.stream.close()
			self.stream = None

		rotate_log = "%s.%s" % (self.baseFilename, self.day)
		if not os.path.exists(rotate_log):
			os.rename(self.baseFilename, rotate_log)
		self.day = time.strftime('%Y-%m-%d', time.localtime())

		if not self.delay:
			self.stream = self._open()


def set_logging(log_path, log_level='error'):
	def add_handler(log_name, formatter, level, logger=None):
		if not logger:
			return
		log_handler = ConcurrentDayRotatingFileHandler(log_name)
		log_formatter = logging.Formatter(formatter)
		log_handler.setFormatter(log_formatter)
		logger.addHandler(log_handler)
		logger.setLevel(level)

	LOG_LEVELS = {
		'critical': logging.CRITICAL, 'error': logging.ERROR,
		'warning': logging.WARNING, 'info': logging.INFO,
		'debug': logging.DEBUG
	}

	if not os.path.isdir(log_path):
		os.makedirs(log_path)

	# log_name = os.path.join(log_path, 'record.log')
	# logger = logging.getLogger('record')
	# formatter = '%(asctime)s %(message)s'
	# add_handler(log_name, formatter, logging.DEBUG, logger)

	log_name = os.path.join(log_path, 'service.log')
	logger = logging.getLogger()
	formatter = '%(asctime)s %(levelname)s %(process)d %(thread)d %(filename)s-%(funcName)s:%(lineno)d %(message)s'
	add_handler(log_name, formatter, LOG_LEVELS.get(log_level.lower(), logging.ERROR), logger)


def get_id_name(model, **kwargs):
	result = model.objects.filter(**kwargs).values('id', 'name')
	return result


def require_role(role=2):
	def _deco(func):
		def __deco(request, *args, **kwargs):
			request.session['pre_url'] = request.path
			try:
				if role != request.session.get('user')['role']:
					return HttpResponse(json.dumps({'errmsg': '权限不够'}, ensure_ascii=False))
			except TypeError:
				HttpResponseRedirect(reverse('login'))
			return func(request, *args, **kwargs)

		return __deco

	return _deco


def require_login():
	def _deco(func):
		def __deco(request, *args, **kwargs):
			request.session['pre_url'] = request.path
			if not request.session.get('login', None):
				return HttpResponse(json.dumps({'code': 1, 'msg': u'用户未登录'}, ensure_ascii=False))
			return func(request, *args, **kwargs)

		return __deco

	return _deco


def time_To_unixtime(str):
	"""2015-09-08 10:10:10 时间转换成为时间戳"""
	t = time.mktime(time.strptime(str, '%Y-%m-%d %H:%M:%S'))
	return int(t)


def time_comp_now(str):
	"""时间与当前时间比较,转换为几分钟前, 几小时前, 几天前, 几月前, 时间"""
	now = int(time.time())
	interval = now - time_To_unixtime(str)
	# print interval
	if interval < 60:
		return '%s秒前' % interval
	elif interval / 60 < 60:
		return '%s分钟前' % (interval / 60)
	elif interval / 60 / 60 < 24:
		return '%s小时前' % (interval / 60 / 60)
	elif interval / 60 / 60 / 24 < 30:
		return '%s天前' % (interval / 60 / 60 / 24)
	elif interval / 60 / 60 / 24 / 30 < 5:
		return '%s月前' % (interval / 60 / 60 / 24 / 30)
	else:
		return interval


def dictfetchall(sql):
	"Returns all rows from a cursor as a dict"
	cursor = connection.cursor()
	cursor.execute(sql)
	desc = cursor.description
	return [
		dict(zip([col[0] for col in desc], row))
		for row in cursor.fetchall()
	]


def get_day_of_day(n=0):
	'''''
	if n>=0,date is larger than today
	if n<0,date is less than today
	date format = "YYYY-MM-DD"
	'''
	if (n < 0):
		n = abs(n)
		return date.today() - timedelta(days=n)
	else:
		return date.today() + timedelta(days=n)


def sendmail(rcpt, subject, content):
	smtp_host = 'smtp.163.com'
	smtp_port = 25
	smtp_user = 'duminchao@163.com'
	smtp_pass = 'duminchaoi123'

	if isinstance(rcpt, str):
		rcpt = rcpt.split(',')
	elif not isinstance(rcpt, list):
		logging.getLogger().warning("SendMail: rcpt_to format invalid")
		return False

	try:
		smtp = smtplib.SMTP()
		smtp.connect(smtp_host, smtp_port)
		if smtp is not None:
			smtp.login(smtp_user, smtp_pass)

		msg = MIMEText(content, _subtype='html', _charset='utf-8')
		msg['From'] = smtp_user
		msg['To'] = ','.join(rcpt)
		msg['Subject'] = Header(subject, 'utf-8')

		smtp.sendmail(smtp_user, rcpt, msg.as_string())
		smtp.quit()
		return True
	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())
		return False


def sendmessage(phone, sms_param):
	req = top.api.AlibabaAliqinFcSmsNumSendRequest()
	req.set_app_info(top.appinfo(appkey='23764268', secret='00181054a64e2d9eb69711912d7a372a'))
	req.extend = ""
	req.sms_type = 'normal'
	req.sms_free_sign_name = "智量酷"
	req.sms_template_code = "SMS_62900005"
	req.rec_num = phone
	req.sms_param = json.dumps(sms_param)
	logging.getLogger().info(req.sms_param)
	try:
		resp = req.getResponse()
		logging.getLogger().info(resp)
		logging.getLogger().info(u'短信发送成功, phone:%s, sms_free_sign_name:%s, sms_template_code:%s 状态%s' % (
			req.rec_num, req.sms_free_sign_name, req.sms_template_code,
			resp['alibaba_aliqin_fc_sms_num_send_response']))
		return True
	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())
		return False


def pages(post_objects, page, lines=20):
	paginator = Paginator(post_objects, lines)
	try:
		show_lines = paginator.page(page)
	except PageNotAnInteger:
		show_lines = paginator.page(1)
	except EmptyPage:
		show_lines = []
	return show_lines


def last_seven_day():
	result = []
	for num in range(-7, 1):
		d = get_day_of_day(num)
		result.append(d.strftime('%Y-%m-%d'))
	return result


def second_to_hour(n):
	if n > 3600:
		a = n / 3600
		b = n % 3600
		if b > 60:
			c = b / 60
			return '%s小时%s分钟' % (a, c)
		else:
			return '%s小时' % a

	else:
		a = n / 60
		return '%s分钟' % a


def _get_refer_url(request):
	refer_url = request.META.get('HTTP_REFER', '/')
	host = request.META.get("HTTP_HOST")
	if refer_url.startswith('http') and host not in refer_url:
		refer_url = '/'
	return refer_url


# 获取动态查询条件
def get_kwargs(param_dict):
	"""
	:param param_dict:查询参数字典
	:return:
	"""
	kwargs = {}
	try:
		kwargs = {query_field: param for query_field, param in param_dict.items() if param}
	except:
		traceback.print_exc()
	finally:
		return kwargs


def str_to_int(param):
	"""字符串转int
	:param param:
	:return:
	"""
	try:
		param = int(param)
	except:
		param = 0
	finally:
		return param


def time_to_second(t):
	"""字符串时间转秒
	:param t:时间字符串
	:return:秒数
	"""
	try:
		h, m, s = t.strip().split(":")
	except:
		traceback.print_exc()
		h, m, s = 0, 0, 0
	return int(h) * 3600 + int(m) * 60 + int(s)


def get_thumbnail(orig, width=200, height=200):
	"""get the thumbnail of orig
	@return: InMemoryUploadedFile which can be assigned to ImageField
	"""
	quality = "keep"
	file_suffix = orig.name.split(".")[-1]
	filename = orig.name
	if file_suffix not in ["jpg", "jpeg"]:
		filename = "%s.jpg" % orig.name[:-(len(file_suffix) + 1)]
		quality = 95
	im = Image.open(orig)
	size = (width, height)
	thumb = im
	thumb.thumbnail(size, Image.ANTIALIAS)
	thumb_io = io.StringIO()
	thumb.save(thumb_io, format="JPEG", quality=quality)
	thumb_file = InMemoryUploadedFile(thumb_io, None, filename, 'image/jpeg', thumb_io.len, None)
	return thumb_file


# 制作面包屑
def make_bread_crumbs(request):
	"""
	:param request:
	:return:
	"""
	result = ""
	try:
		breadcrumbs_list = list()
		for one in request.breadcrumbs:
			breadcrumbs_list.append("<a href='%s'>%s</a>" % (one.url, one.name))
		result = " > ".join(breadcrumbs_list)
	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())
	finally:
		return result


# 生成字母加数字随机字符串
def get_random_code(count):
	src_digits = string.digits  # string_数字
	src_uppercase = string.ascii_uppercase  # string_大写字母
	src_lowercase = string.ascii_lowercase  # string_小写字母
	# 随机生成数字、大写字母、小写字母的组成个数（可根据实际需要进行更改）

	digits_num = random.randint(1, count - 2)
	uppercase_num = random.randint(1, count - digits_num - 1)
	lowercase_num = count - (digits_num + uppercase_num)

	# 生成字符串
	password = random.sample(src_digits, digits_num) + random.sample(src_uppercase, uppercase_num) + random.sample(
		src_lowercase, lowercase_num)

	# 打乱字符串
	random.shuffle(password)

	# 列表转字符串
	new_password = ''.join(password)

	return new_password
