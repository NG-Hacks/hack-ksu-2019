
# standard
import logging

# packages

# internal
from context.context import Context
from utility import const
from utility.tablemap import Tablemap
from endpoints import Endpoints

class Connection(Tablemap):
    def _create(self):
        '''
            This class extends Tablemap so that it can be accessed similarly
            to a dict. When a Tablemap object is created it will run the _create()
            function. Therefore, this function runs when the Connection object is
            created. It will grab all of the accounts and store it in self._tables
            by using 'list_accounts'
        '''
        self._key = const.DATA
        self._tables[const.ACCOUNTS] = \
            Endpoints.list_accounts()[const.DATA][const.ACCOUNTS]

    def _initialize(self):
        self.get_owners()
        self.get_transactions()

    def get_transactions(self):
        '''
            This function will get every transaction from 'list_transactions' 
            and add it to the appropriate owner in self._tables.
        '''
        for owner in self._tables[const.OWNERS]:
            for account in self._tables[const.OWNERS][owner]:
                self._tables[const.OWNERS][owner][account][const.TRANSACTIONS] = \
                        Endpoints.list_transactions(accountID=account)[const.DATA]

    def get_owners(self):
        '''
            This function will find each unique owner in the database by using
            the accounts from self._tables[const.ACCOUNTS]. It will add the owners 
            to it's own tables. There is a 'no_owner' owner (this name should not be 
            used for an owner name) for cases where accounts have no owner.

            Structure:

            self._tables = {
                const.OWNERS : {
                    <owner_name> : {
                        <accountID> : {
                            const.BALANCE : {
                                <account_balance>
                            },
                            const.TRANSACTIONS : {
                                [transactions]
                            }
                        }
                    }
                }
            }
        '''
        self._tables[const.OWNERS] = {
            const.NO_OWNER : {}
        }

        for account in self._tables[const.ACCOUNTS]:
            try:
                # attempt to append the account id and balance to the
                # owners table by key of the owner name
                self._tables[const.OWNERS] = {
                    **self._tables[const.OWNERS],
                    account[const.OWNER] : {
                        **account[const.OWNER],
                        account[const.ID] : {
                            const.BALANCE : account[const.BALANCE]
                        }
                    }
                }

            except TypeError:
                # if type error occurs in this step, it can't append
                # because the dict doesn't exist yet.
                self._tables[const.OWNERS] = {
                    **self._tables[const.OWNERS],
                    account[const.OWNER] : {
                        account[const.ID] : {
                            const.BALANCE : account[const.BALANCE]
                        }
                    }
                }

            except KeyError:
                # if key error occurs, it is because the account has no
                # owner.

                # append the no owner key with the account
                # balance and id
                self._tables[const.OWNERS] = {
                    **self._tables[const.OWNERS],
                    const.NO_OWNER : {
                        **self._tables[const.OWNERS][const.NO_OWNER],
                        account[const.ID] : {
                            const.BALANCE : account[const.BALANCE]
                        }
                    }
                }
            