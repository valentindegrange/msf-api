# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from character.models import Trait


class TraitSerializer(HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='api:trait-detail')

    class Meta:
        model = Trait
        fields = ('id', 'name', 'trait_type', 'url')
