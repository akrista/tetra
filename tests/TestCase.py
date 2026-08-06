from datetime import UTC, datetime

from masonite.facades import Hash
from masonite.tests import TestCase as MasoniteTestCase

from app.models.Tenant import Tenant
from app.models.User import User


class TestCase(MasoniteTestCase):
    def setUp(self):
        super().setUp()
        # ponytail: wipe the relevant tables between tests so slug/email
        # uniqueness doesn't bleed across tests. Faster than re-migrating.
        # Best-effort: missing tables are fine on the first test before any
        # migration has run.
        builder = self.application.make("builder").new()
        for table in (
            "password_resets",
            "users",
            "tenants",
            "notifications",
            "roles",
            "permissions",
            "role_user",
            "permission_role",
        ):
            try:
                builder.table(table).delete()
            except Exception:  # noqa: BLE001, S110
                pass
        # ponytail: wipe the throttle counter so the 5/minute per-IP limit
        # doesn't carry across tests (file cache persists on disk).
        self.application.make("cache").store().flush()

    def make_tenant(self, name="Acme Workspace", slug=None):
        from app.utils.slug import slugify

        if slug is None:
            slug = slugify(name)
        return Tenant.create({"name": name, "slug": slug})

    def make_user(
        self,
        tenant=None,
        name="Test User",
        email="user@example.com",
        password="password1234",
        owner=True,
        verified=True,
    ):
        if tenant is None:
            tenant = self.make_tenant()
        return User.create(
            {
                "name": name,
                "email": email,
                "password": Hash.make(password),
                "tenant_id": tenant.id,
                "is_owner": owner,
                "verified_at": datetime.now(UTC).isoformat(sep=" ")
                if verified
                else None,
            }
        )

    def login_as(self, user):
        self.post("/login", {"email": user.email, "password": "password1234"})

    def make_role(self, tenant=None, name="Administrador", permissions=None):
        from app.models.Permission import Permission
        from app.models.Role import Role
        from app.utils.slug import slugify

        if tenant is None:
            tenant = self.make_tenant()
        role = Role.create(
            {"tenant_id": tenant.id, "name": name, "slug": slugify(name)}
        )
        if permissions:
            builder = self.application.make("builder").new()
            for slug in permissions:
                perm = Permission.where("slug", slug).first()
                if not perm:
                    perm = Permission.create({"slug": slug, "name": slug})
                builder.table("permission_role").create(
                    {"role_id": role.id, "permission_id": perm.id}
                )
        return role
