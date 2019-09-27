
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
    # build request url
    req_url = BASE_URL + f'/accounts/{accountID}/transactions'

    # load params
    params = {
        const.ID : accountID
    }

    if after:
        params[const.AFTER] = after
    if before:
        params[const.BEFORE] = before
    if transactionType:
        params[const.TYPE] = transactionType
    if counterParty:
        params[const.COUNTER_PARTY] = counterParty
    if pageSize:
        params[const.PAGE_SIZE] = pageSize
    if pageOffset:
        params[const.PAGE_OFFSET] = pageOffset

    # make request
    resp = requests.get(
        url=req_url,
        headers=HEADERS,
        params=json.dumps(params)
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