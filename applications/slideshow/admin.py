from django.contrib import admin

from applications.slideshow.models import Carousel


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pathwel')
    search_fields = ('name',)


admin.site.register(Carousel, CarouselAdmin)
