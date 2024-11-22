from datetime import datetime

from pydantic import Field

from utils import BaseData


class PersonBase(BaseData):
    id: int = Field(description="Уникальный номер пользователя")
    name: str = Field(min_length=2, max_length=50, description="Имя")
    surname: str = Field(min_length=2, max_length=50, description="Фамилия")
    email: str = Field(description="Электронный адрес")
    date_create: datetime = Field(description="Дата регистрации")
    avatar: str = Field(description="Путь до аватарки")