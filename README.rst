aws_assignment
==============================

AWS home assignment


LICENSE: MIT


Pre-requistics
------------

* Setup postgresql with a test DB and user on your machine.
* Use environment variables for DB settings or use a .env file.
* Use virtualenv to manage python virtual environment.
* Run :code:`pip install -r requirements/local.txt` to install dependencies.


Setup
----------

* Run :code:`./manage.py migrate` for existing migration files.
* Run :code:`python importDB.py` in _util_ folder to import all *.data files.


Run
--------

* Run :code:`./manage.py runserver 8000`.

Test
--------
* To see list of movies, go to [http://localhost:8000/movie/].
* To see details of a movie, got to [http://localhost:8000/movie/a_fish_called_wanda/].
* To see list of actors, go to [http://localhost:8000/actor/].
* To see details of an actor, go to [http://localhost:8000/actor/jamie_lee_curtis/].
