# Django settings for brisket project.
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DEBUG = True

SENTRY_ADMINS = (
    # So Sentry will send emails
    'arowland@sunlightfoundation.com',
)

DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/some-other-media-folder/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '(1yv=vnhqrvj%qjr%zd)fe*cr4785a#7$ju8km4%+tnscm&p_r'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
    'postcards.cookie.SessionMiddleware',
    'data.middleware.DataRedirectMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'influence.context_processors.custom_context',
    'data.context_processors.custom_context',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'brisket.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
#    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize', #format numbers in templates
    'django.contrib.sitemaps',
    'mediasync',
#    'simplepay',
    'brisket.influence',
    'brisket.util',
#    'django.contrib.admin',
    'django_nose',
    'sentry',
    'raven.contrib.django',
    'indexer',
    'paging',
    'gunicorn',
    'feedinator',
    'fec',
    'data',
)

#DATABASE_ROUTERS = ['db_router.BrisketDBRouter']

# use file-backed sessions while in development. the default location
# for file-backed sessions is tempfile.gettempdir(), most likely /tmp.
# this can be customized with the SESSION_FILE_PATH variable either
# here or in local_settings.py.
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

EMAIL_SUBJECT_PREFIX = '[Brisket] '

LATEST_CYCLE = 2012
TOP_LISTS_CYCLE = 2012

SESSION_COOKIE_NAME = 'brisket_session'

SIMPLEPAY_COMPLETE_REDIRECT = '/postcard/thanks'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

SELENIUM_HOST = '0.0.0.0'
SELENIUM_PORT = 4444 # default
SELENIUM_BROWSER_COMMAND = 'firefox'
SELENIUM_URL_ROOT = 'http://localhost:8001'
#FORCE_SELENIUM_TESTS = False # default

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

from local_settings import *

MEDIASYNC['JOINED'] = {
    'js/brisket-all.js': [
        'js/jquery.tablesorter.min.js',
        'js/jquery.json-2.3.min.js',
        'js/underscore-min.js',
        'js/brisket.js',
        'js/d3.min.js',
        'js/d3.geom.min.js',
        'js/brisket_d3.js',
    ],
    'data/css/all.css': [
        'data/css/ui-lightness/jquery-ui-1.7.2.custom.css',
        'data/css/jquery.autocomplete.css',
        'data/css/main.css',
    ],
    'data/css/3rdparty.css': [
        'data/css/ui-lightness/jquery-ui-1.7.2.custom.css',
        'data/css/jquery.autocomplete.css',
    ],
    'data/3rdparty.js': [
        'data/js/jquery-ui-1.7.2.custom.min.js',
        'data/js/jquery.currency.js',
        'data/js/jquery.expander.js'
    ],
    'data/3rdparty_old.js': [
        'data/js/jquery-1.4.2.min.js',
        'data/js/jquery-ui-1.7.2.custom.min.js',
        'data/js/jquery.currency.js',
        'data/js/underscore-min.js',
        'data/js/jquery.expander.js'
    ],
    'data/contracts.js': [
        'data/js/td.js',
        'data/js/td.fields.js',
        'data/js/td.contracts.js'
    ],
    'data/contractor_misconduct.js': [
        'data/js/td.js',
        'data/js/td.fields.js',
        'data/js/td.contractor_misconduct.js'
    ],
    'data/contributions.js': [
        'data/js/td.js',
        'data/js/td.fields.js',
        'data/js/td.contributions.js'
    ],
    'data/earmarks.js': [
        'data/js/td.js',
        'data/js/td.fields.js',
        'data/js/td.earmarks.js'
    ],
    'data/grants.js': [
        'data/js/td.js',
        'data/js/td.fields.js',
        'data/js/td.grants.js'
    ],
    'data/lobbying.js': [
        'data/js/td.js',
        'data/js/td.fields.js',
        'data/js/td.lobbying.js'
    ],
    'data/faca.js': [
        'data/js/td.js',
        'data/js/td.fields.js',
        'data/js/td.faca.js'
    ],
    'data/bundling.js': [
        'data/js/td.js',
        'data/js/td.fields.js',
        'data/js/td.bundling.js'
    ],
    'data/epa_echo.js': [
        'data/js/td.js',
        'data/js/td.fields.js',
        'data/js/td.epa_echo.js'
    ],
    'data/index.js': [
        'data/js/td.js',
        'data/js/td.fields.js',
        'data/js/td.contracts.js',
        'data/js/td.earmarks.js',
        'data/js/td.grants.js',
        'data/js/td.lobbying.js',
        'data/js/td.contributions.js',
        'data/js/td.contractor_misconduct.js',
        'data/js/td.epa_echo.js',
        'data/js/td.faca.js',
        'data/js/td.bundling.js'
    ],
}

from influenceexplorer import InfluenceExplorer
api = InfluenceExplorer(API_KEY, AGGREGATES_API_BASE_URL)
