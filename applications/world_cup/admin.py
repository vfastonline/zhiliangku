from django.contrib import admin

from applications.world_cup.model_form import *
from applications.world_cup.models import *
from zhiliangku.settings import tinymce_js


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
		'id', "country_a", "country_b", "start_time", "a_victory", "common", "b_victory", "is_summary", "summary_time",
		"create_time")
	search_fields = ('name',)
	readonly_fields = ("summary_time", "create_time",)
	form = TournamentForm


@admin.register(BetRecord)
class BetRecordAdmin(admin.ModelAdmin):
	list_display = ('id', "user", "tournament", "country", "integral", "create_time")
	search_fields = ('user',)
	readonly_fields = ("create_time",)


@admin.register(BetRecordCount)
class BetRecordCountAdmin(admin.ModelAdmin):
	list_display = ('id', "count",)


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
	list_display = ('id', "chart", "create_time",)

	class Media:
		js = tinymce_js
