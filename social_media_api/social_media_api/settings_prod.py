"""
Production settings for social_media_api project.
"""

from pathlib import Path
from datetime import timedelta
import dj_database_url
import os

from .settings import *  # import base settings

BASE_DIR = Path(__file__).resolve().parent.parent

# Production mode
DEBUG = False
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "unsafe-secret-key")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost").split(",")

# Whitenoise (keep original middlewares from base)
INSTALLED_APPS += ["whitenoise.runserver_nostatic"]
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# Database
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=False,
    )
}

# Static files
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Security headers
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
