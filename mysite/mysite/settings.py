"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=l)x8vktdf2z_k&y(cv^ir%_bwacpx8q26npnipn=85l%e02sv'

# SECURITY WARNING: don't run with debug turned on in production!

# flaw 3: Security misconfiguration. One shouldn't leave DEBUG as true, as
# this can lead to a situation where it will be easier for the
# attacker to learn about the inner workings of the application.

# fix: Set DEBUG as False. This will show a much less revealing page
# if an error is faced.

DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

# Login

LOGIN_REDIRECT_URL = 'polls:index'

# flaw 2: The site has no logging and monitoring capabilities.
# This will lead to situations where attacks on the system aren't noticed
# and won't subsequently be responded to.

# The fix: Django has its own lagging framework, which is designed with this
# problem in mind. All we have to do is add loggers for the components of our
# application.

# This configuration sends messages of level 'INFO' and higher to the console.
# While DEBUG = True, this level of sending messages is the same as Django's default
# logging configuration.
# These logs could also be saved on a local file.

#LOGGING = {
#    "version": 1,
#    "disable_existing_loggers": False,
#    "handlers": {
#        "console": {
#            "class": "logging.StreamHandler",
#        },
#    },
#    "root": {
#        "handlers": ["console"],
#        "level": "WARNING",
#    },
#    "loggers": {
#        "django": {
#            "handlers": ["console"],
#            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
#            "propagate": False,
#        },
#    },
#}

# flaw 5: Identification and authentication failures. In the following
# password hashing setting the unsecure MD5 is used. MD5 isn't safe because
# it is vulnerable to collision attacks

# fix: Use better hashing for your passwords. You can install SHA256 and Argon2
# password hashers with pip and use either of them rather than the MD5.

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
    #'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    #'django.contrib.auth.hashers.Argon2PasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
