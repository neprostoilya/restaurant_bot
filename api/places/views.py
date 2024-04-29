from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Places
from .serializers import PlacesSerializer


class GetPlacesAPIView(APIView):
    """
    Get Places
    """
    serializer_class = PlacesSerializer
    model = Places

    def get(self, request):
        places = self.model.objects.all()
        if places.exists():
            serializer = self.serializer_class(places, many=True)
            serialized_data = serializer.data
            return Response(data=serialized_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class GetReservedPlacesAPIView(APIView):
    """
    Get Reserved Places
    """
    serializer_class = PlacesSerializer
    model = Places

    def get(self, request):
        places = self.model.objects.filter(
            is_view=True
        )
        if places.exists():
            serializer = self.serializer_class(places, many=True)
            serialized_data = serializer.data
            return Response(data=serialized_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UpdatePlaceStatusAPIView(APIView):
    """
    Update place Status
    """
    serializer_class = PlacesSerializer
    model = Places

    def put(self, request, place_id):
        data = request.data
        
        try:
            place = self.model.objects.get(pk=place_id)
            
            place.is_view = data.get('is_view')
            
            place.save()
            
            serializer = self.serializer_class(place)
            
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(data={'error': 'Место не найдено'}, status=status.HTTP_404_NOT_FOUND)

            