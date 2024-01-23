from django.contrib import admin
from Categories.models import Categories, Subategories

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    list_display_links = ('title',)

@admin.register(Subategories)
class SubategoriesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category')
    list_editable = ('category', )
    list_display_links = ('title',)