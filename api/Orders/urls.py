from django.urls import path
from Orders.views import GetOrdersAPIView, CreateOrderAPIView
    

app_name = 'Dishes'

urlpatterns = [
    path('get_orders/', GetOrdersAPIView.as_view()),
    path('create_order/', CreateOrderAPIView.as_view())
]