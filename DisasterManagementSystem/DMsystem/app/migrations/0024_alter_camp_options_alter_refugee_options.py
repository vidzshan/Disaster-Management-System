# Generated by Django 4.2.6 on 2024-01-25 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_alter_refugee_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='camp',
            options={'permissions': [('generate_camp_pdf', 'Can print camp')]},
        ),
        migrations.AlterModelOptions(
            name='refugee',
            options={'permissions': [('print_refugee', 'Can print refugee')]},
        ),
    ]
