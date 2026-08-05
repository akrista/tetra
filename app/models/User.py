"""User Model."""

from typing import ClassVar

from masonite.authentication import Authenticates
from masonite.authorization import Authorizes
from masonite.notification import Notifiable
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, belongs_to_many


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

    @belongs_to_many(
        local_foreign_key="user_id", other_foreign_key="role_id", table="role_user"
    )
    def roles(self):
        from app.models.Role import Role

        return Role

    def is_verified(self) -> bool:
        return getattr(self, "verified_at", None) is not None

    def permission_slugs(self) -> set[str]:
        slugs = set()
        for role in self.roles:
            for permission in role.permissions:
                slugs.add(permission.slug)
        return slugs

    def has_permission(self, slug: str) -> bool:
        if self.is_owner:
            return True
        return slug in self.permission_slugs()

    def can(self, slug: str) -> bool:
        return self.has_permission(slug)

    def role_names(self) -> list[str]:
        return [role.name for role in self.roles]
