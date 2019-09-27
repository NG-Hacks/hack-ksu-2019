
# standard
import logging
import time

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

    def _update(self):
        self._create()
        self._initialize()

    def get_transactions(self):
        '''
            This function will get every transaction from 'list_transactions' 
            and add it to the appropriate owner in self._tables.
        '''
        for owner in self._tables[const.OWNERS]:
            for account in self._tables[const.OWNERS][owner]:
                self._tables[const.OWNERS][owner][account][const.TRANSACTIONS] = \
                        Endpoints.list_transactions(accountID=account)[const.DATA]
        # stagger requests so they don't clog up database
        time.sleep(0.2)
        
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
            # see if owner is already in tables
            try:
                test = self._tables[const.OWNERS][account[const.OWNER]]
            # if key error, user was not there. Create it
            except KeyError:
                try:
                    self._tables[const.OWNERS][account[const.OWNER]] = {}

                # if key error happens here, there was no user associated
                # with the account
                except KeyError:
                    self._tables[const.OWNERS][const.NO_OWNER] = {
                        **self._tables[const.OWNERS][const.NO_OWNER],
                        account[const.ID] : {
                            const.BALANCE : account[const.BALANCE]
                        }
                    }

                    continue

            self._tables[const.OWNERS][account[const.OWNER]] = {
                        **self._tables[const.OWNERS][account[const.OWNER]],
                        account[const.ID] : {
                            const.BALANCE : account[const.BALANCE]
                        }
                    }
