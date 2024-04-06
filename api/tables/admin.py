from django.contrib import admin
from .models import Tables


@admin.register(Tables)
class TablesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'number', 'status')
