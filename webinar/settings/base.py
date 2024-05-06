"""
Django settings for webinar project.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from typing import List

import environ
from pydantic import EmailStr

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path("webinar")

env = environ.Env(
    DJANGO_SECRET_KEY=str,
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, ["127.0.0.1:8000"]),
    DATABASE_URL=str,
    BASE_URL=str,
    ADMIN_URL=str,
)

if os.environ["DJANGO_SETTINGS_MODULE"] in [
    "webinar.settings.dev",
    "webinar.settings.test",
]:
    # Take environment variables from .env file
    environ.Env.read_env(os.path.join(ROOT_DIR, ".env"))


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.0/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY")
# https://docs.djangoproject.com/en/5.0/ref/settings/#debug
DEBUG = env("DEBUG")
# https://docs.djangoproject.com/en/5.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env("ALLOWED_HOSTS")

# APPS
# ------------------------------------------------------------------------------
LOCAL_APPS = [
    "webinar.core",
    "webinar.home",
    "webinar.users",
]
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.sites",
    "django.contrib.humanize",
    "django.forms",
    # "django.contrib.gis",
]
THIRD_PARTY_APPS = [
    "django_extensions",  # https://github.com/django-extensions/django-extensions
    "django_rq",  # https://github.com/rq/django-rq
    "hcaptcha",  # https://github.com/AndrejZbin/django-hcaptcha
    "mjml",  # https://github.com/liminspace/django-mjml
    "widget_tweaks",  # https://github.com/jazzband/django-widget-tweaks
]
# https://docs.djangoproject.com/en/5.0/ref/settings/#installed-apps
INSTALLED_APPS = LOCAL_APPS + DJANGO_APPS + THIRD_PARTY_APPS

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"

# MIDDLEWARE
# https://docs.djangoproject.com/en/5.0/topics/http/middleware/
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.0/ref/settings/#root-urlconf
ROOT_URLCONF = "webinar.urls"

# WSGI
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.0/ref/settings/#wsgi-application
WSGI_APPLICATION = "webinar.wsgi.application"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.0/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            str(APPS_DIR.path("templates")),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
            ],
        },
    },
]

# FORM WIDGETS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.0/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# DATABASES
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# ------------------------------------------------------------------------------
DATABASES = {"default": env.db()}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
# https://docs.djangoproject.com/en/5.0/ref/settings/#engine
# https://docs.djangoproject.com/en/5.0/ref/contrib/gis/db-api/#module-django.contrib.gis.db.backends
# DATABASES["default"]["ENGINE"] = "django.contrib.gis.db.backends.postgis"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# PASSWORDS
# ------------------------------------------------------------------------------
# See https://docs.djangoproject.com/en/5.0/topics/auth/passwords/#using-argon2-with-django
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGES = (("en", "English"),)
LANGUAGE_CODE = "en-gb"
TIME_ZONE = "Africa/Lusaka"
USE_I18N = True
USE_L10N = False
DATE_FORMAT = "D jS M, Y"  # e.g. Wed 4th Jan, 2023
DATETIME_FORMAT = "D jS M, Y, P"
TIME_FORMAT = "H:i"  # e.g. 14:00
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# Javascript / CSS assets being served from cache.
# See https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
# Deprecated in Django 4.2: STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
# New in Django 4.2: https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

# this is where Django *looks for* static files
STATICFILES_DIRS = [str(APPS_DIR.path("static"))]

# this is where static files are *collected*
STATIC_ROOT = str(APPS_DIR("staticfiles"))

# this is the *URL* for static files
STATIC_URL = "/static/"

# Files uploaded by users
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.0/topics/files/#managing-files

# https://docs.djangoproject.com/en/5.0/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR("files"))

# https://docs.djangoproject.com/en/5.0/ref/settings/#media-url
MEDIA_URL = "/files/"

# # https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-FILE_UPLOAD_MAX_MEMORY_SIZE
FILE_UPLOAD_MAX_MEMORY_SIZE = 35000000

# The Sites framework
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.0/ref/contrib/sites/#enabling-the-sites-framework
SITE_ID = 1

# The messages framework
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.0/ref/contrib/messages/
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

# Email-related settings
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/5.0/ref/settings/#admins
ADMINS: List[tuple[str, EmailStr]] = []
# https://docs.djangoproject.com/en/5.0/ref/settings/#managers
MANAGERS = ADMINS

# ------------------------------------------------------------------------------
# SETTINGS FOR THIRD PARTY APPS
# ------------------------------------------------------------------------------

# django-mjml
# ------------------------------------------------------------------------------
# https://github.com/liminspace/django-mjml
MJML_BACKEND_MODE = "cmd"
MJML_EXEC_CMD = [
    os.path.join(ROOT_DIR, "node_modules/.bin/mjml"),
    "--config.validationLevel",
    "skip",
]
MJML_CHECK_CMD_ON_STARTUP = False

# django-RQ
# ------------------------------------------------------------------------------
# https://github.com/rq/django-rq
RQ_QUEUES = {
    "default": {"URL": env("RQ_QUEUE", default="redis://redis:6379/0")},
}

# ------------------------------------------------------------------------------
# CUSTOM SETTINGS
# ------------------------------------------------------------------------------
ADMIN_URL = env("ADMIN_URL")  # Django Admin URL.
BASE_URL = env("BASE_URL")  # Base URL for the site.
RQ_URL = env("RQ_URL")  # URL for the RQ dashboard.
APPRISE_NTFY_URL = env("APPRISE_NTFY_URL")  # to send notifications to site admin
LIST_OF_EMAIL_RECIPIENTS: List[str] = []
