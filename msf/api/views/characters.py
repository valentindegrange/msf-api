# -*- coding: utf-8 -*-
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from api.serializers import (
    CharacterSerializer,
    CharacterInstanceSerializer
)
from api.filters import (
    CharacterInstanceFilter
)
from character.models import Character
from roster.models import CharacterInstance


# list all available characters
class CharacterViewSet(ReadOnlyModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterInstanceViewSet(ModelViewSet):

    serializer_class = CharacterInstanceSerializer
    permission_classes = [IsAuthenticated]
    filter_class = CharacterInstanceFilter

    def get_queryset(self):
        current_user = self.request.user
        return CharacterInstance.objects.filter(roster__user=current_user)


