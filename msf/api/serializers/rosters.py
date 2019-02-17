# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from roster.models import Roster


class RosterSerializer(ModelSerializer):
    user_id = serializers.CharField(source='user.id', read_only=True)
    
    class Meta:
        model = Roster
        fields = ('shareable', 'id', 'user_id')
        read_only_fields = ('id', 'user_id')
