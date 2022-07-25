from enum import Enum
from typing import Optional

from beanie import Link
from pydantic import Field
from models.base import TimeBaseModel


class UserRoles(int, Enum):
    new = 0
    user = 1
    admin = 2


class UserIds(TimeBaseModel):
    id: int = Field(...)
    nick: str = None

    class Collection:
        name = "UserModel"


class UserModel(UserIds):
    role: UserRoles = Field(default=UserRoles.new)
    blocked: bool = False
    language_code: str = None
    ref: Optional[Link[UserIds]] = None
