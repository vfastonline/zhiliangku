from django.contrib import admin

from applications.custom_user.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'role', 'user_img')
    search_fields = ('username', 'nickname')


admin.site.register(CustomUser, CustomUserAdmin)
