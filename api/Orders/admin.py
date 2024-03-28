from django.contrib import admin
from .models import Orders


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'datetime_created', 'datetime_selected',
                    'table', 'total_price', 'total_quantity', 'people_quantity', 'status')
        