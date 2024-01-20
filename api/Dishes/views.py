from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer

from Dishes.models import Dishes
from Dishes.serializers import DishesSerializer


class DishesView(APIView):
    """
    Dishes View
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'dishes.html'
    model = Dishes

    def get(self, request):
        queryset = self.model.objects.all()
        return Response({'dishes': queryset})

class GetDishesAPIView(APIView):
    """
    Get Dishes
    """
    serializer_class = DishesSerializer
    model = Dishes

    def get(self, request):
        categories = self.model.objects.all()
        serializer = self.serializer_class(categories, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)