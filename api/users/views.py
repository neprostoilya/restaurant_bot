from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import UserProfile
from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer


class UserAPIView(APIView):
    """
    Get User
    """
    model = UserProfile
    serializer_class = UserSerializer

    def get(self, request, telegram_pk):
        users = self.model.objects.filter(
            telegram_pk=telegram_pk
        )
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)


class RegisterAPIView(APIView):
    """
    Create User
    """
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    """
    Login User
    """
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            return Response(status=status.HTTP_201_CREATED, data=serializer.validated_data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
