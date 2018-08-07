#!encoding:utf-8
import subprocess
import json
import re

import datetime
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from applications.assessment.models import DockerPort
from applications.medal.models import *
from applications.tracks_learning.models import Project, Technology
from applications.tracks_learning.models import UnlockVideo
from applications.tracks_learning.models import Video
from lib.permissionMixin import class_view_decorator, user_login_required
from lib.util import str_to_int

"""
创建docker
docker run -it --rm -d  -v /usr/local/share/xiaodu/script:/usr/local/share/xiaodu/script  -p 动态端口:7681 --name '容器名字' tsl0922/ttyd（镜像名称）
容器名字：token_videoid
"""

docker_sh = "/usr/local/share/xiaodu/script/docker.sh"  # docker启动/停止脚本
kaohe_sh = "/usr/local/share/xiaodu/script/kaohe.sh"  # 判题脚本


@class_view_decorator(user_login_required)
class AssessmentPage(View):
	"""考核-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "assess/info/index.html"
		return render(request, template_name, {})


@class_view_decorator(user_login_required)
class ConstructDocker(View):
	"""构建docker"""

	def __init__(self):
		super(ConstructDocker, self).__init__()
		self.port = ""  # 容器端口
		self.image_port = ""  # 镜像端口
		self.container = ""  # 容器名称
		self.image = ""  # 镜像名称
		self.shell_name = ""  # 判题脚本名称
		self.assess_time = 0  # 考核时长
		self.topic = ""  # 考核题目
		self.video_id = 0  # 考核类型视频ID
		self.token = ""
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": {
				"docker": "",
				"topic": "",
				"assess_time": 0,
			},
		}

	def get(self, request, *args, **kwargs):
		try:
			self.token = re.sub('=', '', kwargs.get('token', ""))  # 登录用户 token
			self.video_id = str_to_int(request.GET.get('video_id', 0))  # 考核类型 视频ID

			# 获取未占用容器端口
			self.get_docker_port()

			# 获取容器相关信息
			self.get_container_info()

			# 检查容器是否已经存在
			self.construct_container()

			# 记录容器名称、端口、使用到期时间
			maturity = datetime.datetime.now() + datetime.timedelta(minutes=self.assess_time)
			DockerPort.objects.get_or_create(container=self.container, port=self.port, maturity=maturity)

			# 接口返回值
			result_data = {
				"docker": ":".join(["118.190.209.153", self.port]),
				"topic": self.topic,
				"assess_time": self.assess_time,
			}
			self.result_dict["data"] = result_data
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))

	def construct_container(self):
		"""构建新的容器
		:return:
		"""
		try:
			param = {"docker_sh": docker_sh, "container": self.container}
			stop_command = "ssh root@docker sh {docker_sh} stop {container}".format(**param)
			param = {
				"docker_sh": docker_sh,
				"container": self.container,
				"port": self.port,
				"image_port": self.image_port,
				"image": self.image,
				"shell_name": self.shell_name,
			}
			start_command = "ssh root@docker sh {docker_sh} start {container} {port} {image_port} {image} {shell_name}".format(
				**param)

			# 查询是否已经为该用户准备容器，有就销毁
			dockerports = DockerPort.objects.filter(container=self.container)
			if dockerports.exists():  # 销毁，不使用旧容器，避免定时任务提前销毁
				stop_info = subprocess.getoutput(stop_command)
				try:
					if not int(stop_info):
						dockerports.delete()
				except:
					traceback.print_exc()
					logging.getLogger().error(traceback.format_exc())
					self.result_dict["err"] = 1
					self.result_dict["msg"] = traceback.format_exc()
					return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))
			start_info = subprocess.getoutput(start_command)
			print(start_command)
			print(start_info)
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))

	def get_container_info(self):
		"""获取容器相关信息
		:return:
		"""
		try:
			videos = Video.objects.filter(id=self.video_id, type="3")
			if videos.exists():
				self.container = "-".join([self.token, str(self.video_id)])
				self.image = videos.first().docker.image if videos.first().docker else ""
				self.image_port = videos.first().docker.port if videos.first().docker else ""
				self.assess_time = videos.first().assess_time
				self.shell_name = videos.first().shell.url.split("/")[-1] if videos.first().shell else ""
				self.topic = videos.first().topic
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))

	def get_docker_port(self):
		"""获取未使用的容器端口
		:return:
		"""
		try:
			self.port = str(random.randint(7000, 10000))
			dockerports = DockerPort.objects.filter(port=self.port)
			if dockerports.exists():
				self.get_docker_port()
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))


@class_view_decorator(user_login_required)
class AssessmentResult(View):
	"""考核-结果-页面"""

	def get(self, request, *args, **kwargs):
		template_name = "assess/result/index.html"
		return render(request, template_name, {})


"""
判题shell返回json结果
{
	"is_pass": 1,
	"total": 5,
	"right": 5,
	"wrong": 0,
	"msg": "错误提示信息"
}
is_pass：   1：通过考核     0：未通过考核
total：题目总数，数字
right：答对题目数，数字
wrong：答错题目数，数字
msg：哪些题目答错信息提示
"""


@class_view_decorator(user_login_required)
class AssessmentResultInfo(View):
	"""考核-结果"""

	def __init__(self):
		super(AssessmentResultInfo, self).__init__()
		self.container = ""  # 容器名称
		self.shell_name = ""  # 判题脚本名称
		self.video_id = 0  # 考核类型视频ID
		self.token = ""
		self.result_dict = {
			"err": 0,
			"msg": "success",
			"data": {
				"is_pass": 0,  # 是否通过，1：是；0：否
				"total": 0,  # 题目总数
				"right": 0,  # 答对个数
				"wrong": 0,  # 答错个数
				"msg": "",  # 错误提示
				"medal": "",  # 勋章图片地址
			},
		}

	def post(self, request, *args, **kwargs):
		try:
			param_dict = json.loads(request.body)
			self.token = re.sub('=', '', kwargs.get('token', ""))  # 当前登录用户token
			custom_user_id = str_to_int(kwargs.get('uid', 0))  # 用户ID
			self.video_id = str_to_int(param_dict.get('video_id', 0))

			videos = Video.objects.filter(id=self.video_id, type="3")
			if videos.exists():
				self.container = "-".join([self.token, str(self.video_id)])  # 容器的名称
				self.shell_name = videos.first().shell.url.split("/")[-1]

			is_pass = 0
			if self.container and self.shell_name:
				# 通过shell判题
				param = {"kaohe_sh": kaohe_sh, "container": self.container, "shell_name": self.shell_name}
				command = "ssh root@docker sh {kaohe_sh} {container} {shell_name}".format(**param)
				result_info = subprocess.getoutput(command)
				print(type(result_info), result_info)

				try:
					command_result_dicts = json.loads(result_info)
					is_pass = str_to_int(command_result_dicts.get("is_pass", 0))
					total = str_to_int(command_result_dicts.get("total", 0))
					right = command_result_dicts.get("right", 0)
					wrong = command_result_dicts.get("wrong", 0)
					msg = command_result_dicts.get("msg", "")
					self.result_dict["data"]["is_pass"] = is_pass
					self.result_dict["data"]["total"] = total
					self.result_dict["data"]["right"] = right
					self.result_dict["data"]["wrong"] = wrong
					self.result_dict["data"]["msg"] = msg
				except:
					traceback.print_exc()
					logging.getLogger().error(traceback.format_exc())
					self.result_dict["err"] = 1
					self.result_dict["msg"] = traceback.format_exc()
			else:
				self.result_dict["msg"] = u"未找到正确考核信息"

			# 增加学生通过考核记录
			customuser = CustomUser.objects.get(id=custom_user_id)
			if is_pass:
				medal_pathwel = ""
				unlockvideos = UnlockVideo.objects.filter(custom_user=customuser, video=videos.first())
				if not unlockvideos.exists():
					new_obj = UnlockVideo.objects.create(video=videos.first(), custom_user=customuser, is_pass=True)
					if new_obj:
						# 判断考核类型，颁发勋章 *初次完成考核 *完成项目考核 *完成技术类别下总项目考核
						unlockvideos = UnlockVideo.objects.filter(custom_user=customuser, is_pass=True)
						if unlockvideos.count() == 1:  # 初次
							add_param = ["first_complete_assess", customuser]
							medal_pathwel = CustomUserMedal.add_customuser_medal(*add_param)
						elif Project.objects.filter(video=videos.first()).exists():  # 项目考核
							add_param = ["complete_project_assess", customuser]
							medal_pathwel = CustomUserMedal.add_customuser_medal(*add_param)

						elif Technology.objects.filter(video=videos.first()).exists():  # 项目总考核
							add_param = ["complete_overall_project_assess", customuser]
							medal_pathwel = CustomUserMedal.add_customuser_medal(*add_param)
				else:
					unlockvideos.update(is_pass=True)

				self.result_dict["data"]["medal"] = medal_pathwel
			else:  # 未通过考核
				unlockvideos = UnlockVideo.objects.filter(custom_user=customuser, video=videos.first())
				if not unlockvideos.exists():
					UnlockVideo.objects.create(video=videos.first(), custom_user=customuser)
				else:
					unlockvideos.update(times=F("times") + 0)

			# 销毁docker
			self.destroy()
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
			self.result_dict["err"] = 1
			self.result_dict["msg"] = traceback.format_exc()
		finally:
			return HttpResponse(json.dumps(self.result_dict, ensure_ascii=False))

	def destroy(self):
		"""销毁docker
		:return:
		"""
		try:
			param = {"docker_sh": docker_sh, "container": self.container}
			stop_command = "ssh root@docker sh {docker_sh} stop {container}".format(**param)
			stop_info = subprocess.getoutput(stop_command)
			try:
				if not int(stop_info):
					DockerPort.objects.filter(container=self.container).delete()
			except:
				traceback.print_exc()
				logging.getLogger().error(traceback.format_exc())
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
