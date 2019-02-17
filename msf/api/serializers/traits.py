# -*- coding: utf-8 -*-

from rest_framework.serializers import ModelSerializer

from character.models import Trait


class TraitSerializer(ModelSerializer):

    class Meta:
        model = Trait
        fields = ('id', 'name', 'trait_type')
