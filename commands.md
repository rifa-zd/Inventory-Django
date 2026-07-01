```bash

python -m venv venv
venv\Scripts\activate

pip install django

pip list

django-admin startproject inventory .

# python manage.py help

python manage.py runserver

python manage.py startapp dashboard #app is like for a website(project) there are-users, shops, - the apps  

python manage.py makemigrations dashboard
python manage.py migrate

```

> **psycopg2-binary** = the driver that lets Python/Django talk to PostgreSQL
 **PostgreSQL** = the actual database server that stores your data
 
# Install PostgreSQL adapter for Django - skip for now working with sqlite
# pip install psycopg2-binary



