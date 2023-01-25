# LOGBOOK 

Genereate base code with : 
 `django-admin startproject <nameProject>`

Run app : 
 `python manage.py runserver`

Migrate to setup the db
 `python manage.py migrate`

Add db.sqlite3 in .gitignore

Create an django "application" (part of the project) --> app listings is created
 `python manage.py startapp listings`

Add listings to the INSTALLED_APPS section of ./merchex/setttings.py (good practice is to add it in the end of the list , thus it is the last to be loaded.)

create first views in listing/views.py