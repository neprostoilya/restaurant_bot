from django.urls import path
from .views import CreateOrderAPIView, GetOrdersByUserAPIView
    

app_name: str = 'Orders'

urlpatterns = [
    path('create_order/', CreateOrderAPIView.as_view()),
    path('get_orders_by_user/<user>', GetOrdersByUserAPIView.as_view())
]