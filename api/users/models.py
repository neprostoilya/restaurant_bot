import jwt
from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserProfileManager(BaseUserManager):
    """
    Defines user creation fields and manages to save user
    """

    def create_user(self, username, phone, telegram_pk, language, password=None):
        user = self.model(
            username=username,
            phone=phone,
            telegram_pk=telegram_pk,
            language=language
        )
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_staffuser(self, username, phone, telegram_pk, language, password=None):
        user = self.create_user(
            username=username,
            phone=phone,
            telegram_pk=telegram_pk,
            password=password,
            language=language
        )

        user.is_staff = True

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, username, phone, telegram_pk, language, password=None):
        user = self.create_user(
            username=username,
            phone=phone,
            telegram_pk=telegram_pk,
            password=password,
            language=language
        )

        user.set_password(password)

        user.is_staff = True

        user.is_admin = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Creates a customized database table for user using customized user manager
    """
    username = models.CharField(
        verbose_name='Имя',
        unique=True,
        max_length=150,
    )
    phone = models.CharField(
        verbose_name='Номер',
        max_length=15,
    )
    telegram_pk = models.CharField(
        verbose_name='Телеграмм ID',
        max_length=20,
        unique=True,
    )
    language = models.CharField(
        verbose_name='Язык'
    )
    is_active = models.BooleanField(
        default=True
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_admin = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['phone', 'telegram_pk', 'language']

    objects = UserProfileManager()

    def str(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def token(self):
        return self.generate_jwt_token()
        
    def generate_jwt_token(self):
        expiration_time = datetime.now() + timedelta(days=45)

        exp_time_int = int(expiration_time.timestamp())
        
        token_payload = {
            'id': str(self.pk),
            'exp': exp_time_int
        }
        
        token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm='HS256')
        
        return token