# Generated by Django 2.1.5 on 2019-02-17 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0008_auto_20190217_0310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'ordering': ['color', 'name']},
        ),
        migrations.AlterModelOptions(
            name='trait',
            options={'ordering': ['trait_type', 'name']},
        ),
    ]
