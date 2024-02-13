from django.contrib import admin
from .models import Carts


@admin.register(Carts)
class CartsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'dish', 'amount')
    list_display_links = ('user',)