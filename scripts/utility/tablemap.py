
# standard
import logging

# internal
from utility import const

_LOGGER = logging.getLogger(__name__)

class Tablemap():
    def __init__(self):
        self._tables = {}
        self._key = None
        self._create()

    def _create(self):
        pass

    def __getitem__(self, key):
        return self._tables[key]

    def __setitem__(self, key, item):
        self._tables[key] = item
    
    def __delitem__(self, key):
        del self._tables[key]

    def has_key(self, key):
        return key in self._tables

    def __contains__(self, item):
        return item in self._tables
    
    def __repr__(self):
        return repr(self._tables)
        
    def __iter__(self):
        return (self._tables[table] for table in self._tables)
