from django.db import models
from django.db.models import CharField, ManyToManyField, BooleanField, TextField, IntegerField
from character.constants import GEAR_STATISTICS, TRAIT_TYPES


class MaterialBonus(models.Model):
    name = CharField(choices=GEAR_STATISTICS, max_length=64)
    value = IntegerField(default=0)

    def __str__(self):
        return f"{self.name}: +{self.value}"


class Material(models.Model):
    GREEN_MATERIAL_COLOR = ('1', 'Green')
    BLUE_MATERIAL_COLOR = ('2', 'Blue')
    PURPLE_MATERIAL_COLOR = ('3', 'Purple')
    ORANGE_MATERIAL_COLOR = ('4', 'Orange')

    MATERIAL_COLORS = (
        GREEN_MATERIAL_COLOR,
        BLUE_MATERIAL_COLOR,
        PURPLE_MATERIAL_COLOR,
        ORANGE_MATERIAL_COLOR
    )
    name = CharField(max_length=64, unique=True)
    components = ManyToManyField("self", blank=True, related_name="materials")
    cost = IntegerField(default=0)
    color = CharField(max_length=64, choices=MATERIAL_COLORS, default=GREEN_MATERIAL_COLOR)
    material_bonuses = ManyToManyField(MaterialBonus, blank=True, related_name="materials")

    class Meta:
        ordering = ['color', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_material_color_string()})"

    def get_material_color_string(self, material_color_id=None):

        if material_color_id is None:
            material_color_id = self.color

        material_color_string = ''

        for material_tuple in self.MATERIAL_COLORS:
            if material_color_id == material_tuple[0]:
                return material_tuple[1]

        return material_color_string


class GearTier(models.Model):
    level = IntegerField(default=1)
    materials = ManyToManyField(Material, related_name="gear_tiers")


class Trait(models.Model):
    name = CharField(max_length=64, unique=True)
    trait_type = CharField(max_length=64, choices=TRAIT_TYPES)

    class Meta:
        ordering = ['trait_type', 'name']

    def __str__(self):
        return self.name


class Character(models.Model):
    name = CharField(max_length=64, unique=True)
    # character_types = ManyToManyField(CharacterType)
    gear_tiers = ManyToManyField(GearTier, blank=True)
    available = BooleanField(default=True)
    traits = ManyToManyField(Trait, blank=True)
    description = TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

