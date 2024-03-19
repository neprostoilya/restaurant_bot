from django.urls import path
from .views import CreateOrderAPIView
    

app_name: str = 'Orders'

urlpatterns = [
    path('create_order/', CreateOrderAPIView.as_view())
]