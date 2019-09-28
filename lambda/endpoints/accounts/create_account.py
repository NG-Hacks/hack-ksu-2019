# packages
from botocore.vendored import requests

from .update_account_balance import update_account_balance
from .update_account_owner import update_account_owner

from .. import const

# global
BASE_URL = 'https://us-central1-incomm-hackathon-api.cloudfunctions.net/api'
HEADERS = {
    'X-API-key': 'f9aOcoPNxfVQrxkEQS40',
    'Content-Type':'application/json'
}

def create_account(
    owner:str=None, 
    balance:int=None):
    '''
    '''
    # build request url
    req_url = BASE_URL + '/accounts'

    # make request
    create_account_request = requests.post(
        url=req_url,
        headers=HEADERS)

    # if request was successful
    if create_account_request.status_code == 200:
        new_account = create_account_request.json()
        new_account_id = new_account["id"]
        
        # if owner param was specified, associate the new
        # account with the owner
        if owner:
            updated_owner = update_account_owner(new_account_id, owner)
            
        # if balance param was specified, initialize the account
        # with the balance
        if balance:
            updated_balance = update_account_balance(new_account_id, balance)
            
        return create_account_request.json()