```bash

python -m venv venv
venv\Scripts\activate

pip install django

pip list

django-admin startproject inventory .

# python manage.py help

python manage.py runserver

python manage.py startapp dashboard #app is like for a website(project) there are-users, shops, - the apps  

```

> **psycopg2-binary** = the driver that lets Python/Django talk to PostgreSQL
 **PostgreSQL** = the actual database server that stores your data
 
# Install PostgreSQL adapter for Django - skip for now working with sqlite
# pip install psycopg2-binary


> <!-- <form method="POST" action="{% url 'dashboard:delete_document' doc.id %}"
                      onsubmit="return confirm('Delete {{ doc.name }}? This cannot be undone.');">
                  {% csrf_token %} -->
                  dlt button should be here
                  
                <!-- </form> -->


