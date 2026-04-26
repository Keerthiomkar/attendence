import os
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

# Security settings
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# Middleware settings
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # other middleware classes...
]