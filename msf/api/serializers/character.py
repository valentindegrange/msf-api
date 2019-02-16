# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer
from character.models import Character


class CharacterSerializer(ModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'gear_tiers', 'available', 'traits')
