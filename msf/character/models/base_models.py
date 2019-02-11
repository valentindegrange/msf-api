from django.db import models
from django.db.models import CharField, ManyToManyField
from django.forms import IntegerField
from character.constants import GEAR_STATISTICS


class MaterialBonus(models.Model):
    name = CharField(choices=GEAR_STATISTICS, max_length=64)
    value = IntegerField()

    def __str__(self):
        return f"{self.name}: +{self.value}"


class CharacterType(models.Model):
    name = CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = CharField(max_length=64, unique=True)
    components = ManyToManyField("self", blank=True, related_name="materials")
    cost = IntegerField()
    material_bonuses = ManyToManyField(MaterialBonus, related_name="materials")


class GearTier(models.Model):
    level = IntegerField(min_value=1, max_value=13)
    materials = ManyToManyField(Material, related_name="gear_tiers")


class Character(models.Model):
    name = CharField(max_length=64, unique=True)
    character_types = ManyToManyField(CharacterType)
    # Todo: set unique gear_tier per level
    gear_tiers = ManyToManyField(GearTier)
