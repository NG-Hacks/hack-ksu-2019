
# standard
import logging

# packages
import requests

# internal
from utility import const
from context.context import Context

_LOGGER = logging.getLogger(__name__)

BASE_URL = Context.data()[const.BASE_URL]
HEADERS = Context.data()[const.HEADERS]

def list_accounts(
    base_url:str=BASE_URL,
    headers:dict=HEADERS):
    '''
    '''
    # build request url
    req_url = base_url + '/accounts'

    # make request
    accounts_list_request = requests.get(
        url=req_url, 
        headers=headers)

    # if request was successful
    if accounts_list_request.status_code == 200:
        accounts_list_response = {
            const.STATUS:accounts_list_request.status_code,
            const.DATA:accounts_list_request.json()
        }

        return accounts_list_response

    elif accounts_list_request.status_code == 401:
        _LOGGER.error("Access forbidden, invalid x-api-key")
        return None
        
    elif accounts_list_request.status_code == 404:
        _LOGGER.error("Unable to find account")
        return None
    else:
        _LOGGER.error("Unknown error")
        return None
