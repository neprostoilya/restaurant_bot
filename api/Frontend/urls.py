from django.urls import path
from .views import MainView, CategoriesView

app_name = 'frontend'

urlpatterns = [
    path('', MainView.as_view(), name='events_and_dishes_view'),
    path('<category>/', CategoriesView.as_view(), name='categories_view'),
]