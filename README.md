# To Do List - Django Implementation

**Author**: Nicholas Hunt-Walker

**Deployment**: https://django-tasks.herokuapp.com/

## Getting Started

Navigate to a directory that you want to work in and clone down this repository.

```
$ git clone https://github.com/PythonToDoList/django.git
```

### For Development

Move into the cloned directory and start a new Python 3 [virtual environment](https://docs.python.org/3/tutorial/venv.html). You should be using Python 3.6 or later.

```
$ cd django
django $ python3 -m venv ENV
(ENV) django $ source ENV/bin/activate
```

[pip](https://pip.pypa.io/en/stable/installing/) install all of the packages from in the `requirements.txt` file. Note: you will need [Postgres](https://www.postgresql.org) running locally for this application.

```
(ENV) django $ pip install -r requirements.txt
```

Create Postgres databases for developing and testing this application.

```
(ENV) django $ createdb django_todo
(ENV) django $ createdb test_todo
```

Export environment variables that point to these databases. You can export the environment variables at the command line, but you should really include that variable in the environment in your `ENV/bin/activate` script. The database url example given below is what works on my machine, but your mileage may vary depending on what it takes to access your local databases.

```
(ENV) django $ export DATABASE_URL='postgres://localhost:5432/django_todo'
(ENV) django $ echo \export DATABASE_URL="'postgres://localhost:5432/django_todo'" >> ENV/bin/activate
(ENV) django $ export TEST_DB='postgres://localhost:5432/test_dj_todo'
(ENV) django $ echo \export TEST_DB="'test_dj_todo'" >> ENV/bin/activate
```

For the settings, also export a `SECRET_KEY`. You can also set `ALLOWED_HOSTS` but it's not required for development.

```
(ENV) django $ export SECRET_KEY='some secret key that you create'
(ENV) django $ echo \export SECRET_KEY="'mysecretkey'"
(ENV) django $ export ALLOWED_HOSTS=[]
(ENV) django $ echo \export ALLOWED_HOSTS=[]
```

Navigate into the `django_todo` directory and apply the built-in migrations to your development database.

```
(ENV) django_todo $ python manage.py migrate
```

To serve the application while developing, Django provides the `manage.py runserver` command.

```
(ENV) django $ python manage.py runserver
```

### For Deployment (Heroku)

Assuming you have access to the [Heroku CLI toolset](https://devcenter.heroku.com/articles/heroku-cli), move into the cloned directory and create a new Heroku application.

```
django $ heroku create
```

Configure the [Heroku Postgres add-on](https://elements.heroku.com/addons/heroku-postgresql) for your new Heroku application (for whatever level of Postgres you want to have).

```
django $ heroku addons:create heroku-postgresql:hobby-dev
```

Set your the following environment variables on Heroku:

- `SECRET_KEY`: this can be any string
- `ALLOWED_HOSTS`: this should just be an empty list as a string '[]'
- `DEBUG`: `False`

```
pyramid $ heroku config:set SECRET_KEY='some secret string'
pyramid $ heroku config:set DEBUG='False'
pyramid $ heroku config:set ALLOWED_HOSTS='[]'
```

Push this repository to your Heroku repository and `heroku open` to view the site.
