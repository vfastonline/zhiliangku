from django.contrib import admin

from backstage.home.models import LearnTask


@admin.register(LearnTask)
class LearnTaskAdmin(admin.ModelAdmin):
	list_display = ('id', "video", "custom_user", "create_time", "update_time",)
	search_fields = ('video__name',)
