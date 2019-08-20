## What is Django?
Django is a Web-Application Framework written in `python`.

It is pretty simple to make web-applications in Django.

Let's get started!

#### Requirements
- Python 3.6 & up
- Virtual Environment (pipenv or virtualenv)

#### Prerequisites
- Python, HTML, CSS, Bootstrap Basics

#### Create Virtual Environment & Install Django
Move to the directory where you want to start this project.

Create a directory with name of your choice, we'll be using try_django for reference.

You'll be installing django for virtual environment only i.e for that particular directory.

```
cd /path/to/dev/folder
mkdir try_django
cd try_django
pipenv --python 3.6 install django==2.2
pipenv shell
```

`pipenv shell` will open the virtual environment that we created.

We'll hve two files initially in try_django folder
- Pipfile
- Pipfile.lock

#### Create Django Project
Make sure virtual environment is active and you're in the virtual environment 
directory i.e in our case try_django.

```
mkdir src
cd src
django-admin startproject try_django . 
python manage.py runserver
  - You'll get an address, try running it in your browser. You'll see django successfully installed.
python manage.py migrate
```

- Create Superuser 
  - python manage.py createsuperuser

#### Add this project into sublime
- Open Sublime
- Project --> New Project --> try_django Project Location --> save as try_django

