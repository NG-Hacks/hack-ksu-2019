import requests
from utility import const
def inspect_account(base_url:str, headers:dict, account_id:str):
    inspect_account_request = requests.get(base_url+"/accounts/"+account_id, headers=headers)
    if inspect_account_request.status_code == 200:
        inspect_account_response  = {
            const.STATUS:inspect_account_request.status_code,
            const.DATA:inspect_account_request.json()
        }
        return inspect_account_response 
    elif inspect_account_request.status_code == 401:
        print("Access forbidden, invalid x-api-key")
        return None
    elif inspect_account_request.status_code == 404:
        print("Unable to find account")
        return None
    else:
        print("Unknow error")
        return None