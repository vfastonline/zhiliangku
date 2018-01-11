from django.contrib import admin

from applications.slideshow.models import Carousel


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "category", "sequence", 'pathwel', "desc")
    search_fields = ('name',)
    list_filter = ('category',)
