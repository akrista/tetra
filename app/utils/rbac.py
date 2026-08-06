"""RBAC bootstrap helpers shared by migrations, seeders and the register flow."""

import os

from masonite.facades import Hash
from masoniteorm.query import QueryBuilder

from app.models.Permission import Permission
from app.models.Role import Role
from app.models.Tenant import Tenant
from app.models.User import User
from config.database import DB

PERMISSIONS = [
    ("users.manage", "Gestionar usuarios"),
    ("roles.manage", "Gestionar roles"),
]

ROLES = {
    "admin": {"name": "Administrador", "slug": "admin"},
    "user": {"name": "Usuario", "slug": "user"},
}


def _env(name: str, default: str) -> str:
    return os.getenv(name, default)


def _pivot(table: str) -> QueryBuilder:
    return QueryBuilder(
        connection_details=DB.get_connection_details(),
        connection="default",
        table=table,
    )


def sync_permission_catalog() -> None:
    """Insert any missing permissions. Idempotent; safe to re-run."""
    for slug, name in PERMISSIONS:
        Permission.first_or_create({"slug": slug}, {"name": name})


def ensure_roles(tenant_id: int) -> dict[str, Role]:
    """Create the standard admin/user roles for a tenant (idempotent).

    The admin role receives every permission in the catalog.
    """
    roles = {}
    for key, attrs in ROLES.items():
        role = Role.first_or_create(
            {"tenant_id": tenant_id, "slug": attrs["slug"]},
            {"name": attrs["name"], "slug": attrs["slug"], "tenant_id": tenant_id},
        )
        roles[key] = role

    pivot = _pivot("permission_role")
    for slug, _ in PERMISSIONS:
        permission = Permission.where("slug", slug).first()
        if permission and not (
            pivot.where("role_id", roles["admin"].id)
            .where("permission_id", permission.id)
            .first()
        ):
            pivot.create({"role_id": roles["admin"].id, "permission_id": permission.id})

    return roles


def attach_role(user_id: int, role_id: int) -> None:
    """Attach a role to a user. Idempotent."""
    pivot = _pivot("role_user")
    if not pivot.where("user_id", user_id).where("role_id", role_id).first():
        pivot.create({"user_id": user_id, "role_id": role_id})


def seed_app_basics() -> None:
    """Provision the app baseline: permissions, default tenant, roles, owner.

    The tenant and owner are driven by TETRA_* env vars (see .env-example)
    so each deployment can provision its own first account. Idempotent.
    """
    sync_permission_catalog()

    slug = _env("TETRA_TENANT_SLUG", "acme")
    tenant = Tenant.first_or_create(
        {"slug": slug},
        {"name": _env("TETRA_TENANT_NAME", "Acme Workspace"), "slug": slug},
    )

    roles = ensure_roles(tenant.id)

    email = _env("TETRA_OWNER_EMAIL", "owner@acme.test")
    owner = User.first_or_create(
        {"email": email},
        {
            "name": _env("TETRA_OWNER_NAME", "Acme Owner"),
            "email": email,
            "password": Hash.make(_env("TETRA_OWNER_PASSWORD", "password1234")),
            "tenant_id": tenant.id,
            "is_owner": True,
            "verified_at": "2026-01-01 00:00:00",
        },
    )
    attach_role(owner.id, roles["admin"].id)
