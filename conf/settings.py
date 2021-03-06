"""
Django settings for conf project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
# import psycopg2
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ======== STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'staticfiles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# ********* UNCOMMENT AFTER NPM RUN BUILD *********
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'frontend/static/build/static'),
)
# ======== END STATIC FILE CONFIGURATION

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0!&r7tm^k9&3ta$7e1cq0qlg68)jw(=oue@p_vzs%*w4f3owas'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION

ALLOWED_HOSTS = [
    'better-world-buddies.herokuapp.com',
    'localhost',
    '127.0.0.1'
]


# UPLOADED FILE CONFIGURATION

# See: https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# DO NOT COMMIT TO VERSION CONTROL WITH THESE KEYS VISIBLE
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = 'finalproject19'
AWS_S3_FILE_OVERWRITE = False  # set to true by default which allows files with same name to overwrite each other
AWS_DEFAULT_ACL = None  # default will be to lock down everything
# AWS_QUERYSTRING_AUTH
#
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'phone_field',
    'rest_framework',
    'localflavor',
    'storages',
    # 'hijack',
    # 'compat',
    # 'hijack_admin',

    'users',
    'api',
    'buddies',
    'frontend',

    # 'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

]

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'users/templates',)],
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

WSGI_APPLICATION = 'conf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(default=os.environ['DATABASE_URL']),
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'buddies',
            'USER': 'buddies',
            'PASSWORD': 'safepass',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

AUTH_USER_MODEL = 'users.CustomUser'

# May need these redirects for custom user model
LOGIN_REDIRECT_URL = '/profile/'
#
LOGOUT_REDIRECT_URL = '/'

LOGIN_URL = '/login/'

REACT_APP_DIR = 'frontend/static'

# # hijack settings
# HIJACK_LOGIN_REDIRECT_URL = '/profile/'  # Where admins are redirected to after hijacking a user
# HIJACK_LOGOUT_REDIRECT_URL = '/admin/auth/customuser/'  # Where admins are redirected to after releasing a user
# HIJACK_ALLOW_GET_REQUESTS = True
