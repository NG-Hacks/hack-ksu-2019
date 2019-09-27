
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

def update_account_owner(
    accountID:str, 
    owner:str, 
    base_url:str=BASE_URL,
    headers:dict=HEADERS):
    '''
    '''
    # build request url
    req_url = base_url + f'/accounts/updateOwner/{accountID}'

    # load data
    data = {
        const.OWNER : owner
    }

    # make request
    update_account_owner_request = requests.put(
        url=req_url, 
        headers=headers, 
        data=json.dumps(data))
    
    # if request was successful
    if update_account_owner_request.status_code == 200:
        update_account_owner_response = {
            const.STATUS : update_account_owner_request.status_code,
            const.DATA : update_account_owner_request.json()
        }

        return update_account_owner_response

    elif update_account_owner_request.status_code == 401:
        _LOGGER.error("Access forbidden, invalid x-api-key")
        return None

    elif update_account_owner_request.status_code == 404:
        _LOGGER.error("Unable to find account")
        return None

    else:
        _LOGGER.error("Unknown error")
        return None
