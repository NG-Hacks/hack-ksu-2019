
# standard
import logging
from pathlib import Path
from datetime import datetime

# packages

# internal
from utility import const, env

# find current working path
CUR_PATH = Path(__file__).parent

# locate config file
CONFIG_FOLDER = '.config'
CONFIG_PATH = CUR_PATH/CONFIG_FOLDER
CONFIG_FILE_PATH = CONFIG_PATH/'config.json'

# if user wants to log to file
if env.LOG_TO_FILE:
    # locate log file
    LOG_FILE = 'api.log'
    LOG_FILE_PATH = CONFIG_PATH/'logs'
    logging.basicConfig(
        filename=LOG_FILE_PATH/LOG_FILE,
        level=env.LOGGING_LEVEL,
        format='%(asctime)s %(message)s'
    )

else:
    # otherwise, log to terminal
    logging.basicConfig(
        level=env.LOGGING_LEVEL,
        format='%(asctime)s %(message)s'
    )

_LOGGER = logging.getLogger(__name__)

if __name__ == '__main__':

    # init context
    _LOGGER.info('initializing context')
    from context.context import Context
    Context.initialize(CONFIG_FILE_PATH)

    # init endpoints
    _LOGGER.info('initializing endpoints')
    from endpoints import Endpoints
    Endpoints.initialize()
    
    # Endpoints.post_transaction(
    #     accountID='88efgiTlszS1z2TqSlPj',
    #     counterParty='suntrust',
    #     transactionType='debit',
    #     description='ATM Withdrawal',
    #     amount='20'
    # )

    # Endpoints.post_transaction(
    #     accountID='88efgiTlszS1z2TqSlPj',
    #     counterParty='suntrust',
    #     transactionType='credit',
    #     description='ATM Deposit',
    #     amount='100'
    # )

    #res = Endpoints.create_account(owner='Anthony')

    # init connection
    # this init references the conn object
    # because the object stores data in tables

    # _LOGGER.info('initializing connection')
    # from connection import conn
    # conn._initialize()

    def get_accounts_by_owner(owner:str):
        accounts_list = Endpoints.list_accounts()[const.DATA][const.ACCOUNTS]
        owner_account = []
        for account in accounts_list:
            if const.OWNER in account:
                if account[const.OWNER] == owner:
                    owner_account.append(account)
        return owner_account
    
    #Endpoints.delete_account('mYXarTIsGL5hfbUeRGC6')
    #res = Endpoints.accounts_by_owner(owner='Anthony')

    res = Endpoints.list_accounts()

    #res = Endpoints.accounts_by_owner(owner='Steve')
    print('done')