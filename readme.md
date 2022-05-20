# Snippet API REST

This project was built with Django and Django Rest Framework. 
It consists of a REST API that controls all types of requests 
made by the client.

## Available Scripts

In the project directory, you can run:

### Build

Run `docker-compose build` to build or rebuild the services.

### Run the app in development mode

Run `docker-compose up` to builds, (re)creates, starts, and attaches to
containers for a service. Then go to [http://localhost:8000](http://localhost:8000)
to view it in your favorite browser.

### Running unit tests

Run `docker-compose run --rm django sh -c "python manage.py test && flake8"` to
execute the unit tests and linting the source code with flake8, verifying pep8,
pyflakes and circular complexity.

### Run the app in production mode

Run `docker-compose up -d --build` to first make your services builds and then,
to start the containers in the background and leave them running.

## Refresh app, rebuilding it

Run `sudo docker-compose up --build --force-recreate --no-deps django` or 
`sudo docker-compose up -d --build --force-recreate --no-deps django` to
 rebuild the django container, reinstalling its dependencies.
 
## Refresh app

Run `sudo docker-compose up --force-recreate --no-deps django` or 
`sudo docker-compose up -d --force-recreate --no-deps django` to
 rebuild the django container, reinstalling its dependencies.

## Technologies involved

- Docker
- Python
- Django
- PostgreSQL
- Django Rest Framework

## Utilities
- Django fields: https://docs.djangoproject.com/en/3.0/ref/models/fields/

## Django Commands

- Create superuser
    - python manage.py createsuperuser
- Create a new app:
    - django-admin startapp user
- Create a migration
    - python manage.py makemigrations
- Migrate
    - python manage.py migrate
- Migrate Through Docker
    - sudo docker-compose run --rm django sh -c "python manage.py migrate"