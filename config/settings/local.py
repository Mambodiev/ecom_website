from .base import *  # noqa
from .base import env


DEBUG = True
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="Vqxj2i23Kkc8x9QIhP7Y0qjwjGd9AYCqXyWkIzComhQLnmKmoZETo38k2VJfOA00",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025


INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
    'SHOW_TOOLBAR_CALLBACK': lambda r: False,  # disables i
}
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

INSTALLED_APPS += ["django_extensions"]  # noqa F405

