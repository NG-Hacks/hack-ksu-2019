from update_balance import update_account_balance
from update_owner import update_account_owner
from utility import const

def create_account(base_url:str, headers:dict, owner:str=None, balance:int=None):
    create_account_request = requests.post(base_url+"/accounts", headers = headers)
    if create_account_request.status_code == 200:
        print("create account!")
        new_account = create_account_request.json()
        print(new_account)
        new_account_id = new_account["id"]
        if owner != None:
            updated_owner = update_account_owner(new_account_id, owner)
            print("Updated owner:", updated_owner)
            if updated_owner == None:
                //todo
        if balance != None:
            updated_balance = update_account_balance(new_account_id, balance)
            print("Updated balance: ", updated_balance)
            if update_account_balance == None:
                //todo
        create_respose = {
            const.STATUS:create_account_request.status_code,
            const.DATA:create_account_request.json()
        }
        return create_respose
        print(self.get_accounts_list())
    elif create_account_request.status_code == 401:
        print("Access forbidden, invalid x-api-key")
        return None
    elif create_account_request.status_code == 404:
        print("Unable to find account")
        return None
    else:
        print("Unknow error")
        return None