#!encoding:utf-8
import logging
import traceback
import random
from applications.assessment.models import DockerPort


def get_docker_port():
	"""获取未使用的端口
	:return:
	"""
	port = "7681"
	try:
		port = random.randint(7000, 10000)
		dockerports = DockerPort.objects.filter(port=str(port))
		if dockerports.exists():
			get_docker_port()
	except:
		traceback.print_exc()
		logging.getLogger().error(traceback.format_exc())
	finally:
		return port
