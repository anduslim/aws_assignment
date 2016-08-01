# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models


class MovieManager(models.Manager):

    def create_movie(self, _slug, _name, _dateyear, _description):

        movie = self.create(slug=_slug, name=_name, date=_dateyear,
                            description=_description)

        return movie

