# IMDB
CRUD operations in Django Rest Framework for Movies.

You can find the documentation of the api's below:

Movie API's : https://documenter.getpostman.com/view/1603718/RW8FF6kL

Auth API's : https://documenter.getpostman.com/view/1603718/RW8FF6kN

# Dependencies
Python 3.4

Django >= 1.9.1

PostgreSQL >= 9.1

# Virtual Environment Setup
Setup virtualenv with command: 

$ virtualenv -p python3 imdb

Move to virtualenv and activate its environment:

$ source bin/activate

# Database Setup
$ sudo apt-get update

$ sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

$ sudo -i -u postgres psql

$ create database test;

$ CREATE USER user WITH PASSWORD pass;

$ GRANT ALL PRIVILEGES ON DATABASE test TO user;

# Github Repository Setup
Go to the link: https://github.com/itsayushbansal/IMDB

Clone this new repository : git clone https://github.com/itsayushbansal/IMDB.git

Using Command Line, navigate to the repository

# Dependency Setup
Install requirements: "pip install -r requirements.txt".

In settings.py, change <DB_PASSWORD>

Run migrations: "python manage.py migrate"

Create superuser: "python manage.py createsuperuser"

# To Run
$ python manage.py runserver
