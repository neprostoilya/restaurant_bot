from django.urls import path
from .views import MainView, CategoriesView, CartView

app_name = 'frontend'

urlpatterns = [
    path('<token>/', MainView.as_view(), name='events_and_dishes_view'),
    path('<token>/category/<category>/', CategoriesView.as_view(), name='categories_view'),
    path('<token>/cart/', CartView.as_view(), name='carts_view'),
]