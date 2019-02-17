# -*- coding: utf-8 -*-
from django.db import transaction

from character.models import Character, Trait, Material
import json


@transaction.atomic
def run():
    with open('data/data.json', 'r') as data_file:
        character_data = json.load(data_file)

    traits_created = build_traits(character_data['traits'])
    print('Traits:')
    print(traits_created)
    characters_created = build_characters(character_data['characters'])
    print('Characters:')
    print(characters_created)
    materials_created = build_base_materials(character_data['base_materials'])
    print('Materials:')
    print(materials_created)


def build_traits(traits_dict):
    results = dict(created=dict(traits=list(), count=0),
                   updated=dict(traits=list(), count=0))
    for trait_type, trait_names in traits_dict.items():
        for name in trait_names:
            trait, created = Trait.objects.update_or_create(name=name, trait_type=trait_type)

            if created is True:
                results['created']['traits'].append(trait)
                results['created']['count'] += 1
            else:
                results['updated']['traits'].append(trait)
                results['updated']['count'] += 1
    return results


def build_characters(characters_dict):
    results = dict(created=dict(characters=list(), count=0),
                   updated=dict(characters=list(), count=0))
    for char_name, char_values in characters_dict.items():
        # parse traits names into objects
        traits = list()
        for trait in char_values.pop('traits'):
            traits.append(Trait.objects.get(name=trait))

        char, created = Character.objects.update_or_create(name=char_name, defaults=char_values)
        char.traits.set(traits)
        if created is True:
            results['created']['characters'].append(char)
            results['created']['count'] += 1
        # the character has been updated
        else:
            results['updated']['characters'].append(char)
            results['updated']['count'] += 1
    return results


def build_base_materials(base_materials_dict):
    results = dict(created=dict(materials=list(), count=0),
                   updated=dict(materials=list(), count=0))

    for material_color, materials in base_materials_dict.items():
        for material_name in materials:
            material, created = Material.objects.update_or_create(name=material_name, color=material_color)

            if created is True:
                results['created']['materials'].append(material)
                results['created']['count'] += 1
            # the character has been updated
            else:
                results['updated']['materials'].append(material)
                results['updated']['count'] += 1
    return results

