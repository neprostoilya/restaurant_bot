from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import login, authenticate

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


class UpdateUserAPIView(APIView):
    """
    Update User
    """
    model = UserProfile
    serializer_class = UserSerializer

    def put(self, request, telegram_pk):
        data = request.data
        
        try:
            order = self.model.objects.get(
                telegram_pk=telegram_pk
            )
            
            if 'phone' in data:
                order.phone = data['phone']
                order.save()
                serializer = self.serializer_class(order)
                
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            elif 'language' in data:
                order.language = data['language']
                order.save()
                serializer = self.serializer_class(order)
                
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data={'error': 'Поле "status" обязательно'}, status=status.HTTP_400_BAD_REQUEST)
            
        except self.model.DoesNotExist:
            return Response(data={'error': 'Пользователь не найден не найден'}, status=status.HTTP_404_NOT_FOUND)


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
        
        if serializer.is_valid():
            telegram_pk = serializer.validated_data.get('telegram_pk')
            
            user = UserProfile.objects.filter(telegram_pk=telegram_pk).first()
            
            if user:
                token = user.generate_jwt_token()
                
                response_data = {
                    'pk': user.pk,
                    'phone': user.phone,
                    'username': user.username,
                    'telegram_pk': user.telegram_pk,
                    'language': user.language,
                    'token': token  
                }
                
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserLanguageAPIView(APIView):
    """
    Get User Language
    """
    model = UserProfile
    serializer_class = UserSerializer

    def get(self, request, telegram_pk):
        users = self.model.objects.filter(
            telegram_pk=telegram_pk
        )
        serializer = self.serializer_class(users, many=True)
        return Response(data={'language': serializer.data[0].get('language')})
