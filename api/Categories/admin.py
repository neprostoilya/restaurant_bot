from django.contrib import admin
from .models import Categories


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    list_display_links = ('title',)
