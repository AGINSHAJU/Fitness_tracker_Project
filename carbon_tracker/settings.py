import os
from pathlib import Path

# Base directory for the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security: Replace this with a secure key in production
SECRET_KEY = 'django-insecure-your-secret-key-here'  # Generate a new one for production

# Debug mode for development
DEBUG = True

# Allowed hosts (add your domain in production)
ALLOWED_HOSTS = []

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'widget_tweaks',
    'django.contrib.staticfiles',
    'tracker',  # Your custom app
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Required for allauth
]

# URL configuration
ROOT_URLCONF = 'carbon_tracker.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Look for templates in the templates/ folder
        'APP_DIRS': True,  # Also look in app-specific template dirs (e.g., tracker/templates/)
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required for allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'carbon_tracker.wsgi.application'

# Database configuration (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'carbon_tracker_db',
        'USER': 'postgres',
        'PASSWORD': 'admin',  # Ensure this matches your PostgreSQL password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',  # For allauth
]

# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Directory for custom static files (e.g., local Bootstrap)
]
STATIC_ROOT = BASE_DIR / "staticfiles"  # Where collectstatic will gather files

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django-allauth settings
LOGIN_REDIRECT_URL = '/'  # Redirect to dashboard after login
ACCOUNT_LOGOUT_REDIRECT_URL = '/'  # Redirect to dashboard after logout
ACCOUNT_SIGNUP_REDIRECT_URL = '/'  # Redirect to dashboard after signup
ACCOUNT_EMAIL_REQUIRED = True  # Require email for signup (optional)
ACCOUNT_USERNAME_REQUIRED = True  # Require username (optional)
ACCOUNT_AUTHENTICATION_METHOD = 'username'  # Use username for login (can be 'email')
ACCOUNT_LOGOUT_ON_GET = True  # Logs out immediately on GET request
ACCOUNT_EMAIL_VERIFICATION = 'none'  # Disable email verification for simplicity (optional)
LOGIN_REDIRECT_URL = '/'  # Points to front_page