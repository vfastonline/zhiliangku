#!encoding:utf-8
from __future__ import unicode_literals

import os

from django.core.validators import MinValueValidator
from django.db import models

from applications.custom_user.models import CustomUser
from lib.storage import ImageStorage
import django.utils.timezone as timezone


def upload_to(instance, fielname):
    return os.path.join("goods", str(instance.id), fielname)


class Goods(models.Model):
    """商品"""

    GTYPE = (
        ("1", "实体商品"),
        ("2", "虚拟商品"),
    )

    name = models.CharField('商品名称', max_length=256)
    gtype = models.CharField('商品类型', max_length=1, choices=GTYPE)
    style = models.CharField('款式', max_length=50, blank=True, null=True, default="")
    images = models.ImageField('商品图片', upload_to=upload_to, storage=ImageStorage())
    integral = models.PositiveIntegerField("积分", validators=[MinValueValidator(1)])
    stock = models.PositiveIntegerField("库存", default=0)
    residue_stock = models.PositiveIntegerField("剩余库存", default=0)
    detail = models.TextField(verbose_name="商品详情", default="")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'Goods'
        verbose_name = "商品"
        verbose_name_plural = "商品"


class ExchangeRecords(models.Model):
    """积分兑换记录"""

    custom_user = models.ForeignKey(CustomUser, verbose_name="兑换用户", related_name="UserExchangeRecords")
    goods = models.ForeignKey(Goods, verbose_name="兑换商品")
    ship = models.BooleanField('是否发货', default=False)
    create_time = models.DateTimeField(verbose_name='兑换时间', default = timezone.now)
    ship_time = models.DateTimeField(verbose_name='发货时间', auto_now=True)

    def __unicode__(self):
        return self.custom_user.nickname + "|" + self.goods.name

    class Meta:
        db_table = 'ExchangeRecords'
        verbose_name = "兑换记录"
        verbose_name_plural = "兑换记录"
