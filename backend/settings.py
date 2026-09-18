import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ============================================================
# SECURITY
# ============================================================
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-dev-only-change-in-production'
)

DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.up.railway.app',
    '.railway.app',
    'kherwarcalendar.co.in',
    'www.kherwarcalendar.co.in',
]

# ============================================================
# CSRF — Production-এর জন্য অপরিহার্য
# ============================================================
CSRF_TRUSTED_ORIGINS = [
    'https://kherwarcalendar.co.in',
    'https://www.kherwarcalendar.co.in',
    'https://*.up.railway.app',
    'https://*.railway.app',
    'http://127.0.0.1:8000',
    'http://localhost:8000',
]

# Railway reverse proxy-র জন্য
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Cookies
CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'

# ============================================================
# APPLICATIONS
# ============================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
]

# ============================================================
# MIDDLEWARE
# ============================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

# ============================================================
# TEMPLATES
# ============================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# ============================================================
# DATABASE — Railway PostgreSQL + Local SQLite
# ============================================================
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR}/db.sqlite3',
        conn_max_age=600,
        ssl_require=False
    )
}

# ============================================================
# PASSWORD VALIDATORS
# ============================================================
AUTH_PASSWORD_VALIDATORS = []

# ============================================================
# INTERNATIONALIZATION
# ============================================================
LANGUAGE_CODE = 'bn'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# ============================================================
# STATIC & MEDIA FILES
# ============================================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'