from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.
from django.db.models import CharField


class MsfUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        user = super().create_user(username, email, password, **extra_fields)
        user.initialize()
        return user


class User(AbstractUser):
    username = CharField(unique=True, max_length=128)

    USERNAME_FIELD = 'username'

    objects = MsfUserManager()

    def initialize(self):
        from roster.models import Roster, CharacterInstance
        from character.models import Character

        roster = Roster.objects.create(user=self, shareable=False)
        for character in Character.objects.filter(available=True):
            CharacterInstance.objects.create(roster=roster, character=character)



