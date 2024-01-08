from django.urls import path
from Orders.views import GetOrdersAPIView, GetOrdersByUserAPIView, \
    CreateOrderAPIView

app_name = 'Dishes'

urlpatterns = [
    path('get_orders/', GetOrdersAPIView.as_view()),
    path('get_order_by_user/<user>', GetOrdersByUserAPIView.as_view()),
    path('create_order/', CreateOrderAPIView.as_view())
]