"""Permission Model. Global catalog shared by every tenant."""

from typing import ClassVar

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to_many


class Permission(Model):
    __fillable__: ClassVar[list[str]] = ["slug", "name"]

    @belongs_to_many(
        local_foreign_key="permission_id",
        other_foreign_key="role_id",
        table="permission_role",
    )
    def roles(self):
        from app.models.Role import Role

        return Role
