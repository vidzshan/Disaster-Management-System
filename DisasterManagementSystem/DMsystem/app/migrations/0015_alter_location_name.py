# Generated by Django 4.2 on 2023-08-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_camp_options_alter_locationdisaster_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
