"""User Model."""

from typing import ClassVar

from masonite.authentication import Authenticates
from masonite.authorization import Authorizes
from masonite.notification import Notifiable
from masoniteorm.models import Model


class User(Model, Authenticates, Authorizes, Notifiable):
    """User Model."""

    __fillable__: ClassVar[list[str]] = ["name", "email", "password", "phone"]
    __hidden__: ClassVar[list[str]] = ["password"]
    __auth__ = "email"
