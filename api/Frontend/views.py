from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from events.models import Events
from events.serializers import EventsSerializer

from dishes.models import Dishes
from dishes.serializers import DishesSerializer

from categories.models import Categories
from categories.serializers import CategoriesSerializer

from carts.models import Carts
from carts.serializers import CartsSerializer

class MainView(APIView):
    """
    View for Events and Dishes
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/index.html'

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
            'user': request.user
        })


class CategoriesView(APIView):
    """
    View for categories
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/index.html'

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
            'user': request.user
        })

class CartView(APIView):
    """
    View for cart
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/cart.html'

    def get(self, request):
        carts = Carts.objects.filter(
            user=request.user
        )       
        carts_serializer = CartsSerializer(carts, many=True)

        return Response({
            'carts': carts_serializer.data
        })

