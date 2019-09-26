
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

def list_transactions(
    accountID:str,
    after:str=None,
    before:str=None,
    transactionType:str=None,
    counterParty:str=None,
    pageSize:int=20,
    pageOffset:int=0):
    '''
        This function interacts with the API Endpoint to create
        a transaction on the specified account.
    '''

    req_url = BASE_URL + f'/{accountID}/transactions'

    data = {
        const.AFTER : after,
        const.BEFORE : before,
        const.TYPE : transactionType,
        const.COUNTER_PARTY : counterParty,
        const.PAGE_SIZE : pageSize,
        const.PAGE_OFFSET : pageOffset
    }

    resp = requests.get(
        url=req_url,
        headers=HEADERS,
        data=json.dumps(data)
    )

    res = {
        const.STATUS : resp.status_code,
        const.TEXT : resp.text
    }

    return res