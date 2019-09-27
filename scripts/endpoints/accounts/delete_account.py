import requests
from utility import const

def delete_account(base_url:str, headers:dict, account_id:str):
    delete_account_request = requests.delete(base_url+"/accounts/"+account_id, headers=headers)
    if delete_account_request.status_code == 204:
        print("Delete account: ", account_id," Successfully!")
        return delete_account_request.status_code
    elif delete_account_request.status_code == 401:
        print("Access forbidden, invalid x-api-key")
        return None
    else:
        print("Unknow error")
        return None