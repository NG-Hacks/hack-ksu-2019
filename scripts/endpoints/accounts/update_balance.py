import requests
import json
from utility import const
def update_account_balance(base_url:str, headers:dict, account_id:str, balance:int):
    if type(balance)!=type(1):
        print("Balance should be an integer!")
        return None
    balance_data = json.dumps({"balance": balance})
    update_account_balance_request = requests.put(base_url+"/accounts/updateBalance/"+account_id, headers=headers, data=balance_data)
    if update_account_balance_request.status_code == 200:
        update_account_balance_response = {
            const.STATUS:update_account_balance_request.status_code,
            const.DATA:update_account_balance_request.json()
        }
        return update_account_balance_response
    elif update_account_balance_request.status_code == 401:
        print("Access forbidden, invalid x-api-key")
        return None
    elif update_account_balance_request.status_code == 404:
        print("Unable to find account")
        return None
    else:
        print("Unknow error")
        return None