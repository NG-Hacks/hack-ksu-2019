
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

def delete_account(
    accountID:str,
    base_url:str=BASE_URL, 
    headers:dict=HEADERS):
    '''
    '''
    # build request url
    req_url = base_url + f'/accounts/{accountID}'

    # make request
    delete_account_request = requests.delete(
        url=req_url, 
        headers=headers)

    # if request was successful
    if delete_account_request.status_code == 200:
        delete_account_response = {
            const.STATUS:delete_account_response.status_code,
            const.DATA:delete_account_response.json()
        }

        return delete_account_response 

    elif delete_account_request.status_code == 401:
        _LOGGER.error("Access forbidden, invalid x-api-key")
        return None

    elif delete_account_request.status_code == 404:
        _LOGGER.error("Unable to find account")
        return None

    else:
        _LOGGER.error("Unknow error")
        return None