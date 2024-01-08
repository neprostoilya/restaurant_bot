from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_or_erorr

from Orders.models import Orders
from Orders.serializers import OrdersSerializer

class GetOrdersAPIView(APIView):
    """
    Get Orders
    """
    serializer_class = OrdersSerializer
    model = Orders

    def get(self, request):
        orders = self.model.objects.all()
        if orders.exists():
            serializer = self.serializer_class(orders, many=True)
            serialized_data = serializer.data
            return Response(data=serialized_data, status=status_or_erorr.HTTP_200_OK)
        else:
            return Response(status=status_or_erorr.HTTP_404_NOT_FOUND)

class GetOrdersByUserAPIView(APIView):
    """
    Get Orders By User
    """
    serializer_class = OrdersSerializer
    model = Orders

    def get(self, request, user):
        order = self.model.objects.filter(
            user=user, 
        )
        if order.exists():
            serializer = self.serializer_class(order, many=True)
            serialized_data = serializer.data
            return Response(data=serialized_data, status=status_or_erorr.HTTP_200_OK)
        else:
            return Response(status=status_or_erorr.HTTP_404_NOT_FOUND)
        
class CreateOrderAPIView(APIView):
    """
    Create Order
    """
    serializer_class = OrdersSerializer
    model = Orders

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status_or_erorr.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status_or_erorr.HTTP_400_BAD_REQUEST)

    
