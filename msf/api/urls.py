# -*- coding: utf-8 -*-
from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import (
    CharacterViewSet,
    CharacterInstanceViewSet,
    CurrentUserRosterView,
    SharedRosterView,
    MaterialViewSet,
    TraitViewSet,
    CreateUserView)

app_name = 'api'

router = DefaultRouter()
router.register(r'characters', CharacterViewSet, basename='character')
router.register(r'character-instances', CharacterInstanceViewSet, basename='character-instance')
router.register(r'materials', MaterialViewSet, basename='material')
router.register(r'traits', TraitViewSet, basename='trait')

urlpatterns = [
    path('roster', CurrentUserRosterView.as_view(), name="current_roster"),
    path('roster/<slug:user_id>', SharedRosterView.as_view(), name="shared_roster"),
    path('create-user', CreateUserView.as_view(), name="create_user")
]

urlpatterns += router.urls
