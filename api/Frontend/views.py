import jwt
from django.conf import settings
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

    def get(self, request, token):
        token_user: dict = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        
        user: int = token_user.get('id')
        
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
            'token': token,
            'user': user
        })


class CategoriesView(APIView):
    """
    View for categories
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/index.html'

    def get(self, request, token, category):
        token_user: dict = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        
        user: int = token_user.get('id')
        
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
            'token': token,
            'user': user
        })

class CartView(APIView):
    """
    View for cart
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/cart.html'

    def get(self, request, token):  
        token_user: dict = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        
        user: int = token_user.get('id')
        
        carts = Carts.objects.filter(
            user=user
        )       
        
        carts_serializer = CartsSerializer(carts, many=True)
        
        total_price_all_cart_user: int = 0  
        
        for cart in carts:
            total_price_all_cart_user += cart.get_total_price()
        
        return Response({
            'carts': carts_serializer.data,
            'token': token,
            'user': user,
            'total_price_all_cart_user': total_price_all_cart_user
        })


class SelectTimeForOrderView(APIView):
    """
    Select DateTime for order
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/select_time.html'

    def get(self, request, token):  
        return Response({
            'token': token,
        })


class SelectTableForOrderView(APIView):
    """
    Select Table for order
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'frontend/select_table.html'

    def get(self, request, token):  
        return Response({
            'token': token,
        })

