# The Airline Project

## Create the project

```bash
django-admin startproject airline 
```

## Crate the flights application

```bash
python3 manage.py startapp flights
```

## Add in ```settings.py``` file the new app do the INSTALLED_APPS list
```python
INSTALLED_APPS = [
    'flights',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## In the project's ```urls.py``` file add a reference to the app

```python

# remember to add 'include' to the imports session
from django.urls import include, path

path('flights/', include("flights.urls")),
```

## In the project's ```models.py``` file add the application's models

Models represent data inside of the database.

```python
class Airport(models.Model):
    code = models.CharField(max_length=64)
    city = models.CharField(max_length=64)


class People(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

```

## Create and apply the migrations

Every changes in the model requires these two steps in order to be reflected into de database.

### 1. Creating/recreating the migrations

```bash
python3 manage.py makemigrations
```

### 2. Applying the migrations:
```bash
python3 manage.py migrate
```

## Add a new airport

Open up the Django shell
```bash
python3 manage.py shell
```

Add airport

```bash
>>> from flights.models import Airport
>>> a = Airport(code="JFK", city="New York")
>>> a.save()
```

## Implement a string representation for the Airport model

Add the ```__str__``` method to the model class definition:
```python
    def __str__(self):
        return f"{self.id}: {self.code}-{self.city}"
```

## Verifying the string representation

Open up the Django shell
```bash
python3 manage.py shell
```

List airports
```bash
>>> from flights.models import Airport
>>> airports = Airport.objects.all()
>>> airports
```


## Create the application's ```urls.py``` file

```python
from django.urls import path

from . import views

app_name = "airline" # project name

urlpatterns = [
    path("", views.index, name="index"),
]
```

### NON RELATED

```sql
select f.id as flight, p.first, p.last, o.city as origin, d.city as destination, f.duration
from flights f
inner join passengers pp on pp.flight_id=f.id
inner join people p on p.id=pp.person_id
inner join airports o on o.id=f.origin_id
inner join airports d on d.id=f.destination_id;
```