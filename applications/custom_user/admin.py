from django.contrib import admin
from applications.custom_user.models import CustomUser
from zhiliangku.settings import tinymce_js


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'nickname', 'role', 'user_img')
    search_fields = ('username', 'nickname')


admin.site.register(CustomUser, CustomUserAdmin)
