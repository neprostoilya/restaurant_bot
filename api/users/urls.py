from django.urls import path

from .views import RegisterAPIView, LoginAPIView, \
    UserAPIView, UpdateUserAPIView
    

app_name: str = 'users'

urlpatterns = [
    path('users/<telegram_pk>/', UserAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('update/<telegram_pk>/', UpdateUserAPIView.as_view()),
]
