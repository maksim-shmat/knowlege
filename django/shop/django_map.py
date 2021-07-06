"""Scheme of django site."""

# first make project on github

simple/
    simple/
        .git/
        .gitignore
        .editorconfig
        manage.py
        pyproject.toml
        requirements/
            base.txt
            local.txt
            production.txt
            tests.txt
        setup.cfg
        simple/
            __init__.py
            apps/
                accounts/
                    migrations/
                        __init__.py
                static/
                    accounts/
                templates/
                    accounts/
                tests/
                    __init__.py
                    factories.py
                __init__.py
                admin.py
                apps.py
                constants.py
                models.py
                views.py
            core/
                migrations/
                    __init__.py
                static/
                    core/
                templates/
                    core/
                tests/
                    __init__.py
                    factories.py
                __init__.py
                admin.py
                apps.py
                constants.py
                models.py
                views.py
            __init__.py
        locale/
        settings/
            __init__.py
            base.py
            local.py
            production.py
            tests.py
        static/
        templates/
        asgi.py
        urls.py
        wsgi.py
venv/

######

base.txt
    dj-database-url==0.5.0
    Django==3.2.4
    psycopg2-binary==2.9.1
    python-decouple==3.4
    pytz==2021.1

tests.txt
-r base.txt
    black==21.6b0
    coverage==5.5
    factory-boy==3.2.0
    flacke8==3.9.2
    isort==5.9.1
    tox==3.23.1

local.txt
-r tests.txt
    django-debug-toolbar==3.2.1 # it is safe?
    ipython==7.25.0

production.txt
-r base.txt
    gunicorn==20.1.0
    sentry-sdk==1.1.0

###### base.py

from pathlib import Path

import dj_database_url
from decouple import Csv, config

BASE_DIR = Path(__file__).resolve().parent.parent

# ============
# CORE SETTINGS
# ============

SECRET_KEY = config("SECRET_KEY", default="django-insecure$simple.settings.local")

DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1, localhost", cast=Csv())

INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "simple.urls"

INTERNAL IPS = ["127.0.0.1"]

WSGI_APPLICATION = "simple.wsgi.application"

# ===================
# MIDDLEWARE SETTINGS
# ===================

MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ==================
# TEMPLATES SETTINGS
# ==================

TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [BASE_DIR / "templates"],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

# ==================
# DATABASES SETTINGS
# ==================

DATABASES = {
        "default": dj_database_url.config(
            default=config("DATABASE_URL", default="postgres://simple@localhost:5432/simple"),
            conn_max_age=600,
        )
}

# =========================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# =========================================

AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttribueSimilarityValidator",
            "NAME": "django.contrib.auth.password_validation.MinimumLingthValidator",
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
]

# ======================
# I18N AND L10N SETTINGS
# ======================

LANGUAGE_CODE = config("LANGUAGE_CODE", default="en-us")

TIME_ZONE = config("TIME_ZONE", default="UTC")

USE_I18N = True

USE_l10N = True

USE_TZ = True

LOCALE_PATHS = [BASE_DIR / "locale"]

# =====================
# STATIC FILES SETTINGS
# =====================

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR.parent.parent / "static"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_FINDERS = (
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    )

# =====================
# MEDIA FILES SETTINGS
# =====================

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR.parent.parent / "media"

# =====================
# THIRD-PARTY SETTINGS
# =====================

# =====================
# FIRST-PARTY SETTINGS
# =====================

SIMPLE_ENVIRONMENT = config("SIMPLE_ENVIRONMENT", default="local")

###### local.py

# flake8: noqa

from .base import *

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

# ===============
# EMAIL SETTINGS
# ===============

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

###### tests.py

# flake8: noqa

from .base import *

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()

###### production.py

# flacke8: noqa

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

import simple
from .base import *

# =================
# SECURITY SETTINGS
# =================

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = True

# =========================
# THIRD-PARTY APPS SETTINGS
# =========================

sentry_sdk.init(
        dsn=config("SENTRY_DSN", default=""),
        environment=SIMPLE_ENVIRONMENT,
        release="simple@%s" % simple.__version__,
        integrations=[DjnagoIntegrations()],
)

###### accounts/apps.py

from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts' # this is the default name created by the startapp command
    name = 'simple.apps.accounts'  # for example

###### 
