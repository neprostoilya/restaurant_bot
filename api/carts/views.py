from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Carts
from .serializers import CartsSerializer

from dishes.models import Dishes

class GetCartByUserAPIView(APIView):
    """
    Get Cart by user
    """
    serializer_class = CartsSerializer
    model = Carts

    def get(self, request, user):
        cart = self.model.objects.filter(
            user=user
        )
        serializer = self.serializer_class(cart, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class CreateCartAPIView(APIView):
    """
    Create cart
    """
    serializer_class = CartsSerializer
    model = Carts

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = request.user
            dish_data = serializer.validated_data['dish']
            quantity = serializer.validated_data['quantity']
            dish = Dishes.objects.get(pk=dish_data.id)
            Carts.update_or_create_cart_item(user=user, dish=dish, quantity=quantity)
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)