from aiogram.types import ChatMemberUpdated

from loader import dp
from models import UserModel

s_map = {
    'kicked': True,
    'member': False,
}


async def set_my_status(my_chat_member: ChatMemberUpdated, user: UserModel):
    user.blocked = s_map[my_chat_member.new_chat_member.status]
    await user.save()

dp.my_chat_member.register(set_my_status)
