
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


from events.models import Events
from events.serializers import EventsSerializer

from dishes.models import Dishes
from dishes.serializers import DishesSerializer

from categories.models import Categories
from categories.serializers import CategoriesSerializer

from tables.models import Tables
from tables.serializers import TablesSerializer


class ChooseLanguageView(APIView):
    """
    Choose Language View
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/choose_language.html'

    def get(self, request):
        return Response()


class MainViewRU(APIView):
    """
    View Dishes RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/index.html'

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


class EventsViewRU(APIView):
    """
    View for Events 
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/events.html'

    def get(self, request):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        return Response({
            'events': events_serializer.data,
        })


class CategoriesViewRU(APIView):
    """
    View for categories RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/index.html'

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

class SelectTimeForOrderViewRU(APIView):
    """
    Select DateTime for order RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/select_time.html'

    def get(self, request):  
        return Response({})


class SelectTableForOrderViewRU(APIView):
    """
    Select Table for order RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/select_table.html'

    def get(self, request):  
        tables = Tables.objects.all()
        tables_serializer = TablesSerializer(tables, many=True)
        
        return Response({
            'tables': tables_serializer.data
        })
        

class CartViewRU(APIView):
    """
    Cart view RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/cart.html'

    def get(self, request):  
        return Response({})
 

class SelectQuantityOfPeopleForOrderViewRU(APIView):
    """
    Select quantity of people for order RU
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/ru/select_quantity_of_people.html'

    def get(self, request):  
        return Response({})


class MainViewUZ(APIView):
    """
    View for Events and Dishes UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/index.html'

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


class EventsViewUZ(APIView):
    """
    View for Events UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/events.html'

    def get(self, request):
        events = Events.objects.all()
        events_serializer = EventsSerializer(events, many=True)

        return Response({
            'events': events_serializer.data,
        })


class CategoriesViewUZ(APIView):
    """
    View for categories UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/index.html'

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

class SelectTimeForOrderViewUZ(APIView):
    """
    Select DateTime for order UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/select_time.html'

    def get(self, request):  
        return Response({})


class SelectTableForOrderViewUZ(APIView):
    """
    Select Table for order UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/select_table.html'

    def get(self, request):  
        tables = Tables.objects.all()
        tables_serializer = TablesSerializer(tables, many=True)
        
        return Response({
            'tables': tables_serializer.data
        })


class CartViewUZ(APIView):
    """
    Cart view UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/cart.html'

    def get(self, request):  
        return Response({})
 

class SelectQuantityOfPeopleForOrderViewUZ(APIView):
    """
    Select quantity of people for order UZ
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/uz/select_quantity_of_people.html'

    def get(self, request):  
        return Response({})