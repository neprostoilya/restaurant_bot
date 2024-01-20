from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer

from Categories.models import Categories
from Categories.serializers import CategoriesSerializer


class CategoriesView(APIView):
    """
    Categories View
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'categories.html'
    model = Categories

    def get(self, request):
        queryset = self.model.objects.all()
        return Response({'categories': queryset})

class GetCategoriesAPIView(APIView):
    """
    Get Categories
    """
    serializer_class = CategoriesSerializer
    model = Categories

    def get(self, request):
        categories = self.model.objects.all()
        serializer = self.serializer_class(categories, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)