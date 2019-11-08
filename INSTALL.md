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
## Generate a new private key, and put it in ./api_project/secret_key.txt
```
django-admin shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
'[GENERATED KEY]'
>>> ```
