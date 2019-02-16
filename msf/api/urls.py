# -*- coding: utf-8 -*-

from rest_framework.routers import DefaultRouter
from api.views import CharacterViewSet, CharacterInstanceViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'characters', CharacterViewSet, basename='character')
router.register(r'character-instances', CharacterInstanceViewSet, basename='character-instance')

urlpatterns = router.urls
