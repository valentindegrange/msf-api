# -*- coding: utf-8 -*-
from rest_framework_filters import FilterSet
from roster.models import CharacterInstance


class CharacterInstanceFilter(FilterSet):
    class Meta:
        model = CharacterInstance
        fields = {
            'level': ['exact', 'lte', 'gte'],
            'red_stars': ['exact', 'lte', 'gte'],
            'stars': ['exact', 'lte', 'gte'],
            'gear_tier_level': ['exact', 'lte', 'gte'],
            'unlocked': ['exact']
        }
