# -*- coding: utf-8 -*-
from django.db import transaction

from character.models import Character
import json


@transaction.atomic
def run():
    with open('data/data.json', 'r') as data_file:
        character_data = json.load(data_file)

    characters_created = build_characters(character_data['characters'])
    print(characters_created)


def build_characters(character_dict):
    results = dict(created=dict(characters=list(), count=0),
                   updated=dict(characters=list(), count=0))
    for char_name, char_values in character_dict.items():
        char, created = Character.objects.update_or_create(name=char_name, defaults=char_values)
        if created is True:
            results['created']['characters'].append(char)
            results['created']['count'] += 1
        # the character has been updated
        else:
            results['updated']['characters'].append(char)
            results['updated']['count'] += 1
    return results
