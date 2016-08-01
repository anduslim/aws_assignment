# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from aws_assignment.movies import models as movie_models
from .managers import ActorManager

class Actor(models.Model):

    slug = models.SlugField()
    name = models.CharField('Full Name', max_length=150, blank=False)
    dob = models.DateField('Date of Birth', blank=False)
    description = models.CharField('Description', max_length=1000, blank=True)
    image_filename = models.CharField('Slug', max_length=150, blank=True)
    movie = models.ManyToManyField(movie_models.Movie, blank=False, related_name='actor')

    objects = ActorManager()

    def Meta(self):
        ordering = ['slug', 'movie']
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'

    def print_movie_list(self):
        return ', '.join([show.name for show in self.movie.all()])

    print_movie_list.short_description = 'Acted in'

    def save(self, **kwargs):
        self.image_filename = '{}.jpg'.format(self.slug)
        super(Actor, self).save()

    def __str__(self):
        if self.movie != None:
            return ', '.join([self.name, self.description, str(self.movie.name)])
        else:
            return ', '.join([self.name, self.description])
