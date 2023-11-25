"""
Django settings for glazgo project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os

from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Режим продукции

ALLOWED_HOSTS = ["*"]  # Режим продукции

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Авторизация ↓
    "rest_framework",
    "rest_framework.authtoken",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    # Другие необходимые инструменты ↓
    "drf_yasg",
    "django_filters",
    "channels",
    "corsheaders",
    "import_export",
    # Приложения ↓
    "ats",
    "users",
    "chat",
    "referral_system",
]

MIDDLEWARE = [
    # "csp.middleware.CSPMiddleware",  # Режим продукции
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "glazgo.urls"

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

WSGI_APPLICATION = "glazgo.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# DATABASES = {  # Режим продукции
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.getenv("DB_NAME"),
#         "USER": os.getenv("FSTR_DB_LOGIN"),
#         "PASSWORD": os.getenv("FSTR_DB_PASS"),
#         "HOST": os.getenv("FSTR_DB_HOST"),
#         "PORT": os.getenv("FSTR_DB_PORT"),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ASGI_APPLICATION = "glazgo.asgi.application"

# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

SITE_ID = 1

CORS_ALLOW_ALL_ORIGINS = True  # Режим продукции

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
}

REST_AUTH = {
    "OLD_PASSWORD_FIELD_ENABLED": True,
    "LOGOUT_ON_PASSWORD_CHANGE": True,
    "REGISTER_SERIALIZER": "users.serializers.CustomRegisterSerializer",
    "USER_DETAILS_SERIALIZER": "users.serializers.UserDetailsSerializer",
}

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

AUTH_USER_MODEL = "users.User"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [
                (
                    f"redis://{os.getenv('PASSWORD')}@{os.getenv('HOST')}:{os.getenv('PORT')}"
                )
            ],
        },
    },
}

################################################################

# Разкомментируйте эти переменные в режиме продукции !!!

# Контрольный список безопасности !!!

# Чтобы сообщить браузеру, что он никогда не должен загружать сайт
# с использованием HTTP и вместо этого должен автоматически преобразовывать
# все попытки доступа к сайту с использованием HTTP в запросы HTTPS.
# SECURE_HSTS_SECONDS = 15780000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# Чтобы заблокировать загрузку страниц при обнаружении отраженных XSS-атак
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True

# Чтобы избежать случайной передачи файла cookie CSRF по HTTP.
# CSRF_COOKIE_SECURE = True

# Чтобы избежать случайной передачи файла cookie сеанса по HTTP.
# SESSION_COOKIE_SECURE = True

# Чтобы Django перенаправлял все запросы, отличные от HTTPS, на HTTPS.
# SECURE_SSL_REDIRECT = True

# Политика безопасности контента (CSP)
# CSP_DEFAULT_SRC = ("'none'", )
# CSP_BASE_URI = ("'none'", )
# CSP_FRAME_ANCESTORS = ("'none'", )
# CSP_FORM_ACTION = ("'self'", )
# CSP_STYLE_SRC = ("'self'", )
# CSP_SCRIPT_SRC = ("'self'", )
# CSP_IMG_SRC = ("'self'", )
# CSP_FONT_SRC = ("'self'", )

# Чтобы проверить соответствует ли приложение списку безопасности
# python manage.py check --deploy

################################################################
