# Generated by Django 2.1.5 on 2019-02-16 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0006_auto_20190216_2234'),
        ('roster', '0003_auto_20190216_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterinstance',
            name='roster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roster.Roster'),
        ),
        migrations.AlterUniqueTogether(
            name='characterinstance',
            unique_together={('character', 'roster')},
        ),
    ]
