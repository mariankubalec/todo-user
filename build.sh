#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

cd backend

python manage.py collectstatic --no-input
python manage.py migrate

cd ..

poetry add gunicorn
