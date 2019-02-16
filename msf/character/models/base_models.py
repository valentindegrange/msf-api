from django.db import models
from django.db.models import CharField, ManyToManyField, BooleanField, TextField
from django.forms import IntegerField
from character.constants import GEAR_STATISTICS, TRAIT_TYPES


class MaterialBonus(models.Model):
    name = CharField(choices=GEAR_STATISTICS, max_length=64)
    value = IntegerField()

    def __str__(self):
        return f"{self.name}: +{self.value}"


class Material(models.Model):
    name = CharField(max_length=64, unique=True)
    components = ManyToManyField("self", blank=True, related_name="materials")
    cost = IntegerField()
    material_bonuses = ManyToManyField(MaterialBonus, related_name="materials")


class GearTier(models.Model):
    level = IntegerField(min_value=1, max_value=13)
    materials = ManyToManyField(Material, related_name="gear_tiers")


class Trait(models.Model):
    name = CharField(max_length=64, unique=True)
    trait_type = CharField(max_length=64, choices=TRAIT_TYPES)


class Character(models.Model):
    name = CharField(max_length=64, unique=True)
    # character_types = ManyToManyField(CharacterType)
    gear_tiers = ManyToManyField(GearTier, blank=True)
    available = BooleanField(default=True)
    traits = ManyToManyField(Trait, blank=True)
    description = TextField(blank=True)

    def __str__(self):
        return self.name

