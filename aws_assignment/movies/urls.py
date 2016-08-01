# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.MovieListView.as_view(),
        name='list'
    ),

    # URL pattern for the ActorDetailView
    url(
        regex=r'^(?P<slug>[\w-]+)/$',
        view=views.MovieDetailView.as_view(),
        name='detail'
    ),
]
