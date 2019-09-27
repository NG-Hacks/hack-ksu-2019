from utility import const
import matplotlib.pyplot as plt 
from prettytable import PrettyTable

def plot_balance(owner_info):
    owner_accounts = owner_info.keys()
    for owner_account in owner_accounts:
        account_info = owner_info[owner_account]
        account_transactions = account_info[const.TRANSACTIONS]
        trans_info = get_transacions_date_amount(account_transactions)
        if trans_info != None:
            most_recent_transaction = account_transactions[0]
            trans_amount = trans_info[0]
            trans_date = trans_info[1]
            make_plot(owner_account, trans_amount, trans_date)
            make_table(owner_account, trans_amount[-1], most_recent_transaction)
    



def get_transacions_date_amount(account_transactions):
    if len(account_transactions) == 0:
        return None
    transactions_date = ["Initial Balance"]
    trasactions_amount = [0]
    j = 0
    for i in range(len(account_transactions)-1, -1, -1 ):
        transaction_info = account_transactions[i]
        amount = int(transaction_info[const.AMOUNT])
        if transaction_info[const.TYPE] == const.CREDIT:
            trasactions_amount.append(amount+trasactions_amount[j])
        else:
            trasactions_amount.append(-amount+trasactions_amount[j])
        j += 1
        transactions_date.append(format_date(transaction_info[const.DATE]))
    return (trasactions_amount, transactions_date)

def make_plot(account_id, transactions_amount, transactions_date):
    plt.plot(transactions_date, transactions_amount, marker="o")
    plt.title("Account: "+account_id)
    plt.xlabel("Transaction Date")
    plt.ylabel("Balance")
    plt.show()
    

def make_table(account_id, balance, mr_trans):
    col_labels = ["Account ID","Balance", "Most Recent Transaction Type", "Date"]
    table_vals = [account_id ,balance, mr_trans[const.COUNTER_PARTY], format_date(mr_trans[const.DATE])]
    tb = PrettyTable()
    tb.field_names = col_labels
    tb.add_row(table_vals)
    print(tb)

def format_date(date):
    day = date.split("T")[0]
    time = date.split("T")[1].split(".")[0]
    return day+"\n "+time

