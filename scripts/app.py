
# standard
import logging
from pathlib import Path
import os
import time

# packages
#import numpy

# internal
from utility import const, env

# find current working path
CUR_PATH = Path(__file__).parent

CONFIG_FOLDER = '.config'
LOG_FILE = 'api.log'

CONFIG_PATH = CUR_PATH/CONFIG_FOLDER
CONFIG_FILE_PATH = CONFIG_PATH/'config.json'
LOG_FILE_PATH = CONFIG_PATH/'logs'

logging.basicConfig(
    filename=LOG_FILE_PATH/LOG_FILE,
    level=logging.DEBUG,
    format='%(asctime)s %(message)s'
)

_LOGGER = logging.getLogger(__name__)

if __name__ == '__main__':

    # init context
    _LOGGER.debug('initiailizing context')
    from context.context import Context
    Context.initialize(CONFIG_FILE_PATH)

    BASE_URL = Context.data()[const.BASE_URL]
    HEADERS = Context.data()[const.HEADERS]
    from endpoints.accounts import create_account, accounts_by_owner,list_accounts,delete_account, inspect_account, update_balance, update_owner
    res_by_owner = accounts_by_owner.get_accounts_by_owner(BASE_URL, HEADERS, "user1")
    "Problem with by owner"
    print(res_by_owner)
    