from django.contrib import admin

from applications.custom_user.models import CustomUser, CustomUserAuths


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'role', 'avatar')
    search_fields = ('nickname',)


@admin.register(CustomUserAuths)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_user_id', 'identity_type', 'identifier', "credential")
    search_fields = ('custom_user_id__nickname', "identity_type",)
