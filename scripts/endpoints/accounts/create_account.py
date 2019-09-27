
# standard
import logging

# packages
import requests

# internal
from utility import const
from context.context import Context
from .update_account_balance import update_account_balance
from .update_account_owner import update_account_owner

_LOGGER = logging.getLogger(__name__)

BASE_URL = Context.data()[const.BASE_URL]
HEADERS = Context.data()[const.HEADERS]

def create_account(
    base_url:str=BASE_URL, 
    headers:dict=HEADERS, 
    owner:str=None, 
    balance:int=None):
    '''
    '''
    # build request url
    req_url = base_url + '/accounts'

    # make request
    create_account_request = requests.post(
        url=req_url,
        headers = headers)

    # if request was successful
    if create_account_request.status_code == 200:
        _LOGGER.debug('Account created.')

        new_account = create_account_request.json()
        new_account_id = new_account["id"]

        # if owner param was specified, associate the new
        # account with the owner
        if owner:
            updated_owner = update_account_owner(new_account_id, owner)
            _LOGGER.debug("Updated owner:", updated_owner)

        # if balance param was specified, initialize the account
        # with the balance
        if balance:
            updated_balance = update_account_balance(new_account_id, balance)
            _LOGGER.debug("Updated balance: ", updated_balance)
            
        create_response = {
            const.STATUS:create_account_request.status_code,
            const.DATA:create_account_request.json()
        }

        return create_response

    elif create_account_request.status_code == 401:
        _LOGGER.error("Access forbidden, invalid x-api-key")
        return None

    elif create_account_request.status_code == 404:
        _LOGGER.error("Unable to find account")
        return None

    else:
        _LOGGER.error("Unknown error")
        return None