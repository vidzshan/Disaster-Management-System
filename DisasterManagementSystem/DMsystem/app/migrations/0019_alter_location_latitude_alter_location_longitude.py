# Generated by Django 4.2.6 on 2024-01-21 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_location_disasters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
