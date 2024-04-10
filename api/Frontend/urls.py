from django.urls import path
from .views import *

app_name = 'frontend'

urlpatterns = [
    path('', ChooseLanguageView.as_view(), name='choose_language_view'),
    path('ru/', MainViewRU.as_view(), name='events_and_dishes_view_ru'),
    path('ru/events/', EventsViewRU.as_view(), name='events_view_ru'),
    path('ru/category/<category>/', CategoriesViewRU.as_view(), name='categories_view_ru'),
    path('ru/cart/', CartViewRU.as_view(), name='carts_view_ru'),
    path('ru/select_time/', SelectTimeForOrderViewRU.as_view(), name='select_time_view_ru'),
    path('ru/select_table/', SelectTableForOrderViewRU.as_view(), name='select_table_view_ru'),
    path('ru/select_quantity_of_people/', SelectQuantityOfPeopleForOrderViewRU.as_view(), name='select_quantity_of_people_view_ru'),
    path('uz/', MainViewUZ.as_view(), name='events_and_dishes_view_uz'),
    path('uz/events/', EventsViewUZ.as_view(), name='events_view_uz'),
    path('uz/category/<category>/', CategoriesViewUZ.as_view(), name='categories_view_uz'),
    path('uz/cart/', CartViewUZ.as_view(), name='carts_view_uz'),
    path('uz/select_time/', SelectTimeForOrderViewUZ.as_view(), name='select_time_view_uz'),
    path('uz/select_table/', SelectTableForOrderViewUZ.as_view(), name='select_table_view_uz'),
    path('uz/select_quantity_of_people/', SelectQuantityOfPeopleForOrderViewUZ.as_view(), name='select_quantity_of_people_view_uz'),
]