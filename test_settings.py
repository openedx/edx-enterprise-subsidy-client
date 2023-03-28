"""
These settings are here to use during tests, because django requires them.

In a real-world use case, apps in this project are installed into other
Django applications, so these settings will not be used.
"""

from os.path import abspath, dirname, join


def root(*args):
    """
    Get the absolute path of the given path relative to the project root.
    """
    return join(abspath(dirname(__file__)), *args)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'default.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'edx_rest_api_client',
)

LOCALE_PATHS = [
    root('edx_rest_api_client', 'conf', 'locale'),
]

ROOT_URLCONF = 'edx_rest_api_client.urls'

SECRET_KEY = 'insecure-secret-key'

OAUTH2_PROVIDER_URL = 'backend-service-oauth-provider-url'
BACKEND_SERVICE_EDX_OAUTH2_KEY = 'your-services-application-key'
BACKEND_SERVICE_EDX_OAUTH2_SECRET = 'your-services-application-secret'
ENTERPRISE_SUBSIDY_URL = 'enterprise-subsidy-service-base-url'
