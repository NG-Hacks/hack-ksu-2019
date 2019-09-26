
# standard
import logging
from pathlib import Path

# packages

# internal
from utility import const, env

# find current working path
CUR_PATH = Path(__file__).parent

CONFIG_FOLDER = '.config'
CONFIG_PATH = CUR_PATH/CONFIG_FOLDER
CONFIG_FILE_PATH = CONFIG_PATH/'config.json'

if env.LOG_TO_FILE:
    LOG_FILE = 'api.log'
    LOG_FILE_PATH = CONFIG_PATH/'logs'
    logging.basicConfig(
        filename=LOG_FILE_PATH/LOG_FILE,
        level=env.LOGGING_LEVEL,
        format='%(asctime)s %(message)s',
    )

else:
    logging.basicConfig(
        level=env.LOGGING_LEVEL,
        format='%(asctime)s %(message)s'
    )

_LOGGER = logging.getLogger(__name__)

if __name__ == '__main__':

    # init context
    _LOGGER.info('initiailizing context')
    from context.context import Context
    Context.initialize(CONFIG_FILE_PATH)

    from endpoints.accounts.list_accounts import list_accounts
    res = list_accounts()
    data = res[const.DATA]
    for account in data[const.ACCOUNTS]:
        print(account[const.ID])

    from endpoints.transactions.list_transactions import list_transactions
    res = list_transactions(accountID='cRXWSTSjI6WT2EYQeshT')
    