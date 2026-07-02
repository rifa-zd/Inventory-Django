```bash
# activating virtual enviroment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# migrate first
python manage.py migrate
python manage.py runserver

#bypassing SSL certificate error - a self-signed certificate blocking pip from downloading packages.
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

pip install psycopg2-binary --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host pypi.python.org
```
```bash
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

Shifted to postgre (used vs extension)



