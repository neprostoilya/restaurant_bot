from django.urls import path

from .views import RegisterAPIView, LoginAPIView, UserAPIView

app_name: str = 'Users'

urlpatterns = [
    path('users/<telegram_pk>/', UserAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]
