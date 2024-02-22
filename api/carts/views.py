from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Carts
from .serializers import CartsSerializer, DeleteCartSerializer

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

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        user = serializer
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            dish_data = serializer.validated_data['dish']
            quantity = serializer.validated_data['quantity']
            dish = Dishes.objects.get(pk=dish_data.pk)
            cart_item = Carts.objects.filter(user=user, dish=dish).first()

            if cart_item:
                cart_item.quantity += quantity
                cart_item.save()
            else:
                cart_item = Carts.objects.create(user=user, dish=dish, quantity=quantity)

            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteCartAPIView(APIView):
    """
    Delete cart
    """
    serializer_class = DeleteCartSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            cart_pk = serializer.validated_data['pk']
            Carts.objects.filter(pk=cart_pk).delete()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)