from django.urls import path
from Categories.views import GetCategoriesAPIView

app_name = 'Categories'

urlpatterns = [
    path('get_categories/', GetCategoriesAPIView.as_view()),
]