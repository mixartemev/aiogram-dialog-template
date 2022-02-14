from aiogram import Bot

from utils.broadcast import broadcast_smth, get_admins


async def notify_superusers(bot: Bot) -> int:
    return await broadcast_smth(await get_admins(), bot.send_message, with_counter=False, attribute='id', text='The bot is running!')
