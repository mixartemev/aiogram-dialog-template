from enum import Enum

from beanie import Document
from pydantic import Field

from models.base import TimeBaseModel


class UserRoles(str, Enum):
    new = 'new'
    user = 'user'
    admin = 'admin'


class UserModel(TimeBaseModel):
    id: int = Field(...)
    language: str = 'en'
    real_language: str = 'en'
    role: UserRoles = Field(default=UserRoles.new)
    status: str = 'member'

    class Collection:
        name = "UserModel"


class Ids(Document):
    id: int = Field(...)
    #
    # class Collection:
    #     name = "UserModel"
