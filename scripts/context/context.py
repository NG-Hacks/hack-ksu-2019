
# standard
import os
import json

# packages

# internal
from utility import const, env

class Context:

    _DATA = {}

    _INITIALIZED = False

    def initialize(config_file_path:str=None):
        if not config_file_path:
            raise ValueError('config file not found')
        
        with config_file_path.open() as file:
            CONFIG_DATA = json.loads(file.read())

        # load api key
        Context._DATA[const.API_KEY] = CONFIG_DATA[env.API_KEY]

        # load base url
        Context._DATA[const.BASE_URL] = CONFIG_DATA[env.BASE_URL]

        _INITALIZED = True

    def data():
        return Context._DATA

    def initialized():
        return Context._INITIALIZED
        