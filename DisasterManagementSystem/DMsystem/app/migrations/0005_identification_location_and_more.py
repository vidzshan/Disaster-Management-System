# Generated by Django 4.1.7 on 2023-06-05 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_guidelines_during_disatser_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Identification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('safety_area', models.CharField(max_length=1000)),
                ('risky_area', models.CharField(max_length=1000)),
                ('affected_area', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='guidelines',
            name='during_disaster',
            field=models.TextField(max_length=1050),
        ),
    ]