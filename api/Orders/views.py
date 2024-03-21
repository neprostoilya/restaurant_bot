from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Orders
from .serializers import OrdersSerializer


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
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetOrdersByUserAPIView(APIView):
    """
    Create Order
    """
    serializer_class = OrdersSerializer
    model = Orders

    def get(self, request, user):
        orders = self.model.objects.filter(
            user=user
        )
        
        if orders.exists():
            serializer = self.serializer_class(orders, many=True)
            serialized_data = serializer.data
            return Response(data=serialized_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
