from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from Users.models import UserProfile
from Users.serializers import RegistrationSerializer, LoginSerializer, \
    UsersSerializer

class GetUsersAPIView(APIView):
    """
    Get Users
    """
    serializer_class = UsersSerializer
    model = UserProfile

    def get(self, request):
        users = self.model.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

class RegisterAPIView(APIView):
    """
    Create User
    """
    serializer_class = RegistrationSerializer
    model = UserProfile

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.error_messages)
    
class LoginAPIView(APIView):
    """
    Create User
    """
    serializer_class = LoginSerializer
    model = UserProfile

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_201_CREATED, data=serializer.validated_data)
        return Response(status=status.HTTP_400_BAD_REQUEST)