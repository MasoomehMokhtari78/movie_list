# Generated by Django 3.2.5 on 2021-08-07 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='savedMovies',
            field=models.JSONField(),
        ),
    ]
