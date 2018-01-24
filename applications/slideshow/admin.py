from django.contrib import admin

from applications.slideshow.model_form import *


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "category", "video", "sequence", 'pathwel', "desc")
    search_fields = ('name',)
    list_filter = ('category',)
    form = CarouselForm
