from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.utils.i18n.core import I18n

from aiogram_dialog import DialogRegistry

from cfg import Cfg

bt = Bot(token=Cfg.BOT_TOKEN, session=AiohttpSession(), parse_mode='HTML')
dp = Dispatcher()

registry = DialogRegistry(dp)  # for dialogs

i18n = I18n(path='locales', default_locale="en", domain='dd')
_ = i18n.gettext
