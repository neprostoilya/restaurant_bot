from django.contrib import admin
from Events.models import Events

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'descriptiontrim', 'img_preview')
    list_display_links = ('title',)
    