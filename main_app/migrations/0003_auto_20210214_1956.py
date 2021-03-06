# Generated by Django 3.1.4 on 2021-02-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='language',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='plot',
        ),
        migrations.AddField(
            model_name='movie',
            name='imdbID',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
