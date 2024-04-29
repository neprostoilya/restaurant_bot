from django.contrib import admin
from .models import Categories


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ['title_ru',]
    list_display = ('pk', 'title_ru',)
    list_display_links = ('title_ru',)
