#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install

cd ..
pip install -r requirements.txt
cd backend

# python manage.py collectstatic --no-input
python manage.py migrate
python manage.py runserver

#poetry add gunicorn