# Generated by Django 4.1.7 on 2023-06-04 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_disaster_guidelines_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guidelines',
            name='during_disatser',
        ),
        migrations.AddField(
            model_name='guidelines',
            name='during_disaster',
            field=models.TextField(default=1050, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='guidelines',
            name='after_disaster',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='guidelines',
            name='before_disaster',
            field=models.TextField(max_length=1000),
        ),
    ]
