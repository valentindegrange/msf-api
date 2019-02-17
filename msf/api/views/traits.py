# -*- coding: utf-8 -*-
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import (
    TraitSerializer,
)
from character.models import Trait


class TraitViewSet(ReadOnlyModelViewSet):
    queryset = Trait.objects.all()
    serializer_class = TraitSerializer
