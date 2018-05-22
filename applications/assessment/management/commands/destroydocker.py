# coding=utf-8
import commands
import datetime
import traceback

from django.core.management.base import BaseCommand, CommandError

from applications.assessment.models import DockerPort


class Command(BaseCommand):
	help = "Destroy the specified docker container"

	def handle(self, *args, **options):
		"""检查正在运行docker是否到考核结束时间，并销毁
		:return:
		"""
		try:
			# 获取后台所有容器名称
			names = commands.getoutput("ssh root@docker docker ps | awk '{print $NF}'")
			name_list = names.split("\n")

			# 查询所有到期容器
			filter_param = {
				"container__in": name_list,
				"maturity__lte": datetime.datetime.now()
			}
			dockerports = DockerPort.objects.filter(**filter_param)
			maturity_container_list = dockerports.values_list("container", flat=True)
			for one_container in maturity_container_list:
				stop_command = "ssh root@docker sh /usr/local/share/xiaodu/script/docker.sh stop '{container}'".format(
					container=one_container)
				stop_info = commands.getoutput(stop_command)
				if not int(stop_info):
					DockerPort.objects.filter(container=one_container).delete()
		except:
			traceback.print_exc()
			raise CommandError(traceback.format_exc())
