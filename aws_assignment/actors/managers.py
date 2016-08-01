# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from aws_assignment.movies import models as movie_models

class ActorManager(models.Manager):

    def create_actor(self, _slug, _name, _dob, _description, _movie_slug=None):

        if _movie_slug:
            try:
                show = movie_models.Movie.objects.filter(slug=_movie_slug)
            except self.DoesNotExist:
                return 0
            movie = self.create(slug=_slug, name=_name, dob=_dob,
                            description=_description, movie=show[0])
        else:
            movie = self.create(slug=_slug, name=_name, dob=_dob,
                                description=_description)

        return movie

    def update_actor_movie(self, _slug, _movie_slug):

        try:
            actor = self.filter(slug=_slug)[0]
            movie = movie_models.Movie.objects.all().filter(slug__in=_movie_slug)
        except self.DoesNotExist:
            return 0

        actor.movie = movie
        actor.save()
        return actor

