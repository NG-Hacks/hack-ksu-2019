import requests
import json
from utility import const
def accounts_by_owner(base_url:str, owner:str, headers:dict):
    params = json.dumps({"onwer":owner})
    accounts_by_owner_request = requests.get(
        base_url+"accounts/owner/"+owner,
        params=params
    )
    if accounts_by_owner_request.status_code == 200:
        
        accounts_by_owner_response = {
            const.STATUS:accounts_by_owner_request.status_code,
            const.DATA:accounts_by_owner_request.json()
        }
        return accounts_by_owner_response
    elif accounts_by_owner_request.status_code == 401:
        print("Access forbidden, invalid x-api-key")
        return None
    elif accounts_by_owner_request.status_code == 404:
        print("Unable to find account")
        return None
    else:
        print("Unknow error")
        return None
