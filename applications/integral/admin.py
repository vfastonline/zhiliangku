from django.contrib import admin
from applications.integral.models import *


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "gtype", "style", 'integral', "stock", "residue_stock", 'detail',)
    search_fields = ('name',)
    list_filter = ('gtype',)

    def suit_row_attributes(self, obj, request):
        css_class = {
            0: 'error',
        }.get(obj.residue_stock)
        if css_class:
            return {'class': css_class}


@admin.register(ExchangeRecords)
class ExchangeRecordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_user', "goods", "ship", 'create_time', "ship_time",)
    search_fields = ('goods',)
    list_filter = ('ship',)

    def suit_row_attributes(self, obj, request):
        css_class = {
            False: 'warning',
        }.get(obj.ship)
        if css_class:
            return {'class': css_class}