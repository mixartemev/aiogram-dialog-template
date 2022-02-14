from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.dispatcher.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from aiogram.utils.i18n.core import I18n

from aiogram_dialog import DialogRegistry

from cfg import Cfg
from utils import logger
from utils.db.mongodb import MyBeanieMongo

logger.setup_logger()
bt = Bot(token=Cfg.BOT_TOKEN, session=AiohttpSession(), parse_mode='HTML')
storage = RedisStorage.from_url(Cfg.REDIS_DSN, key_builder=DefaultKeyBuilder(with_destiny=True))
mongo = MyBeanieMongo()
dp = Dispatcher(storage=storage)

registry = DialogRegistry(dp)  # for dialogs

i18n = I18n(path='locales', default_locale="en", domain='dd')
_ = i18n.gettext
