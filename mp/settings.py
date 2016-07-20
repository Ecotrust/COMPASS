# Django settings for lot project.
from madrona.common.default_settings import *

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TIME_ZONE = 'America/Vancouver'
ROOT_URLCONF = 'urls'
LOGIN_REDIRECT_URL = '/visualize'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'compass',
        'USER': 'postgres',
    }
}

FEEDBACK_RECIPIENT = ["odfwcompass@ecotrust.org"] # default value, actual emails are assigned in settings_local.py
FEEDBACK_SUBJECT = "Compass"


LOG_FILE = os.path.realpath(os.path.join(os.path.dirname(__file__),
                            '..', 'mp.log'))
LOG_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), 'logs'))

ADMIN_MEDIA_PATH = "/usr/local/venv/marine-planner/lib/python2.7/site-packages/django/contrib/admin/static/admin/"

INSTALLED_APPS += ('django_extensions',
                   'social.apps.django_app.default',
                   'general',
                   'scenarios',
                   'data_manager',
                   'mp_settings',
                   'drawing',
                   'explore',
                   'visualize',
                   'django.contrib.humanize',
                   'flatblocks',
                   'mp_proxy',
                   'map_proxy',
                   'content',
                   'tinymce',
                   'django_wysiwyg'
                   )

GEOMETRY_DB_SRID = 3857
GEOMETRY_CLIENT_SRID = 3857  # for latlon
GEOJSON_SRID = 3857
NULLVALUE = -999  # Nulls will be filtered out in the info reports

APP_NAME = "Compass"
SERVER_ADMIN = 'odfwcompass@ecotrust.org'
DEFAULT_FROM_EMAIL = 'ODFW Compass <odfwcompass@ecotrust.org>'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
MANAGERS = ADMINS
EMAIL_SUBJECT_PREFIX = 'ODFW Compass'
ADMINS = (
    ('Ryan Hodges', 'rhodges@ecotrust.org'),
)

FEEDBACK_RECIPIENT = "Compass Team <odfwcompass@ecotrust.org>"
HELP_EMAIL = "odfwcompass@ecotrust.org"
DEFAULT_FROM_EMAIL = "Compass Team <odfwcompass@ecotrust.org>"

# url for socket.io printing
# SOCKET_URL = 'http://ofr.marineplanner.io:8080'
SOCKET_URL = False

# Change the following line to True,
# to display the 'under maintenance' template
UNDER_MAINTENANCE_TEMPLATE = False

TEMPLATE_DIRS = (
    os.path.realpath(os.path.join(os.path.dirname(__file__), 'templates').replace('\\', '/')),
    os.path.realpath(os.path.join(os.path.dirname(__file__), 'mp_profile/templates').replace('\\', '/')),
)


AUTHENTICATION_BACKENDS = (
    # 'social.backends.google.GooglePlusAuth',
    # 'auth.CustomGooglePlusAuth',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

MIDDLEWARE_CLASSES += (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.gzip.GZipMiddleware'

    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main_formatter': {
            'format': '%(levelname)s:%(name)s: %(message)s '
                     '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            # 'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter',
        },
        'production_file':{
            'level' : 'INFO',
            'class' : 'logging.handlers.RotatingFileHandler',
            'filename' : os.path.join(LOG_DIR, 'main.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount' : 7,
            'formatter': 'main_formatter',
            # 'filters': ['require_debug_false'],
        },
        'debug_file':{
            'level' : 'DEBUG',
            'class' : 'logging.handlers.RotatingFileHandler',
            'filename' : os.path.join(LOG_DIR, 'main_debug.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount' : 7,
            'formatter': 'main_formatter',
            # 'filters': ['require_debug_true'],
        },
        'null': {
            "class": 'django.utils.log.NullHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console', 'production_file',],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['null', ],
        },
        'py.warnings': {
            'handlers': ['null', ],
        },
        'apps': {
            'handlers': ['console', 'production_file', 'debug_file'],
            'level': "DEBUG",
        },
        'tracekit': {
            'handlers': ['console', 'production_file', 'debug_file'],
            'level': "DEBUG",
        },
    }
}

ARC_URL_DOMAIN = ''

import logging
logging.getLogger('django.db.backends').setLevel(logging.ERROR)

#For geosearch/geocoding:
POINT_BUFFER = 2500  # meters

DJANGO_WYSIWYG_FLAVOR = "tinymce"    # or "tinymce_advanced"

EXTERNAL_PORT = 80

PLANNING_UNIT_FILENAME = "PU_grid"

PU_FIELDS = {
    'OBJECTID': int,
    'Hex_ID': int,
    'AUSPATID': int,
    'ECOREGION': str,
    'COA_Name': str,
    'habitat': str,
    'fish': str,
    'obs_spec': str,
    'mod_spec': str
}

PU_SQL_LOC = "../media/planning_unit_sql/"
PU_SQL_LIVE = PU_SQL_LOC + "pu_sql.sql"
PU_SQL_BACKUP = PU_SQL_LOC + "pu_sql_backup.sql"

PROCESS_GRID_SCRIPT = "../scripts/process_grid.sh"

SPECIES_LOOKUP = {
    '216': u'Olive-sided Flycatcher',
    '217': u'Willow Flycatcher',
    '214': u'Short-eared Owl',
    '215': u'Common Nighthawk',
    '212': u'Southern Torrent Salamander',
    '213': u'Grasshopper Sparrow',
    '210': u'Northern Red-legged Frog',
    '211': u'Cascade Torrent Salamander',
    '450': u'California Myotis',
    '451': u'Fringed Myotis',
    '452': u'Western Gray Squirrel',
    '453': u'Northern Pacific Pond Turtle',
    '454': u'Western Painted Turtle',
    '455': u'Western Rattlesnake',
    '456': u'Chipping Sparrow',
    '219': u'Acorn Woodpecker',
    '565': u'Bull Trout',
    '584': u'Coho Salmon',
    '595': u'Steelhead, Summer Run',
    '496': u'OCS Habitat - Flowing Water and Riparian',
    '230': u'Northern Pacific Pond Turtle',
    '231': u'Western Painted Turtle',
    '232': u'Chipping Sparrow',
    '559': u'OCS Habitat -  Wetland, high conservation significance',
    '597': u'Steelhead, Winter Run',
    '577': u'Chum Salmon',
    '429': u'Clouded Salamander',
    '209': u'Oregon Slender Salamander',
    '520': u'OCS Habitat - Oak Woodlands',
    '208': u'Clouded Salamander',
    '570': u'Chinook Salmon, Fall Run',
    '502': u'OCS Habitat - Grasslands',
    '586': u'Oregon Chub',
    '449': u'Hoary Bat',
    '448': u'Silver-haired Bat',
    '580': u'Coastal Cutthroat Trout',
    '443': u'Western Purple Martin',
    '442': u'Oregon Vesper Sparrow',
    '441': u'Acorn Woodpecker',
    '440': u'Yellow-breasted Chat',
    '447': u"Townsend's Big-eared Bat",
    '446': u'Western Meadowlark',
    '445': u'Northern Spotted Owl',
    '444': u'Western Bluebird',
    '218': u'Yellow-breasted Chat',
    '229': u'Columbian White-tailed Deer',
    '228': u'Fringed Myotis',
    '227': u'California Myotis',
    '226': u'Silver-haired Bat',
    '225': u"Townsend's Big-eared Bat",
    '224': u'Western Meadowlark',
    '223': u'Northern Spotted Owl',
    '222': u'Western Bluebird',
    '221': u'Western Purple Martin',
    '220': u'Oregon Vesper Sparrow',
    '512': u'OCS Habitat - Natural Lakes',
    '576': u'Chinook Salmon, Spring/Summer Run',
    '532': u'OCS Habitat - Wetland',
    '438': u'Olive-sided Flycatcher',
    '439': u'Willow Flycatcher',
    '436': u'Short-eared Owl',
    '437': u'Common Nighthawk',
    '434': u'Southern Torrent Salamander',
    '435': u'Grasshopper Sparrow',
    '432': u'Cascade Torrent Salamander',
    '433': u'Columbia Torrent Salamander',
    '430': u'Oregon Slender Salamander',
    '431': u'Foothill Yellow-legged Frog'
}

from settings_local import *
