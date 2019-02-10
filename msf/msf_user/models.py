from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
from django.db.models import CharField


class User(AbstractBaseUser):
    username = CharField(unique=True, max_length=128)

    USERNAME_FIELD = 'username'

