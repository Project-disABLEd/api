# Short installation guide

## First, install Python from https://www.python.org/downloads/
Our server software requires:
- Python (3.5, 3.6, 3.7, 3.8)
- Django (1.11, 2.0, 2.1, 2.2)

We **highly recommend** and only officially support the latest patch release of each Python and Django series.

## Create a virtual environment to isolate our package dependencies locally
```
python3 -m venv env
source env/bin/activate  # On Windows use 'env\Scripts\activate'
```
## Install Django and Django REST framework into the virtual environment via pip
```
pip install django
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```
## We'll also need to create an initial migration for our model, and sync the database for the first time.
```
python manage.py makemigrations api_server
python manage.py migrate
```
## Now we can start up a sample server.
```
python manage.py runserver
```
