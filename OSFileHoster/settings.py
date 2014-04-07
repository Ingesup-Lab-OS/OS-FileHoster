"""
Django settings for frontos project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

try:
   from local_settings import *
except ImportError, e:
    print
    """
    -------------------------------------------------------------------------
     You need to create a local_settings.py file which needs to contain at least
    database connection information.

    Copy local_settings_default.py to local_settings.py and edit it.
    -------------------------------------------------------------------------
    """

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

LOGIN_REDIRECT_URL = "/session_auth_token"
LOGIN_URL="/login"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_v*s6n9(j+b-gje9(tt7pq0el$f&a5m&p!afua%5unb5sovr3@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'openstack_auth',
    'django.contrib.staticfiles',
    'OSFileHoster.apps.frontks',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'OSFileHoster.urls'

WSGI_APPLICATION = 'OSFileHoster.wsgi.application'

AUTHENTICATION_BACKENDS = ('openstack_auth.backend.KeystoneBackend',)
OPENSTACK_KEYSTONE_URL = "http://10.31.92.166:5000/v2.0"

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(
        os.path.dirname(__file__),
        'static',
    ),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates').replace('\\','/'),
)

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

