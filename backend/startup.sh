﻿#!/bin/bash
python manage.py collectstatic --noinput &&
python manage.py makemigrations
python manage.py migrate
gunicorn --env DJANGO_SETTINGS_MODULE=dashboard.settings dashboard.wsgi -w 2 -b :8000
