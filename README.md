# IMDB
CRUD operations in Django Rest Framework for Movies.

You can find the documentation of the api's below:

https://documenter.getpostman.com/view/1603718/marketplace/7E8gbFN

# Dependencies
Python 2.x

mySQL

# Virtual Environment Setup
Setup virtualenv with command: 

$ virtualenv -p python2 marketplace

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
Go to the link: https://github.com/itsayushbansal/marketplace

Clone this new repository : git clone https://github.com/itsayushbansal/marketplace.git

Using Command Line, navigate to the repository

# Dependency Setup
Install requirements: "pip install -r requirements.txt".

In config.ini, change user and password to your mysql user's username and password.

# To Run
$ python views.py