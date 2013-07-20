import sys


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'imanhodjaev',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}


DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}


EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
# EMAIL_HOST = 'smtp.webfaction.com'
# EMAIL_HOST_USER = 'pikir'
# EMAIL_PORT = 25
# EMAIL_USER = 'pikir'
# EMAIL_HOST_PASSWORD = 'pikir-mail'
# DEFAULT_FROM_EMAIL = 'pikir@pikir.kg'
# SERVER_EMAIL = 'pikir@pikir.kg'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
THUMBNAIL_DEBUG = True


if 'test' in sys.argv:
    try:
        from test_db import *
    except ImportError:
        pass
