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

def accounts_by_owner(owner:str):
    '''
    '''
    # build request url
    req_url = BASE_URL + f'/accounts/owner/{owner}'

    # load params for request
    params = {
        'owner' : owner
    }

    # make request
    accounts_by_owner_request = requests.get(
        url=req_url,
        headers=HEADERS,
        params=json.dumps(params))

    # if request was successful
    if accounts_by_owner_request.status_code == 200:
        return accounts_by_owner_request.json()
    else:
        return 'Error'