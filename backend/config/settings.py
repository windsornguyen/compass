"""
Django settings for the Compass project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import django_heroku
import dj_database_url
import os
from urllib.parse import urljoin
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production! Toggle in .env
DEBUG = os.environ.get('DEBUG') == 'TRUE'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cas_ng',
    'rest_framework',
    'corsheaders',
    'compass',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_cas_ng.middleware.CASMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend',
)

HOMEPAGE = os.environ.get('COMPASS')
DASHBOARD = urljoin(os.environ.get('COMPASS'), 'dashboard')
CAS = os.environ.get('CAS_URL')

CAS_SERVER_URL = 'https://fed.princeton.edu/cas/'  # .env this?
CAS_CREATE_USER = True
CAS_CREATE_USER_ID = True
CAS_REDIRECT_URL = HOMEPAGE
CAS_LOGOUT_NEXT_PAGE = HOMEPAGE
CAS_VERSION = 3
CAS_APPLY_ATTRIBUTES_TO_USER = True
CAS_LOGIN_URL_NAME = 'login'
CAS_LOGOUT_URL_NAME = 'logout'

CAS_RENAME_ATTRIBUTES = {
    'uid': 'net_id',  # Maps to 'net_id'
    'universityid': 'university_id',  # Maps to 'university_id'
    'mail': 'email',  # Maps to 'email'
    'givenname': 'first_name',  # Maps to 'first_name'
    'sn': 'last_name',  # Maps to 'last_name'
    'department': 'department',
}

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 2419200  # 4 weeks, in seconds

# CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    CAS,
    os.environ.get('COMPASS'),
]
CSRF_TRUSTED_ORIGINS = [os.environ.get('COMPASS'), os.environ.get('BACKEND')]
CORS_ALLOW_CREDENTIALS = True
CAS_REDIRECT_WHITELIST = os.environ.get('BACKEND')
CAS_CHECK_NEXT = False


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
        'propogate': True,
    },
}

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}


AUTH_USER_MODEL = 'compass.CustomUser'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configure Django App for Heroku.
django_heroku.settings(locals())
