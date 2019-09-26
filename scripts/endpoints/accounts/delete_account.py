import requests
from utility import const

def delete_account(base_url:str, account_id:str, headers:dict):
    delete_account_request = requests.delete(base_url+"/accounts/"+account_id, headers=headers)
    if delete_account_request.status_code == 200:
        delete_account_response  = {
            const.STATUS:delete_account_response.status_code,
            const.DATA:delete_account_response.json()
        }
        return delete_account_response 
    elif delete_account_request.status_code == 401:
        print("Access forbidden, invalid x-api-key")
        return None
    elif delete_account_request.status_code == 404:
        print("Unable to find account")
        return None
    else:
        print("Unknow error")
        return None