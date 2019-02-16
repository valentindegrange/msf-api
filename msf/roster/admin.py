from django.contrib import admin

# Register your models here.
from .models import Roster, CharacterInstance

admin.site.register(Roster)
admin.site.register(CharacterInstance)
