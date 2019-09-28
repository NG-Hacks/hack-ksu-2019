
# packages
from botocore.vendored import requests
from .. import const

# global
BASE_URL = 'https://us-central1-incomm-hackathon-api.cloudfunctions.net/api'
HEADERS = {
    'X-API-key': 'f9aOcoPNxfVQrxkEQS40',
    'Content-Type':'application/json'
}

def list_accounts():
    '''
    '''
    # build request url
    req_url = BASE_URL + '/accounts'

    # make request
    accounts_list_request = requests.get(
        url=req_url, 
        headers=HEADERS)

    # if request was successful
    if accounts_list_request.status_code == 200:
        return accounts_list_request.json()

