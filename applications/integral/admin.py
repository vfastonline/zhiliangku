#!encoding:utf-8
from django.contrib import admin
from applications.integral.models import *


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "gtype", "style", 'integral', "stock", "residue_stock", 'detail', "imagess")
    search_fields = ('name',)
    list_filter = ('gtype',)

    def suit_row_attributes(self, obj, request):
        css_class = {
            0: 'error',
        }.get(obj.residue_stock)
        if css_class:
            return {'class': css_class}

    def imagess(self, obj):
        return '<img src="%s" height="24" width="24" />' % (obj.images.url)

    imagess.allow_tags = True
    imagess.short_description = "商品图片"


@admin.register(ExchangeRecords)
class ExchangeRecordsAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'custom_user', "goods", "ship", 'create_time', "ship_time", "receiver", "contact_number", "address")
    search_fields = ('goods__name', "custom_user__nickname")
    list_filter = ('ship',)

    def receiver(self, obj):
        return obj.custom_user.receiver

    receiver.short_description = "收货人"

    def contact_number(self, obj):
        return obj.custom_user.contact_number

    contact_number.short_description = "联系电话"

    def address(self, obj):
        return obj.custom_user.address

    address.short_description = "收货地址"

    def suit_row_attributes(self, obj, request):
        css_class = {
            False: 'warning',
        }.get(obj.ship)
        if css_class:
            return {'class': css_class}
