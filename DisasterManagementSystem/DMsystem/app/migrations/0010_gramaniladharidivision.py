# Generated by Django 4.1.7 on 2023-06-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_divisionalsecretariat'),
    ]

    operations = [
        migrations.CreateModel(
            name='GramaNiladhariDivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
