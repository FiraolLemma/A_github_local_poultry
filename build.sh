#!/usr/bin/env bash
# build.sh

set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py makemigrations users
python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --noinput