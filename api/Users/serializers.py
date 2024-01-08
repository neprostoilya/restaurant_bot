from rest_framework import serializers
from Users.models import UserProfile
from Users.logics.logic import authenticate

class UsersSerializer(serializers.ModelSerializer):
    """
    Get Users
    """
    class Meta:
        model = UserProfile
        fields = ('username', 'name', 'surname', 'phone', 'telegram_pk',)

class RegistrationSerializer(serializers.ModelSerializer):
    """
    Registration User
    """
    token = serializers.CharField(
        read_only=True
    )
    name = serializers.CharField(
    )
    surname = serializers.CharField(
    )
    username = serializers.CharField(
        max_length=150,
    )
    phone = serializers.CharField(
        max_length=15,
    )
    telegram_pk = serializers.CharField(
        max_length=20, 
    )

    def create(self, validated_data):
        username = validated_data['username']
        name = validated_data['name']
        surname = validated_data['surname']
        phone = validated_data['phone']
        telegram_pk = validated_data['telegram_pk']
        user = UserProfile.objects.create_user(
            name=name,
            surname=surname,
            username=username,
            phone=phone,
            telegram_pk=telegram_pk
        )
        return user
    
    class Meta:
        model = UserProfile
        fields = ('username', 'name', 'surname', 'phone', 'telegram_pk', 'token')

class LoginSerializer(serializers.Serializer):
    """
    Login User
    """
    telegram_pk = serializers.CharField(
        max_length=20, 
    )
    token = serializers.CharField(
        read_only=True
    )

    def validate(self, attrs):
        telegram_pk = attrs.get('telegram_pk')
        if telegram_pk:
            user = authenticate(
                telegram_pk=telegram_pk
            )
            if user:
                print(user)
                return {
                    'name': user.name,
                    'surname': user.surname,
                    'username': user.username,
                    'phone': user.phone,
                    'telegram_pk': user.telegram_pk,
                    'token': user.token
                }
            raise serializers.ValidationError('User Not Found')
        raise serializers.ValidationError('You didnt fill in the field')
