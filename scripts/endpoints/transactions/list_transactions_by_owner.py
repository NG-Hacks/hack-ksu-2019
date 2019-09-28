
# standard
import logging
import json

# packages
import requests

# internal
from context.context import Context
from utility import const
from .list_transactions import list_transactions
from endpoints.accounts.accounts_by_owner import accounts_by_owner

_LOGGER = logging.getLogger(__name__)

BASE_URL = Context.data()[const.BASE_URL]
HEADERS = Context.data()[const.HEADERS]

def list_transactions_by_owner(owner:str):
    '''
    '''
    accounts = accounts_by_owner(owner)[const.DATA][const.ACCOUNTS]

    transactions_list = []
    for account in accounts:
        transactions = list_transactions(accountID=account[const.ID])[const.DATA]
        for transaction in transactions:
            transactions_list.append(transaction)

    return transactions_list