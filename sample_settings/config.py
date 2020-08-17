import os

PRODUCTION = False
DEBUG = True
SSL = False  # enables ssl_required decorator
SYSTEM_NAME = 'Rhizo Server'  # replace this
EXTENSIONS = []
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///rhizo.db') # format for postgres: 'postgres://[username]:[password]@[hostname]/[db]'
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 8
DEBUG_MESSAGING = False
MESSAGING_LOG_PATH = ''
CSRF_ENABLED = True
CSRF_SESSION_KEY = '[Random String Here]'
SECRET_KEY = '[Random String Here]'
SALT = '[Random String Here]'
KEY_PREFIX = 'RHIZO'  # replace this if you want to identify your keys more easily
TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''
TEXT_FROM_PHONE_NUMBER = ''
S3_ACCESS_KEY = ''
S3_SECRET_KEY = ''
S3_STORAGE_BUCKET = ''
OUTGOING_EMAIL_ADDRESS = ''  # these OUTGOING_EMAIL settings are required if you want to invite people to create accounts
OUTGOING_EMAIL_USER_NAME = ''
OUTGOING_EMAIL_PASSWORD = ''
OUTGOING_EMAIL_SERVER = ''
OUTGOING_EMAIL_PORT = 587
EXTRA_NAV_ITEMS = ''
DOC_FILE_PREFIX = ''

if os.environ.get('AUTOLOAD_EXTENSIONS') in ['True', 'true'] and os.path.exists('./extensions'):
    EXTENSIONS = [o for o in os.listdir('./extensions/') if os.path.isdir(os.path.join('./extensions', o))]
