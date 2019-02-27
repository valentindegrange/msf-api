# -*- coding: utf-8 -*-
import operator
from functools import reduce

from django.db.models import Q

from character.models import Trait, Character


def associate_char_list_with_trait(name_list, trait_name):
    trait = Trait.objects.get(name__icontains=trait_name)

    clauses = (Q(name__icontains=name) for name in name_list)
    filters = reduce(operator.or_, clauses)
    updated = list()
    for character in Character.objects.filter(filters):
        character.traits.add(trait)
        updated.append(character)

    return updated


def associate_character_with_trait_list(character_name, trait_list):
    character = Character.objects.get(name__icontains=character_name)
    traits = [trait for trait in Trait.objects.filter(name__in=trait_list)]
    for trait in traits:
        character.traits.add(trait)

    return traits



