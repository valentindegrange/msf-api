from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models import CharField


class User(AbstractUser):
    username = CharField(unique=True, max_length=128)

    USERNAME_FIELD = 'username'

