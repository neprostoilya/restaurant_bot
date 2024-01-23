from django.contrib import admin
from Dishes.models import Dishes

@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'descriptiontrim', 'category', 'price', 'img_preview')
    list_display_links = ('title',)
    list_editable = ('price', 'category')
    