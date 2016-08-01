from django.db import models

class Movie(models.model):

    name = models.CharField('Movie Name', max_length=150, blank=False)
    desc = models.CharField(max_length=1000, blank=True)
