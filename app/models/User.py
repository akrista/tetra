"""User Model."""

from typing import ClassVar

from masonite.authentication import Authenticates
from masonite.authorization import Authorizes
from masonite.notification import Notifiable
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to


class User(Model, Authenticates, Authorizes, Notifiable):
    """User Model. One row per human; tenant-scoped via tenant_id."""

    __fillable__: ClassVar[list[str]] = [
        "name",
        "email",
        "password",
        "phone",
        "tenant_id",
        "is_owner",
        "verified_at",
    ]
    __hidden__: ClassVar[list[str]] = ["password", "remember_token"]
    __auth__ = "email"

    @belongs_to("tenant_id", "id")
    def tenant(self):
        from app.models.Tenant import Tenant

        return Tenant

    def is_verified(self) -> bool:
        return getattr(self, "verified_at", None) is not None
