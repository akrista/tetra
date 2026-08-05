"""Role Model. Tenant-scoped; grants permissions to users."""

from typing import ClassVar

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, belongs_to_many


class Role(Model):
    __fillable__: ClassVar[list[str]] = ["name", "slug", "tenant_id"]

    @belongs_to("tenant_id", "id")
    def tenant(self):
        from app.models.Tenant import Tenant

        return Tenant

    @belongs_to_many(
        local_foreign_key="role_id",
        other_foreign_key="permission_id",
        table="permission_role",
    )
    def permissions(self):
        from app.models.Permission import Permission

        return Permission

    @belongs_to_many(
        local_foreign_key="role_id", other_foreign_key="user_id", table="role_user"
    )
    def users(self):
        from app.models.User import User

        return User

    def permission_slugs(self) -> list[str]:
        return [p.slug for p in self.permissions]
