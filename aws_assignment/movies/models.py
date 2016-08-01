# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from .managers import MovieManager


class Movie(models.Model):

    slug = models.SlugField()
    name = models.CharField('Movie Name', max_length=150, blank=False)
    date = models.CharField('Production Date', max_length=4, blank=False)
    description = models.CharField('Description', max_length=1000, blank=True)

    objects = MovieManager()

    def Meta(self):
        ordering = ['slug', 'name']
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def save(self, **kwargs):
        self.image_filename = '{}.jpg'.format(self.slug)
        super(Movie, self).save()

    def __str__(self):
        return ', '.join([self.name, self.description])
