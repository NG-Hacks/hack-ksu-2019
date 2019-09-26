
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

def post_transaction(
    accountID:str,
    counterParty:str,
    transactionType:str,
    description:str,
    amount:int,
    date:datetime=None):
    '''
        This function interacts with the API Endpoint to create
        a transaction on the specified account.
    '''

    req_url = BASE_URL + f'/accounts/{accountID}/transactions'

    data = {
        const.COUNTER_PARTY : counterParty,
        const.TYPE : transactionType,
        const.DESC : description,
        const.AMOUNT : amount,
    }

    # if a date is not specified, the api will fill
    # in the date with the current time
    if date:
        data[const.DATE] = date

    resp = requests.post(
        url=req_url,
        headers=HEADERS,
        data=json.dumps(data)
    )

    res = {
        const.STATUS : resp.status_code,
        const.TEXT : resp.text
    }

    return res