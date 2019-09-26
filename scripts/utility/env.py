
# standard
import logging

# internal
from . import const

ENV_BASE = 'HACK_KSU_'

BASE_URL = ENV_BASE + const.BASE_URL
API_KEY = ENV_BASE + const.API_KEY
CONTENT_TYPE = ENV_BASE + 'CONTENT_TYPE'

# change to true if you wish to log to file
LOG_TO_FILE = False
LOGGING_LEVEL = logging.INFO