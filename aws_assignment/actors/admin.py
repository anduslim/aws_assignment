# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from .models import Actor


class ActorAdmin(admin.ModelAdmin):

    list_display = ('slug', 'name', 'dob', 'description', 'print_movie_list')
    list_filter = ('slug', 'name')


admin.site.register(Actor)
