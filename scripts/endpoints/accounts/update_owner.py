import requests
import json
from utility import const
def update_account_owner(base_url:str, account_id:str, owner:str, headers:dict):
    balance_data = json.dumps({"owner": owner})
    update_account_owner_request = requests.put(base_url+"/accounts/updateOwner/"+account_id, headers=headers, data=balance_data)
    
    if update_account_owner_request.status_code == 200:
        update_account_owner_response = {
            const.STATUS : update_account_owner_request.status_code,
            const.DATA : update_account_owner_request.json()
        }

        return update_account_owner_response
    elif update_account_owner_request.status_code == 401:
        print("Access forbidden, invalid x-api-key")
        return None
    elif update_account_owner_request.status_code == 404:
        print("Unable to find account")
        return None
    else:
        print("Unknow error")
        return None