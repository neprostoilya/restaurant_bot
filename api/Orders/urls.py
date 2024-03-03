from django.urls import path
from .views import GetOrdersAPIView, CreateOrderAPIView
    

app_name: str = 'Orders'

urlpatterns = [
    path('get_orders/<cart>/', GetOrdersAPIView.as_view()),
    path('create_order/', CreateOrderAPIView.as_view())
]