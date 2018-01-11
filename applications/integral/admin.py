from django.contrib import admin
from applications.integral.models import *


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "gtype", "style", 'integral', "stock", "residue_stock", 'detail',)
    search_fields = ('name',)
    list_filter = ('gtype',)


@admin.register(ExchangeRecords)
class ExchangeRecordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_user', "goods", "ship", 'create_time', "ship_time",)
    search_fields = ('goods',)
    list_filter = ('ship',)
