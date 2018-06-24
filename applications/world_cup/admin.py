from django.contrib import admin

from applications.world_cup.model_form import *
from applications.world_cup.models import *


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
	list_display = ('id', "title", "A", "B", "right",)
	search_fields = ('title',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
	list_display = ('id', "name", "flag",)
	search_fields = ('name',)


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
	list_display = (
		'id', "country_a", "country_b", "start_time", "a_victory", "common", "b_victory", "is_summary", "create_time")
	search_fields = ('name',)
	readonly_fields = ("create_time",)
	form = TournamentForm


@admin.register(BetRecord)
class BetRecordAdmin(admin.ModelAdmin):
	list_display = ('id', "user", "tournament", "country", "integral", "create_time")
	search_fields = ('user',)
	readonly_fields = ("create_time",)
