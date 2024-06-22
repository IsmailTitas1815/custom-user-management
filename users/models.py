from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid
from enum import Enum

class UserType(Enum):
    MANAGER = 'manager'
    CUSTOMER = 'customer'

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.authentication_token = uuid.uuid4().hex[:16]
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', UserType.MANAGER.value)

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=50, choices=UserType.choices(), default=UserType.CUSTOMER.value)
    authentication_token = models.CharField(max_length=16, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):
        if not self.authentication_token:
            self.authentication_token = uuid.uuid4().hex[:16]
        super().save(*args, **kwargs)


class RequestLog(models.Model):
    username = models.CharField(max_length=150)
    path = models.CharField(max_length=200)
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField()