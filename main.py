import logging
from aiohttp import web
from aiohttp.web_app import Application

from cfg import Cfg
from loader import dp, bt, registry
from dialogs.sg import MainSG
from aiogram.dispatcher.webhook.aiohttp_server import SimpleRequestHandler, setup_application


async def app_startup(a: Application) -> None:  # pragma: no cover
    await bt.set_webhook(Cfg.WH_HOST+Cfg.BOT_PATH)


async def app_shutdown(a: Application) -> None:  # pragma: no cover
    logging.warning("Shutting down..")
    await bt.delete_webhook()  # Remove webhook (not acceptable in some cases)
    await bt.session.close()
    logging.warning("Bye!")


registry.register_start_handler(MainSG.home)  # resets stack and start dialogs on /start command

app = web.Application()
app.on_startup.append(app_startup)
app.on_shutdown.append(app_shutdown)
SimpleRequestHandler(dispatcher=dp, bot=bt).register(app, path=Cfg.BOT_PATH)

web.run_app(app, port=Cfg.APP_PORT)
