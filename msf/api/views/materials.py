# -*- coding: utf-8 -*-
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from api.serializers import (
    MaterialSerializer,
)
from character.models import Material


class MaterialViewSet(ReadOnlyModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
