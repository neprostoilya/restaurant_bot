from rest_framework import serializers

from users.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    """
    Get Users
    """

    class Meta:
        model = UserProfile
        fields = ('pk', 'username', 'phone', 'telegram_pk', 'language')


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Registration User
    """
    username = serializers.CharField()
    phone = serializers.CharField(
        min_length=6,
        max_length=13,
    )
    telegram_pk = serializers.CharField(
        max_length=20,
    )

    def create(self, validated_data):
        username = validated_data['username']
        phone = validated_data['phone']
        telegram_pk = validated_data['telegram_pk']
        language = validated_data['language']

        user = UserProfile.objects.create_user(
            username=username,
            phone=phone,
            telegram_pk=telegram_pk,
            language=language
        )
        return user

    class Meta:
        model = UserProfile
        fields = ('username', 'phone', 'telegram_pk', 'token', 'language')


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
            user = UserProfile.objects.filter(
                telegram_pk=telegram_pk
            ).first()

            if user:
                return {
                    'phone': user.phone,
                    'username': user.username,
                    'telegram_pk': user.telegram_pk,
                    'language': user.language,
                    'token': user.token
                }
            raise serializers.ValidationError('User Not Found')
        raise serializers.ValidationError('You didnt fill in the field')
