
# standard
import logging
from pathlib import Path

# packages

# internal
from utility import const, env

# find current working path
CUR_PATH = Path(__file__).parent

CONFIG_FOLDER = '.config'
CONFIG_PATH = CUR_PATH/CONFIG_FOLDER
CONFIG_FILE_PATH = CONFIG_PATH/'config.json'

if env.LOG_TO_FILE:
    LOG_FILE = 'api.log'
    LOG_FILE_PATH = CONFIG_PATH/'logs'
    logging.basicConfig(
        filename=LOG_FILE_PATH/LOG_FILE,
        level=env.LOGGING_LEVEL,
        format='%(asctime)s %(message)s'
    )

else:
    logging.basicConfig(
        level=env.LOGGING_LEVEL,
        format='%(asctime)s %(message)s'
    )

_LOGGER = logging.getLogger(__name__)

if __name__ == '__main__':

    # init context
    _LOGGER.info('initiailizing context')
    from context.context import Context
    Context.initialize(CONFIG_FILE_PATH)

    # init endpoints
    _LOGGER.info('initiailizing endpoints')
    from endpoints import Endpoints
    Endpoints.initialize()

    # init application
    from connection import conn
    conn._initialize()

    for owner in conn[const.OWNERS]:
        print(conn[const.OWNERS][owner])