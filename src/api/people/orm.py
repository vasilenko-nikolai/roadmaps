from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

from utils import BaseOrm


class PersonOrm(BaseOrm):

    __tablename__ = 'people'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, comment="Имя")
    surname: Mapped[str] = mapped_column(String(50), nullable=False, comment="Фамилия")
    email: Mapped[str] = mapped_column(nullable=False, comment="Электронная почта", unique=True)
    date_create: Mapped[datetime] = mapped_column(server_default=func.now, nullable=False, comment="Дата регистрации пользователя")
    avatar: Mapped[str] = mapped_column(nullable=False, comment="Путь до изображения аватарки пользователя")
    password: Mapped[str] = mapped_column(nullable=False, comment="Хешированный пароль пользователя")