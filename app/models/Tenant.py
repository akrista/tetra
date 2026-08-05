"""Tenant Model."""

from typing import ClassVar

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class Tenant(Model):
    """Tenant Model. Each customer organization is one row."""

    __fillable__: ClassVar[list[str]] = ["name", "slug"]

    @has_many("id", "tenant_id")
    def users(self):
        from app.models.User import User

        return User
