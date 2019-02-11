from django.db import models
from django.db.models import CASCADE, OneToOneField, ForeignKey, ManyToManyField
from django.forms import IntegerField

from msf_user.models import User
from character.models import Character, Material


class Roster(models.Model):
    user = OneToOneField(User, on_delete=CASCADE)


class CharacterInstance(models.Model):
    roster = OneToOneField(Roster, on_delete=CASCADE)
    character = ForeignKey(Character, on_delete=CASCADE)
    level = IntegerField(
        min_value=1,
        max_value=70
    )
    stars = IntegerField(
        min_value=1,
        max_value=7
    )
    red_stars = IntegerField(
        min_value=1,
        max_value=7
    )
    gear_tier_level = IntegerField(
        min_value=1,
        max_value=13
    )
    current_gear_materials = ManyToManyField(
        Material
    )

