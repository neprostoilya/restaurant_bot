from django.contrib import admin
from .models import Events


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'descriptiontrim', 'img_preview')
