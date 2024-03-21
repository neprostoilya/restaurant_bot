from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Events
from .serializers import EventsSerializer


class GetEventsAPIView(APIView):
    """
    Get Events
    """
    serializer_class = EventsSerializer
    model = Events

    def get(self, request):
        events = self.model.objects.all()
        if events.exists():
            serializer = self.serializer_class(events, many=True)
            serialized_data = serializer.data
            return Response(data=serialized_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
