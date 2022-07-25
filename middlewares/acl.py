from typing import Callable, Any, Awaitable, Optional

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject, Chat, User

from models import UserModel
from utils.notifications.new_notify import notify_new_user


class ACLMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any],
    ) -> Any:
        user: Optional[User] = data.get("event_from_user")
        chat: Optional[Chat] = data.get("event_chat")

        bot: Bot = data.get("bot")

        if user and chat and chat.type == 'private':
            if not (user_db := await UserModel.find_one(UserModel.id == user.id)):
                user_db = await UserModel(id=user.id, language_code=user.language_code, nick=user.username).create()
                await notify_new_user(user, bot)

            data["user"] = user_db

        return await handler(event, data)
