# Generated by Django 3.1.4 on 2021-02-14 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('director', models.CharField(blank=True, max_length=100, null=True)),
                ('genre', models.CharField(blank=True, max_length=10, null=True)),
                ('plot', models.CharField(blank=True, max_length=4000, null=True)),
                ('actors', models.CharField(blank=True, max_length=4000, null=True)),
                ('language', models.CharField(blank=True, max_length=20, null=True)),
                ('poster', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
