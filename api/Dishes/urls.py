from django.urls import path
from Dishes.views import GetDishesAPIView, DishesView

app_name = 'Dishes'

urlpatterns = [
    path('get_dishes/', GetDishesAPIView.as_view()),
    path('dishes/', DishesView.as_view()),
]