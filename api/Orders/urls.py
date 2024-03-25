from django.urls import path
from .views import CreateOrderAPIView, GetOrdersByUserAPIView, \
    UpdateOrderStatusAPIView, GetOrderByOrderIdAPIView
    

app_name: str = 'Orders'

urlpatterns = [
    path('create_order/', CreateOrderAPIView.as_view()),
    path('get_orders_by_user/<user>/', GetOrdersByUserAPIView.as_view()),
    path('update_order_status/<order_id>/', UpdateOrderStatusAPIView.as_view()),
    path('get_order_by_order_id/<order_id>/', GetOrderByOrderIdAPIView.as_view())
]