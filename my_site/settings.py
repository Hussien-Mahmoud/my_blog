"""
Django settings for my_site project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from google.oauth2 import service_account
from google.auth.exceptions import InvalidValue
from os import environ, path
import json

CREDENTIALS = None
try:
    with open('credentials.json', 'r') as file:
        CREDENTIALS = json.loads(file.read())
except:
    pass


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-tinvz4c2q$^01ijx^m_n)0eb+3trmn+c4-_od&z3lwf)eo55_d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if environ.get('debug') == 'false' else True

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ["https://myblog-production-f3b6.up.railway.app"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'my_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'my_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'blog' / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = BASE_DIR / 'uploads'
MEDIA_URL = '/files/'


STORAGES = {
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
    }
}

try:
    GS_BUCKET_NAME = environ.get('gs_bucket_name')
    GS_CREDENTIALS = service_account.Credentials.from_service_account_info(
        {
            "type": environ.get("type"),
            "project_id": environ.get("project_id"),
            "private_key_id": environ.get("private_key_id"),
            "private_key": environ.get("private_key"),
            "client_email": environ.get("client_email"),
            "client_id": environ.get("client_id"),
            "auth_uri": environ.get("auth_uri"),
            "token_uri": environ.get("token_uri"),
            "auth_provider_x509_cert_url": environ.get("auth_provider_x509_cert_url"),
            "client_x509_cert_url": environ.get("client_x509_cert_url"),
        }
    )
except InvalidValue:
    pass


if DEBUG and path.exists("credentials.json"):
    GS_BUCKET_NAME = CREDENTIALS['gs_bucket_name']
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
        "credentials.json"
    )
