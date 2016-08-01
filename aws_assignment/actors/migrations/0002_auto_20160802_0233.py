# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='image_filename',
            field=models.CharField(blank=True, max_length=150, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='actor',
            name='slug',
            field=models.CharField(default='test', max_length=150, verbose_name='Slug'),
            preserve_default=False,
        ),
    ]
