
# standard
import json
import logging

# packages
import requests

# internal
from context.context import Context
from utility import const

_LOGGER = logging.getLogger(__name__)

BASE_URL = Context.data()[const.BASE_URL]
HEADERS = Context.data()[const.HEADERS]

def accounts_by_owner(
    owner:str,
    base_url:str=BASE_URL, 
    headers:dict=HEADERS):
    '''
    '''

    req_url = base_url + f'/accounts/owner/{owner}'

    # load params for request
    params = {
        const.OWNER : owner
    }

    # make request
    accounts_by_owner_request = requests.get(
        url=req_url,
        params=json.dumps(params))

    # if request was successful
    if accounts_by_owner_request.status_code == 200:
        accounts_by_owner_response = {
            const.STATUS:accounts_by_owner_request.status_code,
            const.DATA:accounts_by_owner_request.json()
        }

        return accounts_by_owner_response

    elif accounts_by_owner_request.status_code == 401:
        _LOGGER.error("Access forbidden, invalid x-api-key")
        return None
        
    elif accounts_by_owner_request.status_code == 404:
        _LOGGER.error("Unable to find account")
        return None

    else:
        _LOGGER.error("Unknown error")
        return None
