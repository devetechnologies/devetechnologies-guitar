from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    
    def _create_user(self, username, email, name, last_name, phone, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email=email,
            name=name,
            last_name=last_name,
            phone=phone,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name, last_name, phone, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, phone, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name, last_name, phone, password=None, **extra_fields):
        return self._create_user(username, email, name, last_name, phone, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField('Email',
                              max_length=40, unique=True,)
    name = models.CharField('Name', max_length=20, blank=True, null=True)
    last_name = models.CharField(
        'Lastname', max_length=40, blank=True, null=True)
    phone = models.CharField('Phone', max_length=16,
                             blank=True, unique=True)
    '''image = models.ImageField(
        'Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank=True)'''
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name', 'phone']

    def __str__(self):
        return f'{self.username}'
