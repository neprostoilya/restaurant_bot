from django.urls import path
from Users.views import RegisterAPIView, LoginAPIView, \
    GetUsersAPIView

app_name = 'Users'

urlpatterns = [
    path('get_users/', GetUsersAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
]