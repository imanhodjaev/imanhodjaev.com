import sys


DEBUG = False
IS_PROD = True
IS_DEV = False
DOMAIN_NAME = 'http://pikir.kg'
MEDIA_ROOT = '/home/imanhodjaev/media/petitions/media'
STATIC_ROOT = '/home/imanhodjaev/media/petitions/static'
MEDIA_URL = '/m/'
STATIC_URL = '/s/'
THUMBNAIL_DEBUG = True
COMPRESS_ENABLED = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pikir',
        'USER': 'root',
        'PASSWORD': 'MyR00t',
        'HOST': '',
        'PORT': '',
    }
}


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:27504',
        'OPTIONS': {
            'DB': 1,
            'PASSWORD': '',
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        },
    },
}


EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'pikir'
EMAIL_PORT = 25
EMAIL_USER = 'pikir'
EMAIL_HOST_PASSWORD = 'pikir-mail'
DEFAULT_FROM_EMAIL = 'pikir@pikir.kg'
SERVER_EMAIL = 'pikir@pikir.kg'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


if 'test' in sys.argv:
    try:
        from test_db import *
    except ImportError:
        pass
