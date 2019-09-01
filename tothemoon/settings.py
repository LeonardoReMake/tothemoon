"""
Django settings for tothemoon project.

Generated by 'django-admin startproject' using Django 1.11.20.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open('/home/abgde/secret_key') as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['10.55.131.233', '127.0.0.1', 'shareandsave.ru', '84.201.167.9']



# Application definition

INSTALLED_APPS = [
    'social_django',
    'bootstrap4',
    'tempus_dominus',
    'cotravelling.apps.CotravellingConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_user_agents',
    'sass_processor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'tothemoon.urls'

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
                'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'tothemoon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

with open('/home/abgde/database_password') as f:
    PASSWORD = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cotravelling',
        'USER': 'abgde',
        'PASSWORD': PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Minsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',          # бекенд авторизации через ВКонтакте
    'django.contrib.auth.backends.ModelBackend', # бекенд классической аутентификации, чтобы работала авторизация через обычный логин и пароль
)

SOCIAL_AUTH_VK_OAUTH2_KEY = '6978072'
with open('/home/abgde/vk_app_key') as f:
    SOCIAL_AUTH_VK_OAUTH2_SECRET = f.read().strip()
SOCIAL_AUTH_VK_APP_USER_MODE = 2
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Configuration for SCSS 

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

# Django Sass
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR, 'static')

#SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['state']
#SESSION_COOKIE_SECURE=False

#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
