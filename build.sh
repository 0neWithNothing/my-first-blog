#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py migrate

source env/bin/activate
pip install -U pip
pip install -r requirements.txt