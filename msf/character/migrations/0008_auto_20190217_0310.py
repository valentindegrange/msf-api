# Generated by Django 2.1.5 on 2019-02-17 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0007_auto_20190216_2305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'ordering': ['color']},
        ),
        migrations.AlterField(
            model_name='material',
            name='color',
            field=models.CharField(choices=[('1', 'Green'), ('2', 'Blue'), ('3', 'Purple'), ('4', 'Orange')], default=('1', 'Green'), max_length=64),
        ),
        migrations.AlterField(
            model_name='material',
            name='material_bonuses',
            field=models.ManyToManyField(blank=True, related_name='materials', to='character.MaterialBonus'),
        ),
    ]