
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


from events.models import Events
from events.serializers import EventsSerializer

from dishes.models import Dishes
from dishes.serializers import DishesSerializer

from categories.models import Categories
from categories.serializers import CategoriesSerializer

from places.models import Places
from places.serializers import PlacesSerializer


class ChooseLanguageView(APIView):
    """
    Choose Language View
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/choose_language.html'

    def get(self, request):
        return Response()


class ChooseTypeOrderViewRU(APIView):
    """
    Choose Type Order View RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/choose_type_order.html'

    def get(self, request):
        return Response()


class ChooseTypeOrderViewUZ(APIView):
    """
    Choose Type Order View UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/choose_type_order.html'

    def get(self, request):
        return Response()


# RU


# Booking Table with food



class MainBookingTableViewRU(APIView):
    """
    View Dishes RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/booking_table/index.html'

    def get(self, request):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        dishes = Dishes.objects.all()
        dishes_serializer = DishesSerializer(dishes, many=True)

        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer(categories, many=True)

        return Response({
            'events': events_serializer.data,
            'dishes': dishes_serializer.data,
            'categories': categories_serializer.data,
        })


class EventsBookingTableViewRU(APIView):
    """
    View for Events 
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/booking_table/events.html'

    def get(self, request):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        return Response({
            'events': events_serializer.data,
        })


class CategoriesBookingTableViewRU(APIView):
    """
    View for categories RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/booking_table/index.html'

    def get(self, request, category):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        dishes = Dishes.objects.filter(
            category=category
        )
        dishes_serializer = DishesSerializer(dishes, many=True)

        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer(categories, many=True)

        return Response({
            'events': events_serializer.data,
            'dishes': dishes_serializer.data,
            'categories': categories_serializer.data,
        })


class SelectTimeForOrderBookingTableViewRU(APIView):
    """
    Select DateTime for order RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/booking_table/select_time.html'

    def get(self, request):  
        return Response({})


class SelectPlaceForOrderBookingTableViewRU(APIView):
    """
    Select Place for order RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/booking_table/select_place.html'

    def get(self, request):  
        places = Places.objects.filter(
            is_view=True
        )
        places_serializer = PlacesSerializer(places, many=True)

        return Response({
            'places': places_serializer.data,
        })
        

class CartBookingTableViewRU(APIView):
    """
    Cart view RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/booking_table/cart.html'

    def get(self, request):  
        return Response({})
 

class SelectQuantityOfPeopleBookingTableViewRU(APIView):
    """
    Select quantity of people for order RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/booking_table/select_quantity_of_people.html'

    def get(self, request):  
        return Response({})


# Pickup


class MainPickupViewRU(APIView):
    """
    View Dishes RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/pickup/index.html'

    def get(self, request):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        dishes = Dishes.objects.all()
        dishes_serializer = DishesSerializer(dishes, many=True)

        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer(categories, many=True)

        return Response({
            'events': events_serializer.data,
            'dishes': dishes_serializer.data,
            'categories': categories_serializer.data,
        })


class EventsPickupViewRU(APIView):
    """
    View for Events 
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/pickup/events.html'

    def get(self, request):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        return Response({
            'events': events_serializer.data,
        })


class CategoriesPickupViewRU(APIView):
    """
    View for categories RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/pickup/index.html'

    def get(self, request, category):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        dishes = Dishes.objects.filter(
            category=category
        )
        dishes_serializer = DishesSerializer(dishes, many=True)

        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer(categories, many=True)

        return Response({
            'events': events_serializer.data,
            'dishes': dishes_serializer.data,
            'categories': categories_serializer.data,
        })


class SelectTimeForOrderPickupViewRU(APIView):
    """
    Select DateTime for order RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/pickup/select_time.html'

    def get(self, request):  
        return Response({})


class CartPickupViewRU(APIView):
    """
    Cart view RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/pickup/cart.html'

    def get(self, request):  
        return Response({})


# Delivery


class MainDeliveryViewRU(APIView):
    """
    View Dishes RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/delivery/index.html'

    def get(self, request):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        dishes = Dishes.objects.all()
        dishes_serializer = DishesSerializer(dishes, many=True)

        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer(categories, many=True)

        return Response({
            'events': events_serializer.data,
            'dishes': dishes_serializer.data,
            'categories': categories_serializer.data,
        })


class EventsDeliveryViewRU(APIView):
    """
    View for Events 
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/delivery/events.html'

    def get(self, request):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        return Response({
            'events': events_serializer.data,
        })


class CategoriesDeliveryViewRU(APIView):
    """
    View for categories RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/delivery/index.html'

    def get(self, request, category):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        dishes = Dishes.objects.filter(
            category=category
        )
        dishes_serializer = DishesSerializer(dishes, many=True)

        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer(categories, many=True)

        return Response({
            'events': events_serializer.data,
            'dishes': dishes_serializer.data,
            'categories': categories_serializer.data,
        })


class GetGeolocationDeliveryViewRU(APIView):
    """
    Select DateTime for order RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/delivery/get_geolocation.html'

    def get(self, request):  
        return Response({})


class CartDeliveryViewRU(APIView):
    """
    Cart view RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/delivery/cart.html'

    def get(self, request):  
        return Response({})


# Uz


# Booking Table with food



class MainBookingTableViewUZ(APIView):
    """
    View Dishes UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/booking_table/index.html'

    def get(self, request):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        dishes = Dishes.objects.all()
        dishes_serializer = DishesSerializer(dishes, many=True)

        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer(categories, many=True)

        return Response({
            'events': events_serializer.data,
            'dishes': dishes_serializer.data,
            'categories': categories_serializer.data,
        })


class EventsBookingTableViewUZ(APIView):
    """
    View for Events 
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/booking_table/events.html'

    def get(self, request):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        return Response({
            'events': events_serializer.data,
        })


class CategoriesBookingTableViewUZ(APIView):
    """
    View for categories UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/booking_table/index.html'

    def get(self, request, category):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        dishes = Dishes.objects.filter(
            category=category
        )
        dishes_serializer = DishesSerializer(dishes, many=True)

        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer(categories, many=True)

        return Response({
            'events': events_serializer.data,
            'dishes': dishes_serializer.data,
            'categories': categories_serializer.data,
        })


class SelectTimeForOrderBookingTableViewUZ(APIView):
    """
    Select DateTime for order UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/booking_table/select_time.html'

    def get(self, request):  
        return Response({})


class SelectPlaceForOrderBookingTableViewUZ(APIView):
    """
    Select Place for order UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/booking_table/select_place.html'

    def get(self, request):  
        places = Places.objects.filter(
            is_view=True
        )
        places_serializer = PlacesSerializer(places, many=True)

        return Response({
            'places': places_serializer.data,
        })
        

class CartBookingTableViewUZ(APIView):
    """
    Cart view UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/booking_table/cart.html'

    def get(self, request):  
        return Response({})


class SelectQuantityOfPeopleBookingTableViewUZ(APIView):
    """
    Select quantity of people for order UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/booking_table/select_quantity_of_people.html'

    def get(self, request):  
        return Response({})


# Pickup


class MainPickupViewUZ(APIView):
    """
    View Dishes UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/pickup/index.html'

    def get(self, request):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        dishes = Dishes.objects.all()
        dishes_serializer = DishesSerializer(dishes, many=True)

        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer(categories, many=True)

        return Response({
            'events': events_serializer.data,
            'dishes': dishes_serializer.data,
            'categories': categories_serializer.data,
        })


class EventsPickupViewUZ(APIView):
    """
    View for Events 
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/pickup/events.html'

    def get(self, request):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        return Response({
            'events': events_serializer.data,
        })


class CategoriesPickupViewUZ(APIView):
    """
    View for categories UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/pickup/index.html'

    def get(self, request, category):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        dishes = Dishes.objects.filter(
            category=category
        )
        dishes_serializer = DishesSerializer(dishes, many=True)

        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer(categories, many=True)

        return Response({
            'events': events_serializer.data,
            'dishes': dishes_serializer.data,
            'categories': categories_serializer.data,
        })


class SelectTimeForOrderPickupViewUZ(APIView):
    """
    Select DateTime for order UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/pickup/select_time.html'

    def get(self, request):  
        return Response({})


class CartPickupViewUZ(APIView):
    """
    Cart view UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/pickup/cart.html'

    def get(self, request):  
        return Response({})


# Delivery


class MainDeliveryViewUZ(APIView):
    """
    View Dishes UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/delivery/index.html'

    def get(self, request):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        dishes = Dishes.objects.all()
        dishes_serializer = DishesSerializer(dishes, many=True)

        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer(categories, many=True)

        return Response({
            'events': events_serializer.data,
            'dishes': dishes_serializer.data,
            'categories': categories_serializer.data,
        })


class EventsDeliveryViewUZ(APIView):
    """
    View for Events 
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/delivery/events.html'

    def get(self, request):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        return Response({
            'events': events_serializer.data,
        })


class CategoriesDeliveryViewUZ(APIView):
    """
    View for categories UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/delivery/index.html'

    def get(self, request, category):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        dishes = Dishes.objects.filter(
            category=category
        )
        dishes_serializer = DishesSerializer(dishes, many=True)

        categories = Categories.objects.all()
        categories_serializer = CategoriesSerializer(categories, many=True)

        return Response({
            'events': events_serializer.data,
            'dishes': dishes_serializer.data,
            'categories': categories_serializer.data,
        })


class GetGeolocationDeliveryViewUZ(APIView):
    """
    Select DateTime for order UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/delivery/get_geolocation.html'

    def get(self, request):  
        return Response({})


class CartDeliveryViewUZ(APIView):
    """
    Cart view UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/delivery/cart.html'

    def get(self, request):  
        return Response({})

