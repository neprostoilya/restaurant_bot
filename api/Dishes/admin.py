from django.contrib import admin
from Dishes.models import Dishes

@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title_ru', 'descriptiontrim', 'category', 'price', 'img_preview')
    list_display_links = ('title_ru',)
    list_editable = ('price', 'category')
    