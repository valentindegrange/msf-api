# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from character.models import Material


class MaterialSerializer(HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='api:material-detail')
    # warning: May break once we had components

    class Meta:
        model = Material
        fields = ('id', 'name', 'components', 'cost', 'color', 'material_bonuses', 'url')
