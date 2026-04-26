#!/bin/bash

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the Gunicorn server
PORT=${PORT:-8000}  # Use dynamic PORT if set, default to 8000
exec gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT --workers 3
