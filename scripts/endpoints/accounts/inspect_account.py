
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

def inspect_account(
    account_id:str,
    base_url:str=BASE_URL,
    headers:dict=HEADERS):
    '''
    '''
    # build request url
    req_url = base_url + f'/accounts/{account_id}'

    # make request
    inspect_account_request = requests.get(
        url=req_url, 
        headers=headers)

    # if request was successful
    if inspect_account_request.status_code == 200:
        inspect_account_response = {
            const.STATUS:inspect_account_response.status_code,
            const.DATA:inspect_account_response.json()
        }

        return inspect_account_response 

    elif inspect_account_request.status_code == 401:
        _LOGGER.error("Access forbidden, invalid x-api-key")
        return None

    elif inspect_account_request.status_code == 404:
        _LOGGER.error("Unable to find account")
        return None

    else:
        _LOGGER.error("Unknown error")
        return None