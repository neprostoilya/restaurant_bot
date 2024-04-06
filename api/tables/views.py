from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Tables
from .serializers import TablesSerializer


class GetTablesAPIView(APIView):
    """
    Get Tables
    """
    serializer_class = TablesSerializer
    model = Tables

    def get(self, request):
        events = self.model.objects.all()
        if events.exists():
            serializer = self.serializer_class(events, many=True)
            serialized_data = serializer.data
            return Response(data=serialized_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UpdateTableStatusAPIView(APIView):
    """
    Update Table
    """
    serializer_class = TablesSerializer
    model = Tables

    def put(self, request, table_id):
        data = request.data
        
        try:
            order = self.model.objects.get(pk=table_id)
            
            if 'status' in data:
                order.status = data['status']
                order.save()
                
                serializer = self.serializer_class(order)
                
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data={'error': 'Поле "status" обязательно'}, status=status.HTTP_400_BAD_REQUEST)
            
        except self.model.DoesNotExist:
            return Response(data={'error': 'Стол не найден'}, status=status.HTTP_404_NOT_FOUND)