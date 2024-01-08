from django.contrib import admin
from Categories.models import Categories

@admin.register(Categories)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title_ru',)
    list_display_links = ('title_ru',)

    