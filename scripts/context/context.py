
# standard
import os
import json

# packages

# internal
from utility import const, env

class Context:

    _DATA = {}

    _INITIALIZED = False

    @staticmethod
    def initialize(config_file_path:str=None):
        if not config_file_path:
            raise ValueError('config file not found')
        
        with config_file_path.open() as file:
            CONFIG_DATA = json.loads(file.read())

        # load api key
        Context._DATA[const.API_KEY] = CONFIG_DATA[env.API_KEY]

        # load base url
        Context._DATA[const.BASE_URL] = CONFIG_DATA[env.BASE_URL]

        # load content type
        Context._DATA[const.CONTENT_TYPE] = CONFIG_DATA[env.CONTENT_TYPE]

        Context._DATA[const.HEADERS] = {
            const.X_API_KEY : Context._DATA[const.API_KEY],
            const.CONTENT_TYPE : Context._DATA[const.CONTENT_TYPE]
        }
        
        _INITALIZED = True

    @staticmethod
    def data():
        return Context._DATA

    @staticmethod
    def initialized():
        return Context._INITIALIZED
        