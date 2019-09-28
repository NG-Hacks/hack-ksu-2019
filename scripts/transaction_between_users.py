from endpoints.accounts import list_accounts
from endpoints.transactions import post_transaction

# packages
import requests

# internal
from context.context import Context
from utility import const, get_current_time
from utility.errors import PostTransactionError


def get_accounts_by_owner(owner:str):
    accounts_list = list_accounts.list_accounts()[const.DATA][const.ACCOUNTS]
    ower_account = []
    for account in accounts_list:
        if const.OWNER in account:
            if account[const.OWNER] == owner:
                ower_account.append(account)
    return ower_account


def transaction_between_users(
    sourceOwner:str,
    destinationOwner:str,
    sourceAccountNumber:int,
    amount:int):
    source_owner_accounts = get_accounts_by_owner(sourceOwner)
    destination_owner_accounts = get_accounts_by_owner(destinationOwner)
    if len(source_owner_accounts)<sourceAccountNumber+1:
        raise ValueError("account number does not exist")
    source_account_id = source_owner_accounts[sourceAccountNumber][const.ID]
    if len(destination_owner_accounts) == 0:
        raise ValueError("destination account does not has an account")
    destination_account_id = destination_owner_accounts[0][const.ID]

    try:
        current_time = get_current_time.get_current_time()
        post_transaction.post_transaction(source_account_id,
        destinationOwner,
        const.DEBIT,
        "Transfer balance to "+destinationOwner,
        amount,
        current_time)
    except:
        raise PostTransactionError("fail to post transaction")

    try:
        post_transaction.post_transaction(destination_account_id,
        sourceOwner,
        const.CREDIT,
        "Receive balance to "+sourceOwner,
        amount,
        current_time)
    except:
        raise PostTransactionError("fail to post transaction")




    
