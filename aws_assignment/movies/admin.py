from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):

    list_display = ('slug', 'name', 'date', 'description')


admin.site.register(Movie)
