from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from Events.models import Events
from Events.serializers import EventsSerializer

from Dishes.models import Dishes
from Dishes.serializers import DishesSerializer

from Categories.models import Categories
from Categories.serializers import CategoriesSerializer

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
            'categories': categories_serializer.data
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
            'categories': categories_serializer.data
        })

    