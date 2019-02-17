# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from roster.models import Roster


class RosterSerializer(ModelSerializer):

    class Meta:
        model = Roster
        fields = ('shareable', 'id')
        read_only_fields = ('id',)
