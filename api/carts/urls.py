from django.urls import path
from .views import GetCartByUserAPIView, CreateCartAPIView

app_name = 'carts'

urlpatterns = [
    path('get_cart/<user>/', GetCartByUserAPIView.as_view()),
    path('create_cart/', CreateCartAPIView.as_view(), name='create_cart'),
]

