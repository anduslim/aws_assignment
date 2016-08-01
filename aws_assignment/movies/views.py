# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Movie


class MovieListView(LoginRequiredMixin, ListView):
    model = Movie

    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class MovieDetailView(LoginRequiredMixin, DetailView):
    model = Movie

    slug_field = 'slug'
    slug_url_kwarg = 'slug'
