from rest_framework import serializers
from Users.models import UserProfile
from Users.logics.logic import authenticate

class UsersSerializer(serializers.ModelSerializer):
    """
    Get Users
    """
    class Meta:
        model = UserProfile
        fields = ('name', 'surname', 'phone')

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
    phone = serializers.CharField(
        max_length=15,
    )

    def create(self, validated_data):
        name = validated_data['name']
        surname = validated_data['surname']
        phone = validated_data['phone']
        user = UserProfile.objects.create_user(
            name=name,
            surname=surname,
            phone=phone,
        )
        return user
    
    class Meta:
        model = UserProfile
        fields = ('name', 'surname', 'phone', 'token')

class LoginSerializer(serializers.Serializer):
    """
    Login User
    """
    phone = serializers.CharField(
        max_length=20, 
    )
    token = serializers.CharField(
        read_only=True
    )

    def validate(self, attrs):
        phone = attrs.get('phone')
        if phone:
            user = authenticate(
                telegram_pk=phone
            )
            if user:
                print(user)
                return {
                    'name': user.name,
                    'surname': user.surname,
                    'phone': user.phone,
                    'token': user.token
                }
            raise serializers.ValidationError('User Not Found')
        raise serializers.ValidationError('You didnt fill in the field')
