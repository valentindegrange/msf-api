# -*- coding: utf-8 -*-

from rest_framework.routers import DefaultRouter
from api.views import CharacterViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'characters', CharacterViewSet, basename='character')

urlpatterns = router.urls
