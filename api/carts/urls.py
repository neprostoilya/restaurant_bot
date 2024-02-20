from django.urls import path
from .views import GetCartByUserAPIView, CreateCartAPIView, DeleteCartAPIView

app_name = 'carts'

urlpatterns = [
    path('get_cart/<user>/', GetCartByUserAPIView.as_view(), name='get_cart'),
    path('create_cart/', CreateCartAPIView.as_view(), name='create_cart'),
    path('delete_cart/', DeleteCartAPIView.as_view(), name='delete_cart'),
]

