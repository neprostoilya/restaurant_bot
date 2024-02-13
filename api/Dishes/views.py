from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dishes.models import Dishes
from dishes.serializers import DishesSerializer


class GetDishesByCategoryAPIView(APIView):
    """
    Get Dishes by category
    """
    serializer_class = DishesSerializer
    model = Dishes

    def get(self, request, category):
        dishes = self.model.objects.filter(
            category=category
        )
        serializer = self.serializer_class(dishes, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class GetDishByIdAPIView(APIView):
    """
    Get Dish by id(pk)
    """
    serializer_class = DishesSerializer
    model = Dishes

    def get(self, request, pk):
        dish = self.model.objects.filter(
            pk=pk
        )
        serializer = self.serializer_class(dish, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)