# To Do List - Django Implementation

**Author**: Nicholas Hunt-Walker

**Deployment**: https://django-todo.herokuapp.com/

## Getting Started

Navigate to a directory that you want to work in and clone down this repository.

```
$ git clone https://github.com/PythonToDoList/pyramid.git
```

### For Development

Move into the cloned directory and start a new Python 3 [virtual environment](https://docs.python.org/3/tutorial/venv.html). You should be using Python 3.6 or later.

```
$ cd pyramid
pyramid $ python3 -m venv ENV
(ENV) pyramid $ source ENV/bin/activate
```

[pip](https://pip.pypa.io/en/stable/installing/) install this package along with the included `testing` extras. Note: you will need [Postgres](https://www.postgresql.org) running locally for this application.

```
(ENV) pyramid $ pip install .[testing]
```

Create Postgres databases for developing and testing this application.

```
(ENV) pyramid $ createdb pyramid_todo
(ENV) pyramid $ createdb test_todo
```

Export environment variables that point to these databases and initialize the development database. You can export the environment variables at the command line, but you should really include that variable in the environment in your `ENV/bin/activate` script. The database url example given below is what works on my machine, but your mileage may vary depending on what it takes to access your local databases.

```
(ENV) pyramid $ export DATABASE_URL='postges://localhost:5432/pyramid_todo'
(ENV) pyramid $ echo \export DATABASE_URL="'postges://localhost:5432/pyramid_todo'" >> ENV/bin/activate
(ENV) pyramid $ export TEST_DB='postges://localhost:5432/pyramid_todo'
(ENV) pyramid $ echo \export DATABASE_URL="'postges://localhost:5432/test_todo'" >> ENV/bin/activate
(ENV) pyramid $ initdb development.ini
```

To serve the application while developing, Pyramid provides the `pserve` command. Use it in conjunction with one of the `.ini` configuration files.

```
(ENV) pyramid $ pserve development.ini --reload
```

### For Deployment (Heroku)

Assuming you have access to the [Heroku CLI toolset](https://devcenter.heroku.com/articles/heroku-cli), move into the cloned directory and create a new Heroku application.

```
pyramid $ heroku create
```

Configure the [Heroku Postgres add-on](https://elements.heroku.com/addons/heroku-postgresql) for your new Heroku application (for whatever level of Postgres you want to have).

```
pyramid $ heroku addons:create heroku-postgresql:hobby-dev
```
