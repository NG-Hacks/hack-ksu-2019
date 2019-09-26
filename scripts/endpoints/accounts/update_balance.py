
# standard
import logging
import json

# packages
import requests

# internal
from utility import const
from context.context import Context

_LOGGER = logging.getLogger(__name__)

BASE_URL = Context.data()[const.BASE_URL]
HEADERS = Context.data()[const.HEADERS]

def update_balance(
    account_id:str,
    balance:int,
    base_url:str=BASE_URL, 
    headers:dict=HEADERS):
    '''
    '''
    if not isinstance(balance, int):
        _LOGGER.error('Balance not of type integer')
        return None

    req_url = base_url + f'/accounts/updateBalance/{account_id}'

    data = {
        const.BALANCE : balance
    }

    update_account_balance_request = requests.put(
        url=req_url, 
        headers=headers, 
        data=json.dumps(data))

    if update_account_balance_request.status_code == 200:
        update_account_balance_response = {
            const.STATUS:update_account_balance_request.status_code,
            const.DATA:update_account_balance_request.json()
        }

        return update_account_balance_response

    elif update_account_balance_request.status_code == 401:
        _LOGGER.error("Access forbidden, invalid x-api-key")
        return None

    elif update_account_balance_request.status_code == 404:
        _LOGGER.error("Unable to find account")
        return None

    else:
        _LOGGER.error("Unknown error")
        return None