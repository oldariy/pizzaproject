# PizzaProject

Web app for pizzeria using Django, MDL, jQuery, PostgreSQL.

### Install

1. Install [Python 3.x](https://www.python.org)
2. Install [PostgreSQL 9.5.x](https://www.postgresql.org/download)
3. Donwload and unpack [PizzaProject](https://github.com/GreyPK/pizzaproject/archive/master.zip)
4. Open SQL Shell (psql) and create new database and role using this code:

```PostgreSQL
create user django_user with password 'password'; 
alter role django_user set client_encoding to 'utf8'; 
alter role django_user set default_transaction_isolation to 'read committed'; 
alter role django_user set timezone to 'Antarctica/Vostok'; 
create database django_db owner django_user;
```
5. Create folder for project and create virtual environment:

```sh
$ mkdir pizzaapp
$ cd pizzaapp
$ python -m venv pizzavenv
```
6. Activate virtual environment:
```sh
$ pizzavenv\Scripts\activate
```
7. Install django and another components
```sh
$ pip install django~=1.11.2
$ pip install django-material
$ pip install Pillow
$ pip install psycopg2
```
8. Create superuser with login **admin** and password **adminpass** and execute this commands:
```sh
$ python manage.py createsuperuser
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
9 Open [url](127.0.0.1:8000)