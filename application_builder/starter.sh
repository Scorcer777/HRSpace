#!/bin/sh

while ! nc -z db 5432;
    do sleep .5;
    echo "wait database";
done;
    echo "connected to the database";

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --noinput
python manage.py loaddata data/region_data.json
python manage.py loaddata data/city_data.json
python manage.py loaddata data/citizenship_data.json
python manage.py loaddata data/industry_data.json
python manage.py loaddata data/language_data.json
python manage.py loaddata data/languageproficiency_data.json
python manage.py loaddata data/profession_data.json
python manage.py loaddata data/skill_data.json
python manage.py loaddata data/professionskill_data.json
exec "$@"
