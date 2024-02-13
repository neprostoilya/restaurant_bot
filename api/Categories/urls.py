from django.urls import path
from .views import GetCategoriesAPIView

app_name: str = 'Categories'

urlpatterns = [
    path('get_categories/', GetCategoriesAPIView.as_view()),
]