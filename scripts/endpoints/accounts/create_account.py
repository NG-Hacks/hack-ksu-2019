import requests
from utility import const

def create_account(base_url:str, headers:dict):
    create_account_request = requests.post(base_url+"/accounts", headers = headers)
    if create_account_request.status_code == 200:
        create_respose = {
            const.STATUS:create_account_request.status_code,
            const.DATA:create_account_request.json()
        }
        return create_respose
    elif create_account_request.status_code == 401:
        print("Access forbidden, invalid x-api-key")
        return None
    elif create_account_request.status_code == 404:
        print("Unable to find account")
        return None
    else:
        print("Unknow error")
        return None