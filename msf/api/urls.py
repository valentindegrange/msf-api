# -*- coding: utf-8 -*-
from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import (
    CharacterViewSet,
    CharacterInstanceViewSet,
    CurrentUserRosterView,
    SharedRosterView)

app_name = 'api'

router = DefaultRouter()
router.register(r'characters', CharacterViewSet, basename='character')
router.register(r'character-instances', CharacterInstanceViewSet, basename='character-instance')

urlpatterns = [
    path('roster', CurrentUserRosterView.as_view(), name="current_roster"),
    path('roster/<slug:user_id>', SharedRosterView.as_view(), name="shared_roster")
]

urlpatterns += router.urls
