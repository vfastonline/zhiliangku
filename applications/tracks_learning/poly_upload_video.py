#!encoding:utf-8
import hashlib
import json
import time

from django.http import HttpResponse
from django.views.generic import View

from conf.conf_core import *


class UploadVideoPolyvParam(View):
	"""上传视频到保利威视接口参数，3分钟获取一次"""

	def get(self, request, *args, **kwargs):
		ts = str(int(round(time.time() * 1000)))
		result_dict = dict()

		hash_str = hashlib.new("md5", "".join([ts, WRITETOKEN])).hexdigest()
		sign = hashlib.new("md5", "".join([SECRETKEY, ts])).hexdigest()
		result_dict["writeToken"] = WRITETOKEN
		result_dict["userid"] = USERID
		result_dict["ts"] = ts
		result_dict["hash"] = hash_str
		result_dict["sign"] = sign
		result_dict["readToken"] = READTOKEN
		return HttpResponse(json.dumps(result_dict, ensure_ascii=False))
