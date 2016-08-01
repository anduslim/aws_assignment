import sys, os, datetime
import django
sys.path.append('../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings.local')
django.setup()

from aws_assignment.actors.models import Actor
from aws_assignment.movies.models import Movie

ACTOR_DIR = './actor/'
MOVIE_DIR = './movie/'
JOIN_DIR = './'

def parseActor(file):

    for line in file:
        slug, name, dob_unix, description = line.rstrip('\n').split('|')
        print("\tslug:{}, name: {}, dob_unix: {}, desc: {}".format(slug, name, dob_unix,
                                                                   description))
        dob = datetime.datetime.fromtimestamp(int(dob_unix[:-3])).strftime('%Y-%m-%d')
        print('dob: {}'.format(dob))
        result = Actor.objects.create_actor(slug, name, dob, description)
        if result:
            print('Create actor successfully!')
        else:
            print('Error in creating actor!')


def parseMovie(file):

    for line in file:
        slug, name, dateyear, description = line.rstrip('\n').split('|')
        print("\tslug:{}, name: {}, year: {}, desc: {}".format(slug, name, dateyear,
                                                                   description))
        result = Movie.objects.create_movie(slug, name, dateyear, description)
        if result:
            print('Create movie successfully!')
        else:
            print('Error in creating movie!')


def parseJoin(filename):
    for line in file:
        slugs = line.rstrip('\n').split('|')
        actor_slug = slugs[0]
        movies_slug = slugs[1:]
        print("\tactor:{}, movies: {}".format(actor_slug, movies_slug))
        #for movie in movies_slug:
        result = Actor.objects.update_actor_movie(actor_slug, movies_slug)
        if result:
            print('Update actor movie successfully!')
        else:
            print('Error in update actor movie!')


# Populate actor data files
print('\n\nParsing actor data files\n')

for filename in os.listdir(ACTOR_DIR):
    if filename.endswith(".data"):
        print('\nFilename: {}'.format(filename))
        file = open(ACTOR_DIR + filename, 'r')
        parseActor(file)


# Populate movie data files
print('\n\nParsing movie data files\n')

for filename in os.listdir(MOVIE_DIR):
    if filename.endswith(".data"):
        print(filename)
        file = open(MOVIE_DIR + filename, 'r')
        parseMovie(file)


# Populate join file
print('\n\nParsing join data files\n')

for filename in os.listdir(JOIN_DIR):
    if filename.endswith(".data"):
        print(filename)
        file = open(JOIN_DIR + filename, 'r')
        parseJoin(file)
