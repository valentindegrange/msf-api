# -*- coding: utf-8 -*-
from character.models import Character, Trait, Material
import json


def run():
    data = dict(
        traits=dict(),
        characters=dict(),
        base_materials=dict()
    )

    data['characters'] = export_characters()
    data['base_materials'] = export_materials()
    data['traits'] = export_traits()

    write_into_json(data)


def export_characters():
    characters = dict()
    for character in Character.objects.all():
        characters[character.name] = dict(
            available=character.available,
            traits=[trait.name for trait in character.traits.all()]
        )
    return characters


def export_materials():
    materials = dict()
    for material in Material.objects.all():
        if material.color not in materials:
            materials[material.color] = [material.name]
        else:

            materials[material.color].append(material.name)
    return materials


def export_traits():
    traits = dict()
    for trait in Trait.objects.all():
        if trait.trait_type not in traits:
            traits[trait.trait_type] = [trait.name]
        else:
            traits[trait.trait_type].append(trait.name)
    return traits


def write_into_json(data):
    with open('msf/data/exported_data.json', 'w') as file:
        json.dump(data, file)
