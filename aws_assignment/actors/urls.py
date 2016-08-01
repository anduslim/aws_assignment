# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the ActorListView
    url(
        regex=r'^$',
        view=views.ActorListView.as_view(),
        name='list'
    ),

    # URL pattern for the ActorDetailView
    url(
        regex=r'^(?P<slug>[\w-]+)/$',
        view=views.ActorDetailView.as_view(),
        name='detail'
    ),
]
