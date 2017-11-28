from django.contrib import admin

from applications.slideshow.models import Carousel
from zhiliangku.settings import tinymce_js


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pathwel', 'desc')
    search_fields = ('name',)

    class Media:
        js = tinymce_js


admin.site.register(Carousel, CarouselAdmin)
