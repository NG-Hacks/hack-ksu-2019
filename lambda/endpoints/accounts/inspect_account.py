# packages
from botocore.vendored import requests
from .. import const

# global
BASE_URL = 'https://us-central1-incomm-hackathon-api.cloudfunctions.net/api'
HEADERS = {
    'X-API-key': 'f9aOcoPNxfVQrxkEQS40',
    'Content-Type':'application/json'
}

def inspect_account(accountID:str):
    '''
    '''
    # build request url
    req_url = BASE_URL + f'/accounts/{accountID}'

    # make request
    inspect_account_request = requests.get(
        url=req_url, 
        headers=HEADERS)

    # if request was successful
    if inspect_account_request.status_code == 200:

        return inspect_account_request.json()