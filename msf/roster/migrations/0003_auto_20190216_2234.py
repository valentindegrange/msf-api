# Generated by Django 2.1.5 on 2019-02-16 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0002_auto_20190216_2139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characterinstance',
            options={'ordering': ['character__name']},
        ),
        migrations.AddField(
            model_name='characterinstance',
            name='gear_tier_level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='characterinstance',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='characterinstance',
            name='red_stars',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='characterinstance',
            name='stars',
            field=models.IntegerField(default=1),
        ),
    ]
