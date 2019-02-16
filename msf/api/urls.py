# -*- coding: utf-8 -*-

from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import CharacterListViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'characters', CharacterListViewSet, basename='character')

urlpatterns = router.urls
