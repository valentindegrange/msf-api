from django.contrib import admin
from .models import (
    MaterialBonus,
    Material,
    GearTier,
    Character,
    Trait
)
admin.site.register(MaterialBonus)
admin.site.register(Material)
admin.site.register(GearTier)
admin.site.register(Character)
admin.site.register(Trait)

# Register your models here.
