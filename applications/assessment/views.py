#!encoding:utf-8
import commands
import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from applications.assessment.generate_docker_port import *
from applications.tracks_learning.models import Video
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int

"""
创建docker
docker run -it --rm -d  -v /usr/local/share/xiaodu/script:/usr/local/share/xiaodu/script  -p 动态端口:7681 --name '容器名字' tsl0922/ttyd（镜像名称）
容器名字：token_videoid
"""


@class_view_decorator(user_login_required)
class AssessmentPage(View):
	"""考核-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "assess/info/index.html"
		return render(request, template_name, {})


@class_view_decorator(user_login_required)
class ConstructDocker(View):
	"""构建docker"""

	def get(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success", "data": dict()}
		try:
			token = kwargs.get('token', "")  # 当前登录用户token
			video_id = str_to_int(request.GET.get('video_id', 0))  # 考核类型的视频ID

			# 获取端口
			port = get_docker_port()
			port = 7681
			image_port = ""
			container = ""
			image = ""
			shell_name = ""
			assess_time = 0
			topic = ""

			# 容器名字
			videos = Video.objects.filter(id=video_id, type="3")
			if videos.exists():
				container = "-".join([token, str(video_id)])
				image = videos.first().docker.image if videos.first().docker else ""
				image_port = videos.first().docker.port if videos.first().docker else ""
				assess_time = videos.first().assess_time
				shell_name = videos.first().shell.url.split("/")[-1] if videos.first().shell else ""
				topic = videos.first().topic

			# 检查容器是否已经存在
			stop_command = "ssh root@docker sh /usr/local/share/xiaodu/script/docker.sh stop {container}".format(
				container=container)
			start_command = "ssh root@docker sh /usr/local/share/xiaodu/script/docker.sh start {container} {port} {image_port} {image} {shell_name}".format(
				container=container, port=port, image_port=image_port, image=image, shell_name=shell_name)
			dockerports = DockerPort.objects.filter(container=container)
			if dockerports.exists():  # 销毁，不使用旧环境，避免定时任务提前销毁
				stop_info = commands.getoutput(stop_command)
				if not int(stop_info):
					dockerports.delete()
			start_info = commands.getoutput(start_command)
			print start_command
			print start_info

			# 入库创建记录
			maturity = datetime.datetime.now() + datetime.timedelta(minutes=assess_time)
			DockerPort.objects.get_or_create(container=container, port=port, maturity=maturity)
			# start_info = json.loads(start_info)
			result_data = {"ip": "", "port": port, "topic": topic}
			result_dict["data"] = result_data
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class AssessmentResult(View):
	"""考核-结果"""

	def post(self, request, *args, **kwargs):
		result_dict = {"err": 0, "msg": "success", "grade": "0"}
		try:
			param_dict = json.loads(request.body)
			token = kwargs.get('token', "")  # 当前登录用户token
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			video_id = str_to_int(param_dict.get('video_id', 0))
			container = "-".join([token, video_id])
			videos = Video.objects.filter(id=video_id, type="3")
			shell_name = ""
			if videos.exists():
				container = "-".join([token, video_id])
				shell_name = videos.first().shell.split("/")[-1]

			command = "ssh root@docker sh /usr/local/share/xiaodu/script/kaohe.sh {container} {shell_name}".format(
				container=container, shell_name=shell_name)
			result_info = commands.getoutput(command)
			print type(result_info), result_info

			# 销毁docker
			container = "-".join([token, str(video_id)])
			stop_command = "ssh root@docker sh /usr/local/share/xiaodu/script/docker.sh stop {container}".format(
				container=container)
			stop_info = commands.getoutput(stop_command)
			if not int(stop_info):
				dockerports = DockerPort.objects.filter(container=container).delete()
			
			result_dicts = json.loads(result_info)
			result_dict["grade"] = result_dicts.get("grade", "x")
			result_dict["msg"] = result_dicts.get("msg", "x")
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			result_dict["err"] = 1
			result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(result_dict, ensure_ascii=False))

	def destroy(self):
		try:
			pass
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			pass
