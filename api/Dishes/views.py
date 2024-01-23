from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Dishes.models import Dishes
from Dishes.serializers import DishesSerializer

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