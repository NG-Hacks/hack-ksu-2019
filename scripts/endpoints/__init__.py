
class Endpoints:

    @staticmethod
    def initialize():
        # import endpoints
        from .accounts.accounts_by_owner import accounts_by_owner
        from .accounts.create_account import create_account
        from .accounts.inspect_account import inspect_account
        from .accounts.list_accounts import list_accounts
        from .accounts.update_account_balance import update_account_balance
        from .accounts.update_account_owner import update_account_owner
        from .transactions.delete_transaction import delete_transaction
        from .transactions.inspect_transaction import inspect_transaction
        from .transactions.list_transactions import list_transactions
        from .transactions.post_transaction import post_transaction
        # assign endpoints
        Endpoints.accounts_by_owner = accounts_by_owner
        Endpoints.create_account = create_account
        Endpoints.inspect_account = inspect_account
        Endpoints.list_accounts = list_accounts
        Endpoints.update_acount_balance = update_account_balance
        Endpoints.update_account_owner = update_account_owner
        Endpoints.delete_transaction = delete_transaction
        Endpoints.inspect_transaction = inspect_transaction
        Endpoints.list_transactions = list_transactions
        Endpoints.post_transaction = post_transaction