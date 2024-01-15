from django.contrib import admin
from Users.models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'surname', 'phone', 'is_staff', 'is_admin')
    list_editable = ('is_staff', 'is_admin')
    list_display_links = ('name',)
    exclude  = ('groups', 'user_permissions', 'is_superuser', 'last_login', 'password')

    