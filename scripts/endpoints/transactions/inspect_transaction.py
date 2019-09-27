
# standard
from datetime import datetime
import time
import logging
import json

# packages
import requests

# internal
from context.context import Context
from utility import const

_LOGGER = logging.getLogger(__name__)

BASE_URL = Context.data()[const.BASE_URL]
HEADERS = Context.data()[const.HEADERS]

def inspect_transaction(
    accountID:str,
    transactionID:str):
    '''
        This function interacts with the API Endpoint to inspect
        a transaction. 
        Path Params:
            accountID - Account identifier
            transactionID - Transaction identifier
    '''

    req_url = BASE_URL + f'accounts/{accountID}/transactions/{transactionID}'

    resp = requests.get(
        url=req_url,
        headers=HEADERS
    )

    try:
        res = {
            const.STATUS : resp.status_code,
            const.DATA : resp.json()
        }

    except: 
        res = {
            const.STATUS : resp.status_code,
            const.DATA : None
        }
        
    return res