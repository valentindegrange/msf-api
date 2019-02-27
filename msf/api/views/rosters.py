# -*- coding: utf-8 -*-
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.filters import CharacterInstanceFilter
from api.serializers import RosterSerializer, CharacterInstanceSerializer
from roster.models import Roster, CharacterInstance


class CurrentUserRosterView(UpdateAPIView):
    serializer_class = RosterSerializer

    permission_classes = [IsAuthenticated]

    def get_object(self):
        current_user = self.request.user
        return Roster.objects.get(user=current_user)

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class SharedRosterView(GenericAPIView):

    filter_class = CharacterInstanceFilter

    serializer_class = CharacterInstanceSerializer

    def get_queryset(self):
        user_id = self.request.parser_context['kwargs']['user_id']
        return CharacterInstance.objects.filter(roster__user__id=user_id, roster__shareable=True)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)





