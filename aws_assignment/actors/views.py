# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Actor


class ActorListView(LoginRequiredMixin, ListView):
    model = Actor

    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ActorDetailView(LoginRequiredMixin, DetailView):
    model = Actor

    slug_field = 'slug'
    slug_url_kwarg = 'slug'
