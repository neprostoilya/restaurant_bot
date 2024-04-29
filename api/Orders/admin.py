from django.contrib import admin
from .models import Orders, DishOrder


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    search_fields = ['user', 'datetime_created', 'datetime_selected', 'place']
    
    list_display = ('pk', 'user', 'datetime_created', 'datetime_selected',
                    'place', 'people_quantity', 'total_price_all_dishes', 'total_quantity_all_dishes', 'status')


@admin.register(DishOrder)
class DishOrderAdmin(admin.ModelAdmin):
    search_fields = ['order', 'dish']
    list_display = ('pk', 'order', 'dish', 'total_quantity', 'total_price')


