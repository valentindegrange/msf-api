# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from character.models import Character
from roster.models import CharacterInstance, Roster
from character.constants import (
    MIN_LEVEL,
    MAX_LEVEL,
    MIN_STARS,
    MAX_STARS,
    MIN_RED_STARS,
    MAX_RED_STARS,
    MIN_GEAR_LEVEL,
    MAX_GEAR_LEVEL,
)


class CharacterSerializer(ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'name', 'gear_tiers', 'available', 'traits')
        read_only_fields = ('id',)


class CharacterInstanceSerializer(ModelSerializer):
    character_name = serializers.CharField(source='character.name', read_only=True)
    level = serializers.IntegerField(min_value=MIN_LEVEL, max_value=MAX_LEVEL)
    stars = serializers.IntegerField(min_value=MIN_STARS, max_value=MAX_STARS)
    red_stars = serializers.IntegerField(min_value=MIN_RED_STARS, max_value=MAX_RED_STARS)
    gear_tier_level = serializers.IntegerField(min_value=MIN_GEAR_LEVEL, max_value=MAX_GEAR_LEVEL)

    class Meta:
        model = CharacterInstance
        fields = (
            'id',
            'character',
            'character_name',
            'level',
            'stars',
            'red_stars',
            'gear_tier_level',
            'unlocked'
        )
        read_only_fields = ('id', 'character_name',)

    def create(self, validated_data):
        current_user = self.context['request'].user
        roster, _ = Roster.objects.get_or_create(user=current_user)
        validated_data['roster'] = roster
        return super().create(validated_data)
