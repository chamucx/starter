from .settings import *
import os

WIBBLE2 = 'Wibble2'




# TO-DO ADD IT CSRF_TRUSTED_ORIGINS = ['https://*'] as wildcar locally
# TO-DO once deployed from VS code
# CSRF_TRUSTED_ORIGINS = ['https://youdomain.azurewebsites.net']

# TO-ADD -- uncomment

#add the next middleware for whitenoise
#MIDDLEWARE = [
#    'django.middleware.security.SecurityMiddleware',
#    # Enables whitenoise for serving static files
#    'whitenoise.middleware.WhiteNoiseMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#]

#TO-DO add the static files
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
