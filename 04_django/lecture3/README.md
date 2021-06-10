# Developing a Django Webservice

Django is a Python webserver.

## Installing Django

Once python is already installed, Django may be instaled, by typing this pip command:
```bash
pip3 install Django
```

## Starting a new Django project

This command allows us to create a new Django project:
```bash
django-admin startproject <projectName> 
```

After that, among other files, the ```manage.py``` file will be created.

### Trying out the new Django server

This command starts the new project:
```bash
python3 manage.py runserver
```

By default the new server runs on port 8000.

The Django's default page can be accessed on the address:
```http
http://localhost:8000
```


## Creating a new application into the Django project

Every Django project is composed for one or more applications.

To create a new appplication into the Django project, just type the command bellow, replacing the function's name "hello" acconrdingly:
```bash
python3 manage.py startapp hello
```

After that, it is necessary do add the reference to the new app to the INSTALLED_APPS list into the ```settings.py``` file just like below:

```python
INSTALLED_APPS = [
    'hello',  # <-- here
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## Setting the new application up on the Project (the basics)

In order to get the new application working, these three steps have to be taken.

### 1. Into ```views.py``` : create a function

Create the function which will be executed when the corresponding route (url) will be accessed by the client.

```python views.py
from django.http import HttpResponse # included for the function's return
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")
```

### 2. Create a ```urls.py``` file for the application

Once a project may have many applications into it, it is a good practice to set each application's routes into its own ```urls.py``` file. So, a ```hello/urls.py``` file was create cotaining this code into it:

```python hello/urls.py
from django.urls import path

from . import views

# this "urlpatterns" list has to have exactly this name
urlpatterns = [
    path("", views.index, name="index")
]
```

### 3. Update the Project's ```urls.py``` file

```python urls.py
from django.contrib import admin
from django.urls import path, include # allows including othe urls files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("hello.urls")) # add here
]
```

## Setting up robust applications

## Task application

## Migration

Jango stores session data inside tables.

When using session control for a list, in order to avoid Django raising an exception on not being able to store data in a table, use this command in ternminal:

```bash
python manage.py migrate
```

