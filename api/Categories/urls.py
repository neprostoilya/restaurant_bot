from django.urls import path
from Categories.views import GetCategoriesAPIView, CategoriesView

app_name = 'Categories'

urlpatterns = [
    path('get_categories/', GetCategoriesAPIView.as_view()),
    path('categories_view/', CategoriesView.as_view()),
]