from django.urls import path
from Categories.views import GetCategoriesAPIView, GetSubcategoriesAPIView

app_name = 'Categories'

urlpatterns = [
    path('get_categories/', GetCategoriesAPIView.as_view()),
    path('get_subcategories/', GetSubcategoriesAPIView.as_view()),
]