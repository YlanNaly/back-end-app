from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class PersonManager(BaseUserManager):
    def create_person(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        person = self.model(username=username, **extra_fields)
        person.set_password(password)
        person.save(using=self._db)
        return person


class Person(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = PersonManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

