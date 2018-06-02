# IMDB
CRUD operations in Django Rest Framework for Movies.

You can find the documentation of the api's below:

Movie API's : https://documenter.getpostman.com/view/1603718/RW8FF6kL
Auth API's : https://documenter.getpostman.com/view/1603718/RW8FF6kN

# Dependencies
Python 3.4
Django >= 1.9.1
PostgreSQL

# Virtual Environment Setup
Setup virtualenv with command: 

$ virtualenv -p python3 imdb

Move to virtualenv and activate its environment:

$ source bin/activate

# Database Setup
$ sudo apt-get update

$ sudo apt-get install mysql-server-5.6

$ sudo mysql_secure_installation

$ mysql -u root -p"your root password here(without quotes)"

$ create database marketplace;

$ create user 'testuser'@'localhost' identified by 'password';

$ GRANT ALL PRIVILEGES ON product.* TO 'testuser'@'localhost';

$ FLUSH PRIVILEGES;

# Github Repository Setup
Go to the link: https://github.com/itsayushbansal/IMDB

Clone this new repository : git clone https://github.com/itsayushbansal/IMDB.git

Using Command Line, navigate to the repository

# Dependency Setup
Install requirements: "pip install -r requirements.txt".
In settings.py change 

# To Run
$ python manage.py runserver
