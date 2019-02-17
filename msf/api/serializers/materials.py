# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from character.models import Material


class MaterialSerializer(ModelSerializer):

    class Meta:
        model = Material
        fields = ('id', 'name', 'components', 'cost', 'color', 'material_bonuses')
