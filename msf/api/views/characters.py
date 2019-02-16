# -*- coding: utf-8 -*-
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import CharacterSerializer
from character.models import Character


# list all available characters
class CharacterViewSet(ReadOnlyModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
