from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer

from Categories.models import Categories, Subategories
from Categories.serializers import CategoriesSerializer, SubategoriesSerializer


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
    
class GetSubcategoriesAPIView(APIView):
    """
    Get Subategories
    """
    serializer_class = SubategoriesSerializer
    model = Subategories

    def get(self, request):
        categories = self.model.objects.all()
        serializer = self.serializer_class(categories, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)