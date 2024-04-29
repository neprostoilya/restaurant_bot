from django.contrib import admin
from .models import Places


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    search_fields = ['title_ru',]
    list_display = ('pk', 'title_ru', 'is_view')
    list_editable = ('is_view',)
