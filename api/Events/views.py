from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_or_erorr

from Events.models import Events
from Events.serializers import EventsSerializer

class GetEventsAPIView(APIView):
    """
    Get Events
    """
    serializer_class = EventsSerializer
    model = Events

    def get(self, request):
        orders = self.model.objects.all()
        if orders.exists():
            serializer = self.serializer_class(orders, many=True)
            serialized_data = serializer.data
            return Response(data=serialized_data, status=status_or_erorr.HTTP_200_OK)
        else:
            return Response(status=status_or_erorr.HTTP_404_NOT_FOUND)