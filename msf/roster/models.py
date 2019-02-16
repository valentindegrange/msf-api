from django.db import models
from django.db.models import CASCADE, OneToOneField, ForeignKey, ManyToManyField, IntegerField, \
    BooleanField

from msf_user.models import User
from character.models import Character, Material


class Roster(models.Model):
    user = OneToOneField(User, on_delete=CASCADE)


class CharacterInstance(models.Model):
    roster = ForeignKey(Roster, on_delete=CASCADE)
    character = ForeignKey(Character, on_delete=CASCADE)
    level = IntegerField(default=1)
    stars = IntegerField(default=1)
    red_stars = IntegerField(default=1)
    gear_tier_level = IntegerField(default=1)
    current_gear_materials = ManyToManyField(
        Material,
        blank=True
    )
    unlocked = BooleanField(default=False)

    class Meta:
        ordering = ['character__name']
        unique_together = ('character', 'roster')

