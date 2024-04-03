from django.urls import path

from .views import RegisterAPIView, LoginAPIView, \
    UserAPIView, UpdateUserAPIView, GetUserLanguageAPIView, \
    CheckManagerAPIView
    

app_name: str = 'users'

urlpatterns = [
    path('users/<telegram_pk>/', UserAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('update/<telegram_pk>/', UpdateUserAPIView.as_view()),
    path('get_user_language/<telegram_pk>/', GetUserLanguageAPIView.as_view()),
    path('check_manager/<telegram_pk>/', CheckManagerAPIView.as_view()),
]
