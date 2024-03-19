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
        print(serializer.errors)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

