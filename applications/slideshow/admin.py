from django.contrib import admin

from applications.slideshow.models import Carousel


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pathwel')
    search_fields = ('name',)
