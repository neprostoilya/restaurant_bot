from django.urls import path
from .views import GetDishByIdAPIView, GetDishesByCategoryAPIView

app_name = 'dishes'

urlpatterns = [
    path('get_dishes/<category>/', GetDishesByCategoryAPIView.as_view()),
    path('get_dish/<pk>/', GetDishByIdAPIView.as_view()),
]

