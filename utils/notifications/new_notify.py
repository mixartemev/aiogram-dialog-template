from aiogram import Bot, html
from aiogram.types import User

from utils.broadcast import broadcast_smth, get_admins


async def notify_new_user(user: User, bot: Bot) -> int:
    pics = await bot.get_user_profile_photos(user.id)
    txt = [
        "#new_user",
        f"Имя: {html.quote(user.full_name)}",
        f'id: <a href="tg://user?id={user.id}">{user.id}</a>',
        f"username: @{user.username}",
    ]
    photo = None
    if pics and pics.total_count > 0:
        photo = pics.photos[0][-1].file_id
    if photo:
        return await broadcast_smth(await get_admins(), bot.send_photo, False, 'id', photo=photo, caption='\n'.join(txt))
    return await broadcast_smth(await get_admins(), bot.send_message, False, 'id', text='\n'.join(txt))
