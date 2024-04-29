from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ['username', 'phone', 'telegram_pk']
    list_display = ('pk', 'username', 'phone', 'telegram_pk', 'is_staff', 'is_admin')
    list_editable = ('is_staff', 'is_admin')
    list_display_links = ('username',)
    exclude = ('groups', 'user_permissions', 'is_superuser', 'last_login', 'password')
