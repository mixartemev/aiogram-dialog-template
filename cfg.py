from typing import NamedTuple
from environs import Env


class Cfg(NamedTuple):
    __env = Env()
    __env.read_env()

    BOT_TOKEN = __env.str('BOT_TOKEN')
    WH_HOST = __env.str('WH_HOST')
    BOT_PATH = f"/wh/{BOT_TOKEN}"
    APP_PORT = __env.int('APP_PORT')
