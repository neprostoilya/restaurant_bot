from django.urls import path
from .views import *

app_name = 'frontend'

urlpatterns = [
    path('', ChooseLanguageView.as_view(), name='choose_language_view'),
    
    
    path('ru/type_order/', ChooseTypeOrderViewRU.as_view(), name='choose_type_order_view_ru'),
    path('ru/booking_table/', MainBookingTableViewRU.as_view(), name='events_and_dishes_booking_table_view_ru'),
    path('ru/booking_table/events/', EventsBookingTableViewRU.as_view(), name='events_booking_table_view_ru'),
    path('ru/booking_table/category/<category>/', CategoriesBookingTableViewRU.as_view(), name='categories_booking_table_view_ru'),
    path('ru/booking_table/cart/', CartBookingTableViewRU.as_view(), name='carts_booking_table_view_ru'),
    path('ru/booking_table/select_time/', SelectTimeForOrderBookingTableViewRU.as_view(), name='select_time_booking_table_view_ru'),
    path('ru/booking_table/select_place/', SelectPlaceForOrderBookingTableViewRU.as_view(), name='select_place_booking_table_view_ru'),
    path('ru/booking_table/select_quantity_of_people/', SelectQuantityOfPeopleBookingTableViewRU.as_view(), name='select_quantity_of_people_booking_table_view_ru'),
    
    
    path('ru/pickup/', MainPickupViewRU.as_view(), name='events_and_dishes_pickup_view_ru'),
    path('ru/pickup/events/', EventsPickupViewRU.as_view(), name='events_pickup_view_ru'),
    path('ru/pickup/category/<category>/', CategoriesPickupViewRU.as_view(), name='categories_pickup_view_ru'),
    path('ru/pickup/cart/', CartPickupViewRU.as_view(), name='carts_pickup_view_ru'),
    path('ru/pickup/select_time/', SelectTimeForOrderPickupViewRU.as_view(), name='select_time_pickup_view_ru'),
    
    
    path('ru/delivery/', MainDeliveryViewRU.as_view(), name='events_and_dishes_delivery_view_ru'),
    path('ru/delivery/events/', EventsDeliveryViewRU.as_view(), name='events_delivery_view_ru'),
    path('ru/delivery/category/<category>/', CategoriesDeliveryViewRU.as_view(), name='categories_delivery_view_ru'),
    path('ru/delivery/cart/', CartDeliveryViewRU.as_view(), name='carts_delivery_view_ru'),
    path('ru/delivery/get_geolocation/', GetGeolocationDeliveryViewRU.as_view(), name='get_geolocation_delivery_view_ru'),

    
    path('uz/booking_table/', MainBookingTableViewUZ.as_view(), name='events_and_dishes_booking_table_view_uz'),
    path('uz/type_order/', ChooseTypeOrderViewUZ.as_view(), name='choose_type_order_view_uz'),
    path('uz/booking_table/events/', EventsBookingTableViewUZ.as_view(), name='events_booking_table_view_uz'),
    path('uz/booking_table/category/<category>/', CategoriesBookingTableViewUZ.as_view(), name='categories_booking_table_view_uz'),
    path('uz/booking_table/cart/', CartBookingTableViewUZ.as_view(), name='carts_booking_table_view_uz'),
    path('uz/booking_table/select_time/', SelectTimeForOrderBookingTableViewUZ.as_view(), name='select_time_booking_table_view_uz'),
    path('uz/booking_table/select_place/', SelectPlaceForOrderBookingTableViewUZ.as_view(), name='select_place_booking_table_view_uz'),
    path('uz/booking_table/select_quantity_of_people/', SelectQuantityOfPeopleBookingTableViewUZ.as_view(), name='select_quantity_of_people_booking_table_view_uz'),

    path('uz/pickup/', MainPickupViewUZ.as_view(), name='events_and_dishes_pickup_view_uz'),
    path('uz/pickup/events/', EventsPickupViewUZ.as_view(), name='events_pickup_view_uz'),
    path('uz/pickup/category/<category>/', CategoriesPickupViewUZ.as_view(), name='categories_pickup_view_uz'),
    path('uz/pickup/cart/', CartPickupViewUZ.as_view(), name='carts_pickup_view_uz'),
    path('uz/pickup/select_time/', SelectTimeForOrderPickupViewUZ.as_view(), name='select_time_pickup_view_uz'),
    

    path('uz/delivery/', MainDeliveryViewUZ.as_view(), name='events_and_dishes_delivery_view_uz'),
    path('uz/delivery/events/', EventsDeliveryViewUZ.as_view(), name='events_delivery_view_uz'),
    path('uz/delivery/category/<category>/', CategoriesDeliveryViewUZ.as_view(), name='categories_delivery_view_uz'),
    path('uz/delivery/cart/', CartDeliveryViewUZ.as_view(), name='carts_delivery_view_uz'),
    path('uz/delivery/get_geolocation/', GetGeolocationDeliveryViewUZ.as_view(), name='get_geolocation_delivery_view_uz'),
]