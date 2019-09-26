import requests
from utility import const
def get_accounts_list(base_url:str, headers:dict):
        accounts_list_request = requests.get(base_url+"/accounts", headers=headers)
        if accounts_list_request.status_code == 200:
            accounts_list_response = {
                const.STATUS:accounts_list_request.status_code,
                const.DATA:accounts_list_request.json()
            }
            return accounts_list_response
        elif accounts_list_request.status_code == 401:
            print("Access forbidden, invalid x-api-key")
            return None
            
        elif accounts_list_request.status_code == 404:
            print("Unable to find account")
            return None
        else:
            print("Unknow error")
            return None