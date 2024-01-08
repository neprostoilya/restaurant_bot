from django.contrib import admin
from Orders.models import Orders

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'dish', 'completed')
    list_display_links = ('user',)
    