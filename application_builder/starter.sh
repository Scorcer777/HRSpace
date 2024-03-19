#!/bin/sh

while ! nc -z db 5432;
    do sleep .5;
    echo "wait database";
done;
    echo "connected to the database";

python manage.py makemigrations
python manage.py migrate
#python manage.py createsuperuser --email superuser@test.com
python manage.py loaddata data/cities_data.json
python manage.py loaddata data/citizenships_data.json
python manage.py loaddata data/industries_data.json
python manage.py loaddata data/languages_data.json
python manage.py loaddata data/profession_skills_data.json
python manage.py loaddata data/professions_data.json
#gunicorn -w 2 -b 0:8000 foodgram_project.wsgi:application