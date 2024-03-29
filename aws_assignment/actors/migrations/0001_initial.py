# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Full Name')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Description')),
                ('movie', models.ManyToManyField(to='movies.Movie')),
            ],
        ),
    ]
