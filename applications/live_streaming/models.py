#!encoding:utf-8
from __future__ import unicode_literals

from colorfield.fields import ColorField
from django.core.exceptions import ValidationError
from django.db import models

from lib.polyv.live_api import *
from lib.storage import ImageStorage
from lib.util import NULL_BLANK_TRUE


class Live(models.Model):
	"""直播"""

	AUTOPLAY = (
		(0, '否'),
		(1, '是'),
	)
	STATUS = (
		("live", '正在直播'),
		("end", '直播结束'),
	)
	name = models.CharField('频道名称', max_length=50, unique=True)
	channelId = models.IntegerField('频道号', **NULL_BLANK_TRUE)
	channelPasswd = models.CharField('频道密码', max_length=50, default="111111", **NULL_BLANK_TRUE)
	playerColor = ColorField('播放器控制栏颜色', max_length=50, default="#666666", **NULL_BLANK_TRUE)
	autoPlay = models.IntegerField('是否自动播放', choices=AUTOPLAY, default=1)  # 是否自动播放，0/1，默认1
	pathwel = models.ImageField('直播图片', upload_to='live/%Y%m%d', storage=ImageStorage())
	status = models.CharField('状态', max_length=5, choices=STATUS, default='end')  # 频道的直播状态，字符串，值包括：live end
	data = models.TextField("创建直播接口返回值", **NULL_BLANK_TRUE)
	desc = models.TextField('简介', max_length=1000, default='', **NULL_BLANK_TRUE)

	def __unicode__(self):
		return self.name

	def clean(self):
		self.clean_fields()  # 校验model fields
		self.validate_unique()  # 校验field的唯一性

		# 首次创建直播
		if not self.channelId:
			create_result = create_live(self.name, autoplay=self.autoPlay, playercolor=self.playerColor,
										channelpasswd=self.channelPasswd)
			code = create_result.get("code")
			message = create_result.get("message", "")
			data = create_result.get("data", {})
			if code == 200:
				self.channelId = data.get("channelId")
				self.data = data
			else:
				raise ValidationError("".join(["创建直播频道异常 ", message]))
		else:  # 修改已经创建的直播
			history_live_obj = Live.objects.filter(id=self.id).first()

			# 修改直播频道名称
			if self.name != history_live_obj.name:
				set_result = update_live_name(self.channelId, self.name)
				set_result_code = set_result.get("code")
				set_result_message = set_result.get("message", "")
				if set_result_code != 200:
					raise ValidationError("".join(["修改频道名称异常 ", set_result_message]))

			# 设置频道密码
			if self.channelPasswd != history_live_obj.channelPasswd:
				set_result = setlivepasswd(self.channelId, self.channelPasswd)
				set_result_code = set_result.get("code")
				set_result_message = set_result.get("message", "")
				if set_result_code != 200:
					raise ValidationError("".join(["设置频道号密码异常 ", set_result_message]))

	def delete(self, *args, **kwargs):
		"""删除直播，同时删除保利威视直播频道
		:param args:
		:param kwargs:
		:return:
		"""
		ret_result = False
		try:
			delete_result = delete_live(self.channelId)
			status = delete_result.get("status")
			if status == "success":
				super(Live, self).delete()
				ret_result = True
		except:
			traceback.print_exc()
			logging.getLogger().error(traceback.format_exc())
		finally:
			return ret_result

	class Meta:
		db_table = 'Live'
		verbose_name = "直播间"
		verbose_name_plural = "直播间"
		ordering = ['name']
