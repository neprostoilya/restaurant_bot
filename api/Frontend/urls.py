from django.urls import path
from .views import MainView, CategoriesView, SelectTimeForOrderView, \
    SelectTableForOrderView, CartView, SelectQuantityOfPeopleForOrderView

app_name = 'frontend'

urlpatterns = [
    path('', MainView.as_view(), name='events_and_dishes_view'),
    path('category/<category>/', CategoriesView.as_view(), name='categories_view'),
    path('cart/', CartView.as_view(), name='carts_view'),
    path('select_time/', SelectTimeForOrderView.as_view(), name='select_time_view'),
    path('select_table/', SelectTableForOrderView.as_view(), name='select_table_view'),
    path('select_quantity_of_people/', SelectQuantityOfPeopleForOrderView.as_view(), name='select_quantity_of_people_view'),
]