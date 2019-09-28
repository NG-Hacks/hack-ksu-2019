# packages
from botocore.vendored import requests
import json
from .. import const

# global
BASE_URL = 'https://us-central1-incomm-hackathon-api.cloudfunctions.net/api'
HEADERS = {
    'X-API-key': 'f9aOcoPNxfVQrxkEQS40',
    'Content-Type':'application/json'
}

def update_account_balance(
    accountID:str,
    balance:int):
    '''
    '''
    # build request url
    req_url = BASE_URL + f'/accounts/updateBalance/{accountID}'

    # load data
    data = {
        const.BALANCE : balance
    }

    # make request
    update_account_balance_request = requests.put(
        url=req_url, 
        headers=HEADERS, 
        data=json.dumps(data))

    # if request was successful
    if update_account_balance_request.status_code == 200:
        return update_account_balance_request.json()
