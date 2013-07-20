import os

here = lambda * x: os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), *x))

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ENV = os.getenv('ENV', 'dev')
PROJECT_NAME = 'imanhodjaev'
PROJECT_ROOT = here('../..')

root = lambda * x: os.path.abspath(os.path.join(os.path.abspath(PROJECT_ROOT), *x))


DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = '89%29-=#c9f*@cx*lxv%6s%-j@etf*2)%f)bm2pzxuo8jo$n&t'
AUTH_USER_MODEL = 'my_auth.User'

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


MY_APPS = [
    'apps.util',
    'apps.front',
    'apps.project',
    'apps.my_auth',
]


INSTALLED_APPS = DJANGO_APPS + MY_APPS
ROOT_URLCONF = 'imanhodjaev.urls'
WSGI_APPLICATION = 'imanhodjaev.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'


def extend_list_avoid_repeats(list_to_extend, extend_with):
    """
    Extends the first list with the elements in the second one,
    making sure its elements are not already there in the original list.
    """
    list_to_extend.extend(filter(lambda x: not list_to_extend.count(x), extend_with))
