#!encoding:utf-8
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models

from lib.polyv.live_api import *
from lib.storage import ImageStorage
from colorfield.fields import ColorField


class Live(models.Model):
    """直播"""

    AUTOPLAY = (
        (0, '否'),
        (1, '是'),
    )
    STATUS = (
        ("live", '开启'),
        ("end", '关闭'),
    )
    name = models.CharField('直播名称', max_length=50, unique=True)
    channelId = models.IntegerField('直播频道ID', blank=True, null=True)
    channelPasswd = models.CharField('直播频道密码', max_length=50, blank=True, null=True, default="111111")
    playerColor = ColorField('播放器控制栏颜色', max_length=50, blank=True, null=True, default="#666666")
    autoPlay = models.IntegerField('是否自动播放', choices=AUTOPLAY, default=1)  # 是否自动播放，0/1，默认1
    pathwel = models.ImageField('直播图片', upload_to='live/img/%Y/%m/%d', storage=ImageStorage())
    status = models.CharField('直播状态', max_length=5, choices=STATUS, default='end')  # 频道的直播状态，字符串，值包括：live end
    data = models.TextField("创建直播接口返回值", blank=True, null=True)
    desc = models.TextField('直播简介', max_length=1000, blank=True, null=True, default='')

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
            message = create_result.get("message")
            data = create_result.get("data", {})
            if code == 200:
                self.channelId = data.get("channelId")
                self.data = data
            else:
                raise ValidationError("".join(["创建直播频道异常 ", message]))
        else:  # 修改已经创建的直播
            history_live_obj = Live.objects.filter(id=self.id).first()

            # 设置频道密码
            if self.channelPasswd != history_live_obj.channelPasswd:
                set_result = setlivepasswd(self.channelId, self.channelPasswd)
                set_result_code = set_result.get("code")
                set_result_message = set_result.get("message")
                if set_result_code != 200:
                    raise ValidationError("".join(["设置频道号密码 ", set_result_message]))

    def delete(self, *args, **kwargs):
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
        verbose_name = "直播"
        verbose_name_plural = "直播"
