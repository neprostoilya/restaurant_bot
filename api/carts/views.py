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

            new_cart = Carts.objects.filter(user=user, dish=dish).first()
            
            total_price = new_cart.get_total_price()
            
            get_quantity = new_cart.get_quantity()
            
            carts = Carts.objects.filter(
                user=user
            )       
        
            total_price_all_cart_user: int = 0  
        
            for cart in carts:
                total_price_all_cart_user += cart.get_total_price()
            
            return Response({'total_price': total_price, 'get_quantity': get_quantity, 'dish': dish.pk, 'total_price_all_cart_user': total_price_all_cart_user},
                            status=status.HTTP_201_CREATED)
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
            
            user = serializer.validated_data['user']
            
            Carts.objects.filter(pk=cart_pk).delete()
            
            
            carts = Carts.objects.filter(
                user=user
            )       
        
            total_price_all_cart_user: int = 0  
        
            for cart in carts:
                total_price_all_cart_user += cart.get_total_price()
                
            return Response({'total_price_all_cart_user': total_price_all_cart_user}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)